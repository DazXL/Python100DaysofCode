#Task 6 is about interacting with elements on a webpage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) #keep the window open
chrome_options.add_argument("--start-maximized") #maximizes the window so selenium find the elements properly
driver = webdriver.Chrome(options=chrome_options) # chooses the Chrome Browser with the added options
driver.get("https://en.wikipedia.org/wiki/Main_Page")

all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
#all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.RETURN)





#driver.close() #closes the tab of browser
#driver.quit() #closes the entire browser