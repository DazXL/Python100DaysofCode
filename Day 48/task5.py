# yet another challenge with selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]' )
print(articles.text)