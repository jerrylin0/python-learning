# -*- coding: utf-8 -*-
#urlparse
import requests

url = 'https://dev.mysql.com/downloads/file/?id=477210'

html = requests.get(url)
html.encoding = 'utf-8'

htmllist = html.text.splitlines()
n = 0
for row in htmllist:
    if 'mysql' in row:
        n += 1

print('find "mysql" string {} times!' .format(n))

# -*- coding: utf-8 -*-
#regex
import requests
import re

regex = re.compile('[a-zA-Z\._]+@[a-zA-Z\.]+\.[a-zA-Z\.]+')
url = 'https://auth.cht.com.tw/ldaps/'
html = requests.get(url)
emails = regex.findall(html.text)
for email in emails:
    print(email)

# -*- coding: utf-8 -*-
#regex
import requests
from bs4 import BeautifulSoup


url = 'http://www.e-happy.com.tw/'
html = requests.get(url)
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text ,'html.parser')

links = sp.find_all(['a','img'])
for link in links:
    href = link.get("href")
    if href != None and href.startswith("http"):
        print(href)







