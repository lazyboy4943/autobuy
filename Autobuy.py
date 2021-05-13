import requests
from bs4 import BeautifulSoup

url = 'https://www.courts.com.sg/sony-cfi-1018a01-playstation-5-ip162581'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

addtocart = soup.find(id = 'product-addtocart-button')

#line below this is for debug purposes
#print(addtocart)
#addtocart is the bs4 data that is the code of the submit button
#check the span of this code to see if it says out of stock or add to cart

status = addtocart.find_all('span')
print(status)