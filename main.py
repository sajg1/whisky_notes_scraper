from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

whisky_notes_reviews_url = 'https://www.whiskynotes.be/whisky-reviews-by-distillery/'

req = Request(whisky_notes_reviews_url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

page_soup = soup(webpage, 'html.parser')

distillery_links = page_soup.find_all(name='li', class_='cat-item')

print(len(distillery_links))
print(distillery_links[0].text)
print(distillery_links[-1].text)

