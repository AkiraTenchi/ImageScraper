import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

url = 'https://gelbooru.com/index.php?page=post&s=view&id=5614231&tags=trap'

picture_amount = 10
x = 0

browser = webdriver.Firefox()  

#create dir for imgages
if not os.path.exists('delbooru'):
    os.makedirs('delbooru')
os.chdir('delbooru')

for i in range(0, picture_amount):
    browser.get(url)
    html_source = browser.page_source
    soup = bs(html_source,'html.parser') 
    try: 
        img_tag = soup.find(id='image')
        img_url = img_tag['src'] 
        print(img_url)
        response = requests.get(img_url)
        if response.status_code == 200:
            with open('img-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(img_url).content)
                f.close()
                x += 1
    except:
        pass
    browser.execute_script('navigateNext()')
    time.sleep(3)
    url = browser.current_url

browser.quit()


