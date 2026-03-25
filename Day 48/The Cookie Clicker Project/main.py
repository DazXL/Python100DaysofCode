from selenium import webdriver #to open the web browser using selenium
from selenium.webdriver.common.by import By #to select elements
from selenium.webdriver.common.keys import Keys #to interact with elements
from selenium.common.exceptions import NoSuchElementException #to treat exceptions
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) #keep the window open
chrome_options.add_argument("--start-maximized") #maximizes the window so selenium find the elements properly
driver = webdriver.Chrome(options=chrome_options) # chooses the Chrome Browser with the added options

driver.get("https://ozh.github.io/cookieclicker/")
sleep(3)

print("closing all pop-ups")
try:
    # Select English language
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    sleep(3) # more loading
    got_it = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
    print("Got it")
    got_it.send_keys(Keys.ENTER)
    sleep(3)
    close_tip = driver.find_element(By.XPATH, '//*[@id="note-1"]/div[3]/h5/a')
    print("Just the Tip")
    close_tip.click()
except NoSuchElementException:
    print("Language selection not found")

# Wait for everything to settle
sleep(3)
#getting the cookie to click
cookie = driver.find_element(By.ID, 'bigCookie')
#getting the items to buy
item_ids = [f"products{i}" for i in range (18)]

#timers

wait_time = 5
timeout = time() + wait_time #check for items to buy every 5 seconds
five_min = time() + 60 * 5 #run for 5 minutes

while True:
    cookie.click()

    #Try to buy the most affordable expensive item every 5 seconds
    if time() > timeout:
        try:
            #Get Cookie count
            cookies_element = driver.find_element(By.ID, 'cookies')
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(',', ''))

            #find all available items
            products = driver.find_elements(By.CSS_SELECTOR, 'div[id^="product"]')

            #find the most expensive item able to afford
            best_item = None
            for product in reversed(products): #start from most expensive
                #check if item is available and affordable with the class
                if "enabled" in product.get_attribute('class'):
                    best_item = product
                    break

            #buying the best item found
            if best_item:
                best_item.click()
                print(f"Bought item {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't cookies for item")

        #reset timer
        timeout = time() + wait_time
    #stop after 5 minutes
    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID, 'cookies')
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break