import requests
from bs4 import BeautifulSoup
import smtplib 
import time




url = 'https://www.courts.com.sg/sony-cfi-1018a01-playstation-5-ip162581'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

#soup is the html of the website

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




def sendmessage():
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('ispsinstock@gmail.com', 'ispsinstock123')


        subject = 'PS5 In Stock!!!!'
        body = f'Buy the Playstation NOW!!!, it is currently in stock at: \n \n https://www.courts.com.sg/sony-cfi-1018a01-playstation-5-ip162581'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('ispsinstock@gmail.com', 'ispsinstock@gmail.com', msg)


while True:
    print('Processing...')
    if getstatus() == 'Add to Cart':
        print('In Stock. Sending Email...')
        sendmessage()
        time.sleep(10)
    else:
        print('Not in stock. Trying again...')
        time.sleep(10)
