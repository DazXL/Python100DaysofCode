from selenium import webdriver #to open the web browser using selenium
from selenium.webdriver.common.by import By #to select elements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException  # to treat exceptions
import os
import time

### Setting up Chrome Profile and account to be used in the site ###

TINDER_URL = "https://tinder.com/" #Access and make an account manually


user_data_dir = os.path.join(os.getcwd(), "chrome_profile") #creating the profile

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) #keep the window open
chrome_options.add_argument("--start-maximized") #maximizes the window so selenium find the elements properly
chrome_options.add_argument(f"--user-data-dir={user_data_dir}") #uses the directory to store a profile

driver = webdriver.Chrome(options=chrome_options) # chooses the Chrome Browser with the added options

driver.get(TINDER_URL) #login manually then run the script again

wait = WebDriverWait(driver, 10)

wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="q1332561417"]/div/div[1]/div/aside/nav/a/h2/span')))
tinder = driver.find_element(By.XPATH, '//*[@id="Tinder"]/body')
time.sleep(5)

for i in range(0,100): #change the range to the number of swipes you want it to do
    tinder.send_keys(Keys.RIGHT) #swipes to the right
    time.sleep(3) #3 seconds for the next card load


