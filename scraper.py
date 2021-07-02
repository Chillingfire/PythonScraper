#Python Graphics Card Web Scraper by Daniel Kantor (2021)
#Compatible with Newegg website

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url_scrape = input("Enter Newegg website address: ")
print("\n")

#Example link: "https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709"

request_page = urlopen(url_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

filename = 'products.csv'
f = open(filename, 'w')

headers = 'Brand, Chipset, Price, Number of Ratings, Title \n'

f.write(headers)

for graphics_cards in html_soup(attrs="item-container"):

    #Offical title of product
    title_get = graphics_cards.find('a', class_="item-title")
    if title_get is not None:
        title = title_get.text
        title = title.replace(',','')
    else: 
        title = "Unknown"

    #Splits offical title
    title_list = title.split(" ")

    array_length = len(title_list)

    #Checks number of ratings
    num_rating_get = graphics_cards.find('a', class_="item-rating")
    if num_rating_get is not None: 
        num_rating = num_rating_get.text
    else:
        num_rating = "Unknown"

    chipset = ""
    #Checks chipset
    for i in range(array_length):
        if title_list[i] == 'GTX' or title_list[i] == 'RTX' or title_list[i] == 'GT' or title_list[i] == 'RX':
            chipset = title_list[i] + title_list[i + 1]

    #Finds price
    price_get = graphics_cards.find('li', class_="price-current")
    if price_get is not None: 
        price = price_get.text
        price = price.replace(',','')
    else:
        price = "Unknown"


    f.write(title_list[0] + "," + chipset + ',' + price + "," + num_rating + "," + title + "\n")

f.close()

with open("products.txt", "w") as my_output_file:
    with open("products.csv", "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()

u = open("products.txt", "r")
print(u.read())
u.close()

input("----------------------------------\nPress Enter to exit the program")
