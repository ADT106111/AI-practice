'''
#Python 22 抓網站上資料
#抓系上網站的各種老師信箱
'''
import requests, re
email = re.compile('[a-zA-Z0-9_]+@[a-zA-Z0-9\._]+</a>')
url = 'https://dct.ntcu.edu.tw/intro.php#director'
save_email = []
html = requests.get(url)
html.encoding = 'utf-8'
#print(type(html.text))
#print(html.text)
all_email = email.findall(html.text)
for i in range(len(all_email)):
    save_email = all_email[i].replace('</a>','')
    print(save_email)