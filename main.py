from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from selenium import webdriver
import time

whisky_notes_reviews_url = 'https://www.whiskynotes.be/whisky-reviews-by-distillery/'
# CHROME_DRIVER_PATH = '/Users/admin/Development/chromedriver'
# driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)


req = Request(whisky_notes_reviews_url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

page_soup = soup(webpage, 'html.parser')

distilleries = page_soup.find_all(name='li', class_='cat-item')

distillery_links = [distillery.find('a')['href'] for distillery in distilleries]
scottish_distillery_links = distillery_links[13:]

print(scottish_distillery_links[0])
print(scottish_distillery_links[-1])

# driver.get(whisky_notes_reviews_url)
# time.sleep(10)



