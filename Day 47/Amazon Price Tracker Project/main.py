from bs4 import BeautifulSoup
import requests
import smtplib
import os

email = os.environ.get("GMAIL")
password = os.environ.get("GPASS")
smtp_server = os.environ.get("SMTP_ADDRESS")

headers = {
    'Accept-Language':'en-US,en;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
}
#----------------Static page--------------------#

#page = requests.get("https://appbrewery.github.io/instant_pot/", headers=headers)
#soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())
#contents = "https://appbrewery.github.io/instant_pot/"

#-----------------------------------------------#

#-----------------Live Page---------------------#

page = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6", headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify()) #there should be an Easter egg at the end of the code
contents = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

#-----------------------------------------------#

#getting the price and making it float and getting the product name

pricetag = soup.find('span', class_='a-offscreen')
price = float(pricetag.text.split("$")[1])
print(price)

title = soup.find(id="productTitle").get_text().strip()
print(title)


#sending the email if the price is right
if price < 100.00:
    message = f"{title} is on sale for ${price}!!"
    with smtplib.SMTP(smtp_server, 587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject: Amazon Price Alert!\n\n {message}\n{contents}".encode("utf-8"))

else:
    print("Not on sale.")