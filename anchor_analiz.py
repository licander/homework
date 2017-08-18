 # coding: utf8
import re
f = open('konzeptual.ru2.csv', encoding='utf-8')
res = open('res.csv', 'w')
text = f.readline()

while text:
    text = text.split(';')
    num = text[0]
    donor = text[1]
    print(donor)
    text = f.readline()
    html_file = open('html_konzeptual/'+num+'.txt', encoding='utf-8')
    html = html_file.read()
    html_file.close()
    links = re.findall(r'<a.*?<\/a>', html, flags=re.S|re.I)
    for link in links:
        url = re.search(r'href="[^"]*"', link)
        anchor = re.sub(r'<[^>]*?>', '', link, flags=re.S|re.I)
        anchor = re.sub(r'\n', '', anchor, flags=re.S|re.I)
        anchor = re.sub(r'\nm', '', anchor, flags=re.S|re.I)
        anchor = re.sub(r'\s+', ' ', anchor, flags=re.S|re.I)
        anchor = re.sub(r'&nbsp;', ' ', anchor, flags=re.S|re.I)
        anchor = anchor.strip()
        if url and anchor:
            clean_url = url.group(0)[6:-1]
            res.write(clean_url + ';' + anchor  + ';' + donor )
f.close()
res.close()

