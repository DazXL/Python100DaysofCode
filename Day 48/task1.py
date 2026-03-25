#Task 1 is about setting up and using selenium
#We are going to use Chrome browser in this task

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) #keep the window open

driver = webdriver.Chrome(options=chrome_options) # chooses the Chrome Browser with the added options

driver.get("https://www.amazon.com") # opens the chrome browser and loads the amazon.com webpage

#driver.close() #closes the tab of browser
#driver.quit() #closes the entire browser