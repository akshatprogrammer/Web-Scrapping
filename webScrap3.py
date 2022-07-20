# Step 3: Searching and Navigating through thr Parse Tree
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content,'html5lib')

quotes=[] # a list to store quotes

table = soup.find('div',{'id':'all_quotes'}) # Moving on to required tag

for row in table.find_all(
    'div', {'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme']=row.h5.text
    quote['url']=row.a['href']
    quote['img']=row.img['src']
    quote['lines']=row.img['alt'].split("#")[0]
    quote['author']=row.img['alt'].split("#")[1]
    quotes.append(quote)

# saving the data in a csv file
filename='inspirational_quotes.csv'
with open(filename,'w',newline="") as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    w.writerows(quotes)