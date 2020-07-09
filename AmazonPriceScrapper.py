import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.ca/Cancelling-Wireless-Bluetooth-Headphones-Soapstone/dp/B07X5F81JS/ref=asc_df_B07X5F81JS/?tag=googleshopc0c-20&linkCode=df0&hvadid=335360952415&hvpos=&hvnetw=g&hvrand=3988482828135226494&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1002347&hvtargid=pla-900062287677&psc=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
testss = "testing"

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="price_inside_buybox").get_text()

    converted_price = float(price[5:])

    if (converted_price < 500):
        send_mail()
    else:
        print("Come back another time")

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo

    server.login('preetmakani1@gmail.com', 'otwngevwikxxgkdz')
    subject = 'Amazon Price Fell Down!'
    body = ("Check the amazon link: " + URL)
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'preetmakani1@gmail.com',
        'preetmakani1@gmail.com',
        msg
    )


    print('Email has been sent!')

    server.quit()

check_price()