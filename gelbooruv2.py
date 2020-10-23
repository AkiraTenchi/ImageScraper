import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import os
import time

searchTerm = 'trap'
url = 'https://gelbooru.me/index.php?page=dapi&s=post&q=index&tags=' + searchTerm + '&limit=100'
x=0

rawSource = requests.get(url).content

source = bs(rawSource, 'html.parser')

posts = source.findAll('post')

if not os.path.exists('delbooru'):
    os.makedirs('delbooru')
os.chdir('delbooru')

for post in posts:
    img_url = post['file_url']
    response = requests.get(img_url)
    if response.status_code == 200:
        with open('img-' + str(x) + '.jpg', 'wb') as f:
            f.write(requests.get(img_url).content)
            f.close()
            x += 1
    print(str(x) + "/" + str(len(posts)))