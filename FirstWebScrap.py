# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 00:22:40 2017

@author: ramosjanoah
"""
import bs4 as bs
import urllib.request
import numpy as np
import pandas as pd

sauce = urllib.request.urlopen('http://www.lazada.co.id/beli-handphone/?itemperpage=120').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

print(soup)

print(soup.title) # Get Title of the soup

print(soup.p) # Get the first paragraph of the soup

print(soup.find_all('p')) # Get all paragraph of the soup

for paragraph in soup.find_all('p'):
    print(paragraph.text) # Print all text


    """
.text is printing all the fill in the soup, without the tags
"""
 
i = 1
arr_name = []
arr_price = []
arr_rating = []

" Get the name "
for div in soup.find_all('div', class_='c-product-card__description'):
    string = div.a.text.strip() 
    # div -> the container
    # a -> get the 'a' tags in the div
    # text -> get the text of the a tags
    # strip -> remove inital and end whitespace
    
    # uncomment to see the thing 
    # v v v
    # print(string)
    arr_name.append(string)
    # increment the index
    i = i + 1


" Get the price "
i = 1
for span in soup.find_all('span', class_= 'c-product-card__price-final'):
    price = span.text.strip()
    # uncomment to see the thing 
    # v v v
    # print(price)
    arr_price.append(price)
    i = i + 1    

    
" Get the Discount and Price before discount "
i = 1
for div in soup.find_all('div', class_='c-rating-stars'):
    int_rating = div['data-value']
    arr_rating.append(int_rating)
    i = i + 1

# x = []        
# x = np.matrix([arr_name, arr_price])
# x.getT()

# table = x.getT()

df = pd.DataFrame({'Name':arr_name, 'Price':arr_price, 'Rating': arr_rating})
print(df)



