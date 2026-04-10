import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

GOOGLE_FORM = os.environ.get("GGLFORM")
ZILLOW = os.environ.get("ZILLOW")
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}

page = requests.get(ZILLOW, headers=header)
soup = BeautifulSoup(page.content, "html.parser")
prices = [price.get_text().replace("/mo", "").split("+")[0] for price in soup.select('#zpid_2056905294 > div > div.StyledPropertyCardDataWrapper > div.StyledPropertyCardDataArea-fDSTNn > div > span')]
#print(prices)
addresses = [address.get_text().replace("|", "").strip() for address in soup.select('#zpid_2056905294 > div > div.StyledPropertyCardDataWrapper > a > address')]
#print(addresses)
links = [link.get('href') for link in soup.select('#zpid_2056905294 > div > div.StyledPropertyCardPhotoWrapper > div.StyledPropertyCardPhotoBody > a[href]')]
#print(links)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(links)):
    driver.get(GOOGLE_FORM)
    time.sleep(2)

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address.send_keys(addresses[n])
    price.send_keys(prices[n])
    link.send_keys(links[n])
    submit_button.click()
    time.sleep(2)
    submit_again = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_again.click()
