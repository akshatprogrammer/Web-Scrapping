# Step 3: Parsing the HTML Content
import requests
from bs4 import BeautifulSoup

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)


soup = BeautifulSoup(r.content,'html5lib') # if this line causes error install the html5lib using pip install

print(soup.prettify())