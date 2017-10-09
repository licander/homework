# -*- coding: utf-8 -*-
from urllib.parse import urlencode
from mean_text_from_url import get_mean_text_without_format, get_content_from_url
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def from_text_to_trigram(text):
    text_list = text.split()
    trigram_set = set()
    for i in range(2, len(text_list)):
        trigram_set.add(text_list[i-2] + ' ' + text_list[i-1] + ' ' + text_list[i])
    return(trigram_set)
        

def get_serp(query, region, deep):
    url = 'http://search-analytics.ru/services/for_python/position.php'
    data = {
            'query': query,
            'region': region,
            'deep': deep
            }
    url = '?'.join((url, urlencode(data)))
    serp = get_content_from_url(url)
    serp = serp['result'].split()
    return(serp)


def get_serp_texts(serp):
    text_dict = {}
    for url in serp:
        text = get_mean_text_without_format(url)
        if (type(text) == int):
            text_dict[url] = set()
            continue
        text = from_text_to_trigram(text)
        text_dict[url] = text
    return(text_dict)


def compare_trigram(set1, set2):
    all_trigram = len(set1)
    unique_trigram = 0    
    for trigram in set1:
        if trigram not in set2:
            unique_trigram +=1
    return(unique_trigram, all_trigram)


def join_all_without_one(text_dict, the_url):
    all_texts = set()
    for url, text in text_dict.items():
        if url != the_url:
            all_texts = all_texts | text
    return(all_texts)
        

def top_unique(query, region):
    serp = get_serp(query, region)
    text_dict = get_serp_texts(serp)
    result = {}
    for url in serp:
        result[url] = compare_trigram(text_dict[url], join_all_without_one(text_dict, url))
    return(result)
        

def compare_urls(url1, url2):
    text1 = get_mean_text_without_format(url1)
    text2 = get_mean_text_without_format(url2)
    if (type(text1) == int or type(text2) == int):
        return 1
    trigram1 = from_text_to_trigram(text1)
    trigram2 = from_text_to_trigram(text2)
    res = compare_trigram(trigram1, trigram2)
    return res


def find_urls_from_same_site(query1, query2, region):
    serp1 = get_serp(query1, region)
    serp2 = get_serp(query2, region)
    domain_dict1 = {}
    domain_dict2 = {}
    
    for url in serp1:
        url_list = url.split('/')
        domain_dict1[url_list[2]] = url
    for url in serp2:
        url_list = url.split('/')
        domain_dict2[url_list[2]] = url        

    domains1 = set(domain_dict1.keys())
    domains2 = set(domain_dict2.keys())
    pair_domain = domains1 & domains2
    
    for domain in pair_domain:
        if domain_dict1[domain] != domain_dict2[domain]:
            print((domain_dict1[domain], domain_dict2[domain]))
            print(compare_urls(domain_dict1[domain], domain_dict2[domain]))
    return(0)   
    
    
# print(top_unique('Источники напряжения 12V в защитном кожухе', '213'))
# print(find_urls_from_same_site('Набор 6 бокалов для шампанского 180 мл', 'Набор 6 бокалов для шампанского Bubbles 175 мл', '213'))
# print(compare_urls('http://www.vamsvet.ru/catalog/product/odeon_lyustra-2565-7c/', 'http://www.vamsvet.ru/catalog/product/lyustra-potolochnaya-a2550pl-3cc/'))
