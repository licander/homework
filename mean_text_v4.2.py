# -*- coding: utf-8 -*-
# Метод разделяет текст на теговые и не теговые области. Достаточно большая нетеговая область - текст.
# Теги форматирования - как слова
# попытка удалить одиночные теги
import re
import chardet
import copy

def get_decode_html(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
        coding = chardet.detect(data)
        if coding['language'] != 'Russian':
            coding['encoding'] = 'utf8'
        data = data.decode(coding['encoding'])   
    return data

def write_in_file(file_name, html, code):
    new_file = open(file_name, 'w', encoding=code) 
    new_file.write(html) 
    new_file.close()

def first_part(text):
    title = re.search(r'<title[^>]*?>.*?</title>', text, flags=re.S|re.I)
    if title:
        first_part = '<html><head>' + title.group(0) + '</head><body>'
    else:
        first_part = '<html><head></head><body>'
    return first_part

def clear_html(text):
    text = re.sub(r'<!DOCTYPE html>', '', text, flags=re.S|re.I)
    text = re.sub(r'<head[^>]*?>.*?</head>', '', text, flags=re.S|re.I)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S|re.I)
    text = re.sub(r'<script[^>]*?>.*?</script>', '<script></script>', text, flags=re.S|re.I)
    text = re.sub(r'<style[^>]*?>.*?</style>', '<style></style>', text, flags=re.S|re.I)
    text = re.sub(r'<form[^>]*?>.*?</form>', '<form></form>', text, flags=re.S|re.I)
    text = re.sub(r'\n', ' ', text, flags=re.S|re.I)
    text = re.sub(r'\s+', ' ', text, flags=re.S|re.I)
    text = re.sub(r'&nbsp;', '', text, flags=re.S|re.I)
    text = re.sub(r'&quot;', '', text, flags=re.S|re.I)
    text = re.sub(r'&rarr;', '', text, flags=re.S|re.I)
    
    text = re.sub(r'<em[^>]*?>', '', text, flags=re.S|re.I)
    text = re.sub(r'</em>', '', text, flags=re.S|re.I)
    text = re.sub(r'<strong[^>]*?>', '', text, flags=re.S|re.I)
    text = re.sub(r'</strong>', '', text, flags=re.S|re.I)
    text = re.sub(r'<b\s[^>]*?>', '', text, flags=re.S|re.I)
    text = re.sub(r'<b>', '', text, flags=re.S|re.I)
    text = re.sub(r'</b>', '', text, flags=re.S|re.I)
    text = re.sub(r'<ins[^>]*?>', '', text, flags=re.S|re.I)
    text = re.sub(r'</ins>', '', text, flags=re.S|re.I)
    text = re.sub(r'<font[^>]*?>', '', text, flags=re.S|re.I)
    text = re.sub(r'</font>', '', text, flags=re.S|re.I)
    text = re.sub(r'<center[^>]*?>', '', text, flags=re.S|re.I)
    text = re.sub(r'</center>', '', text, flags=re.S|re.I)
    
    text = re.sub(r'<h[0-9][^>]*?>', ' !F!h1 ', text, flags=re.S|re.I)
    text = re.sub(r'</h[0-9]>', ' !F!/h1 ', text, flags=re.S|re.I)
    text = re.sub(r'<br[^>]*?>', ' !F!br ', text, flags=re.S|re.I)
    text = re.sub(r'</br>', ' !F!br ', text, flags=re.S|re.I)
    text = re.sub(r'<p[^>]*?>', ' !F!p ', text, flags=re.S|re.I)
    text = re.sub(r'</p>', ' !F!/p ', text, flags=re.S|re.I)
    text = re.sub(r'<([a-z]+)\s[^>]*?>', '<\g<1>>', text, flags=re.S|re.I)

    text = re.sub(r'\n', ' ', text, flags=re.S|re.I)
    text = re.sub(r'>', '> ', text, flags=re.S|re.I)
    text = re.sub(r'<', ' <', text, flags=re.S|re.I)
    text = re.sub(r'\s+', ' ', text, flags=re.S|re.I)
    return text

def is_tag(word):
    if word[0] == '<' and word[-1] == '>':
        return 1
    else:
        return 0
    
def list_to_text(tx):
    new_text = ' '.join(tx)
    new_text =  new_text.replace('!F!h1', '<h1>')
    new_text =  new_text.replace('!F!/h1', '</h1>')
    new_text =  new_text.replace('!F!/h1', '</h1>')
    new_text =  new_text.replace('!F!br', '</br>')
    new_text =  new_text.replace('!F!p', '<p>')
    new_text =  new_text.replace('!F!/p', '</p>')
    new_text =  new_text.replace('!O!ul', '<ul>')
    new_text =  new_text.replace('!O!/ul', '</ul>')
    new_text =  new_text.replace('!O!ol', '<ul>')
    new_text =  new_text.replace('!O!/ol', '</ul>')
    new_text =  new_text.replace('!O!li', '<li>')
    new_text =  new_text.replace('!O!/li', '</li>') 
    return new_text

def search_bad_tag(ul, good_tag):
    tag_list = re.findall(r'<([a-z]+)>', ul)
    for tag in tag_list:
        if tag not in good_tag:
            return 0
    return 1    
    
def ul_replace(text):
    ul_list = re.findall(r'<ul>.*?</ul>', text)
    ol_list = re.findall(r'<ol>.*?</ol>', text)
    for ul in ul_list + ol_list:
        if search_bad_tag(ul, ['ul', 'ol', 'li']):
            new_ul = re.sub(r'<ul[^>]*?>', ' !O!ul ', ul, flags=re.S|re.I)
            new_ul = re.sub(r'</ul>', ' !O!/ul ', new_ul, flags=re.S|re.I)
            new_ul = re.sub(r'<ol[^>]*?>', ' !O!ol ', new_ul, flags=re.S|re.I)
            new_ul = re.sub(r'</ol>', ' !O!/ol ', new_ul, flags=re.S|re.I)
            new_ul = re.sub(r'<li[^>]*?>', ' !O!li ', new_ul, flags=re.S|re.I)
            new_ul = re.sub(r'</li>', ' !O!/li ', new_ul, flags=re.S|re.I)
            text =  text.replace(ul, new_ul)
    return text
        
def span_replace(text):
    span_list = re.findall(r'<span>[^<>]*?</span>', text)
    for span in span_list:
        if len(span) > 30:
            new_span = re.sub(r'<span>', '', span, flags=re.S|re.I)
            new_span = re.sub(r'</span>', '', new_span, flags=re.S|re.I)
            text =  text.replace(span, new_span)
    return text

def num_tag(group):
    num = 0
    for word in group[1:]:
        if re.match(r'![A-Z]!', word):
            num += 1
    return num

def delete_a_from_text(group_list):
    index = 1
    while index < len(group_list)-3:
        try:
            group_list[index+3]
        except IndexError:
            break
             
        if group_list[index] == [1, '<a>'] and group_list[index+2] == [1, '</a>']\
        and len(group_list[index-1]) > 7 and len(group_list[index+3]) > 7:
            group_list[index-1] = group_list[index-1] + group_list[index+1][1:] + group_list[index+3][1:]
            del group_list[index]
            del group_list[index]
            del group_list[index]
            del group_list[index]
        else:
            index += 1

    return group_list            
    
for ind in range(2618,3743):    
    text = get_decode_html('html_for_baden/'+str(ind)+'.txt')
    if (len(text) < 5000):
        write_in_file('html/'+str(ind)+'_v4.2.html', '', 'utf8')
        print(ind)
        continue
    
    all_text = first_part(text)
    text = clear_html(text)
    text = span_replace(span_replace(text))
    text = ul_replace(text)

    text_list = text.split()
    
    group_list = []
    
    word_type = 1
    sentence = [1]
    
    for word in text_list:
        if word_type == is_tag(word):
            sentence.append(word)
        else:
            group_list.append(sentence)
            word_type = is_tag(word)
            sentence = []
            sentence.append(word_type)
            sentence.append(word)
            
            
    group_list.append(sentence)  
    
    group_list = delete_a_from_text(group_list)
    take_list = []
    for index, group in enumerate(group_list):
        if group[0] == 0 and len(group) - num_tag(group) > 45 and index not in take_list:
            res = group[1:]
            #print(res)
            take_list.append(index)
            if len(group_list[index-1]) == 2 and index-2 not in take_list:
                res = group_list[index-2][1:] + res
                take_list.append(index-2)
            if len(group_list[index+1]) == 2 and index+2 not in take_list:
                res = res + group_list[index+2][1:]
                take_list.append(index+2)
            all_text = all_text + list_to_text(res) + '</br></br>'       

    
    all_text = all_text + '</body></html>'
    write_in_file('html/'+str(ind)+'_v4.2.html', all_text, 'utf8')
    print(ind)



