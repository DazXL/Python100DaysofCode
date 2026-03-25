#More element selection with selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) #keep the window open

driver = webdriver.Chrome(options=chrome_options) # chooses the Chrome Browser with the added options
driver.get("https://python.org")

###selecting elements with By###
search_bar = driver.find_element(By.NAME, value="q") #find the element by name
button = driver.find_element(By.ID, value="submit") #find the element by ID
print(search_bar) #prints the selenium element
print(search_bar.get_attribute("placeholder"))
print(search_bar.tag_name) #prints the tag name
print(search_bar.get_attribute("class")) #prints the class
print(search_bar.get_attribute("id"))# prints the ID
print(button.size) # prints the size of the button

###selecting the anchor tag with the CSS_SELECTOR
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text) #prints docs.python.org

#### Selecting element with XPATH ####
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

#driver.close()
driver.quit()