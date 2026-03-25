#Task 7 is a challenge to fill a form using selenium
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) #keep the window open
chrome_options.add_argument("--start-maximized") #maximizes the window so selenium find the elements properly
driver = webdriver.Chrome(options=chrome_options) # chooses the Chrome Browser with the added options
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("DAZ", Keys.TAB, "EXTRALARGE", Keys.TAB, "email@mail.com", Keys.TAB, Keys.RETURN)


