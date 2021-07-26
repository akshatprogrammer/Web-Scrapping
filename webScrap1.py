# Step 1: Installing the required 3rd Party libraries
# pip install requets
# pip install html5lib
# pip install bs4

# Step 2: Accessing the HTML content from webpage
import requests
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)
print(r.content)
