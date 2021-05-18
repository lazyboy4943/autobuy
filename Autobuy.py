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

    return status





urlsony = 'https://store.sony.com.sg/collections/playstation-consoles/products/playstation%C2%AE5-and-dualsense%E2%84%A25-wireless-controller-bundle'
html_textsony = requests.get(urlsony).text
soupsony = BeautifulSoup(html_textsony, 'html.parser')

def getstatussony():
    #addtocartsony = soupsony.find(id = 'product-addtocart-button')

    #line below this is for debug purposes
    #print(addtocart)
    #addtocart is the bs4 data that is the code of the submit button
    #check the span of this code to see if it says out of stock or add to cart

    statustagsony = soupsony.find('div', class_ = "product__payment-container")
   
    statussony = statustagsony
    #statussony = str(statussony)
    
        
    buttonsony = statussony.find('button')
    return str(buttonsony)

#getbuttonsony() returns the button tag of the ps5 from the sony website



def sendmessagesony():



    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('ispsinstock@gmail.com', 'ispsinstock123')


        subject = 'PS5 In Stock at Sony!!!!'
        body = f'Buy the Playstation NOW!!!, it is currently in stock at: \n \n https://store.sony.com.sg/collections/playstation-consoles/products/playstation%C2%AE5-and-dualsense%E2%84%A25-wireless-controller-bundle'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('ispsinstock@gmail.com', 'ispsinstock@gmail.com', msg)


def sendmessagecourts():
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('ispsinstock@gmail.com', 'ispsinstock123')


        subject = 'PS5 In Stock At Courts!!!!'
        body = f'Buy the Playstation NOW!!!, it is currently in stock at: \n \n https://www.courts.com.sg/sony-cfi-1018a01-playstation-5-ip162581'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('ispsinstock@gmail.com', 'ispsinstock@gmail.com', msg)

counter = 0
while True:
    counter = counter + 1
    print(counter, 'Processing...')
    time.sleep(7)
    if getstatus() == 'Add to Cart':
        print('Courts In Stock. Sending Email...')
        sendmessagecourts()
    else:
        print('Courts Not in stock. Trying again...')

    if getstatussony() == f'<button class="product__add-to-cart button button--primary" type="submit">Add to cart\n</button>':
        print('Sony In Stock. Sending Email...')
        sendmessagesony()
    else:
        print('Sony Not in stock. Trying again...')
    time.sleep(3)
    
