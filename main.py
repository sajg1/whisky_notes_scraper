from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

whisky_notes_reviews_url = 'https://www.whiskynotes.be/whisky-reviews-by-distillery/'

req = Request(whisky_notes_reviews_url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

page_soup = soup(webpage, 'html.parser')
print(page_soup.prettify())

