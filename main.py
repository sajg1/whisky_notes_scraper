from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

whisky_notes_reviews_url = 'https://www.whiskynotes.be/whisky-reviews-by-distillery/'
CHROME_DRIVER_PATH = '/Users/admin/Development/chromedriver'
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)


req = Request(whisky_notes_reviews_url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# BEAUTIFULSOUP USED TO FIND ALL THE LINKS TO EACH DISTILLERIES PAGE AND ADD THEM TO A LIST
page_soup = soup(webpage, 'html.parser')
distilleries = page_soup.find_all(name='li', class_='cat-item')

distillery_links = [distillery.find('a')['href'] for distillery in distilleries]
scottish_distillery_links = distillery_links[13:]

# SELENIUM USED TO MANIPULATE THE DOM AND FIND THE WHISKY DESCRIPTIONS
driver.get(scottish_distillery_links[0])
whisky_links = driver.find_elements(By.CLASS_NAME, 'entry-permalink')
print(len(whisky_links))
aberfeldy_12 = whisky_links[0]
aberfeldy_12.click()
description = driver.find_element(By.CLASS_NAME, 'entry-content')
p_tags = description.find_elements(By.TAG_NAME, 'p')
for p in p_tags:
    print(p.text)





