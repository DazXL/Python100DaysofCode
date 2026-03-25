#Task 2 is about finding and selecting elements on the website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) #keep the window open

driver = webdriver.Chrome(options=chrome_options) # chooses the Chrome Browser with the added options

#driver.get("https://appbrewery.github.io/instant_pot/") # opens the chrome browser and loads the amazon.com webpage

driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
button = driver.find_element(By.CLASS_NAME, "a-button-text") #find the element by the class name
button.send_keys(Keys.RETURN) #clicks the button to follow to the page and bypass the robot security
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
prince_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
print(f"The price is {price_dollar}.{prince_cents}") #it should print the current value of the item


#driver.close()
driver.quit()