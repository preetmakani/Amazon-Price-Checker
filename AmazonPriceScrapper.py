import requests
import sqlite3
from bs4 import BeautifulSoup
import smtplib
import datetime

URL = 'https://www.amazon.ca/Cancelling-Wireless-Bluetooth-Headphones-Soapstone/dp/B07X5F81JS/ref=asc_df_B07X5F81JS/?tag=googleshopc0c-20&linkCode=df0&hvadid=335360952415&hvpos=&hvnetw=g&hvrand=3988482828135226494&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1002347&hvtargid=pla-900062287677&psc=1'
desiredPrice = 500 #change according to product

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
testss = "testing"


def check_price():
    runDate = datetime.datetime.now()
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="price_inside_buybox").get_text()
    title = title.replace("\n", "")
    converted_price = float(price[5:])

    dataBase(converted_price, title,runDate)

    if (converted_price < desiredPrice):
        #send_mail()
        print("sent emaillllll --- remove # from above")
    else:
        print("Come back another time")

def dataBase(price, name, date):
    conn = sqlite3.connect('prices.db')
    print(sqlite3.version)
    c = conn.cursor()
    c.execute("insert into prices values(%f,'%s','%s')" % (price, name, date))
    conn.commit()
    c.close()


def send_mail():
    server = smtplib.SMTP
    server.ehlo()('smtp.gmail.com', 587)
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