import requests
from bs4 import BeautifulSoup
import re
import json


url = "https://www.taobao.com/"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')
title = soup.title
paras = soup.find_all('p')
anchors = soup.find_all('a')
for link in anchors:
    anchors = soup.find_all('a')
    all_links = set()

for link in anchors:
        if(link.get('href') != '#'):
            linkText = "https://www.taobao.com/" +link.get('href')
            all_links.add(link)
            print(linkText)

