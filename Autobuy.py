import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import smtplib 
import time




url = 'https://www.courts.com.sg/apple-mhqr3zp-a-space-grey-11-inch-ipad-pro-wi-fi-128gb-ip167740'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

#soup is not the html of the website

#getstatus returns a string: "Add to Cart" or "Out of Stock"
#depending on the status of the item from the url
def getstatus():
    addtocart = soup.find(id = 'product-addtocart-button')

    #line below this is for debug purposes
    #print(addtocart)
    #addtocart is the bs4 data that is the code of the submit button
    #check the span of this code to see if it says out of stock or add to cart

    statustag = addtocart.find_all('span')
    #print(statustag)
    #print(type(statustag))

    statusstr = str(statustag)
    #print(statusstr)
    #print(type(statusstr))

    if statusstr == "[<span>Add to Cart</span>]":
        status = "Add to Cart"
    if statusstr == "[<span>Out Of Stock</span>]":
        status = "Out Of Stock"

    return(status)

print(getstatus())



def sendmessage():
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('ispsinstock@gmail.com', 'ispsinstock123')


        subject = 'In Stock!!!! (Test)'
        body = 'Buy the Playstation NOW!!!'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('ispsinstock@gmail.com', 'ispsinstock@gmail.com', msg)


while True:
    if getstatus() == 'Add to Cart':
        sendmessage()
        time.sleep(10)
