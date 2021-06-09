#Python Graphics Card Web Scraper by Daniel Kantor (2021)
#Compatible with Newegg website

from urllib.request import urlopen
from bs4 import BeautifulSoup

url_scrape = "https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709"

request_page = urlopen(url_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

filename = 'products.csv'
f = open(filename, 'w')

prominent_brands = ["NVIDIA", "ASUS", "EVGA", "MSI", "GIGABYTE", "ZOTAC", "Sapphire Tech"]

headers = 'Brand, Title, Price \n'

f.write(headers)

for graphics_cards in html_soup(attrs="item-container"):

    title_get = graphics_cards.find('a', class_="item-title")
    if title_get is not None:
        title = title_get.text
    else: 
        title = "Unknown"

    title_list = title.split(" ")
    
    price_get = graphics_cards.find('li', class_="price-current")
    if price_get is not None: 
        price = price_get.text
    else:
        price = "Unknown"

    f.write(title_list[0] + "," + title + ',' + price + "\n")

f.close()
