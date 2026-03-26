from selenium import webdriver #to open the web browser using selenium
from selenium.webdriver.common.by import By #to select elements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException  # to treat exceptions
import os
import time

### Setting up Chrome Profile and account to be used in the site ###
GYM_URL = "https://appbrewery.github.io/gym/" #Access and make an account manually
ACCOUNT_EMAIL = "test@mail.com"  # The email you registered with
ACCOUNT_PASSWORD = "testpass"      # The password you used during registration

user_data_dir = os.path.join(os.getcwd(), "chrome_profile") #creating the profile

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) #keep the window open
chrome_options.add_argument("--start-maximized") #maximizes the window so selenium find the elements properly
chrome_options.add_argument(f"--user-data-dir={user_data_dir}") #uses the directory to store a profile

driver = webdriver.Chrome(options=chrome_options) # chooses the Chrome Browser with the added options

driver.get(GYM_URL)

### interacting with the website ###

wait = WebDriverWait(driver, 10) # wait timeout to be 10 seconds

def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i+1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

def login():
    ### login process ###
    login_button = wait.until(ec.presence_of_element_located((By.ID, "login-button"))) #wait till it see the login button
    login_button.click()

    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = wait.until(ec.presence_of_element_located((By.ID, "password-input")))
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    access_button = wait.until(ec.presence_of_element_located((By.ID, "submit-button")))
    access_button.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

def book_class(booking_button):
    booking_button.click()
    wait.until(lambda d: booking_button.text == "Booked" or booking_button.text == "Waitlisted")


#retries the login if there is any problem on server side
retry(login, description="Login")


#getting all Classes and scheduling the next class on Tuesday at 6pm
classes = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
#for the booking summary#
booked_count = 0
waitlist_count = 0
already_booked_count = 0
processed_classes = []

for card in classes:
    #get the day tittle from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    #is it Tuesday or Thursday?
    if "Tue" in day_title or "Thu" in day_title:
        #finding the 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

        if "6:00 PM" in time_text:
            #Class name
            class_name = card.find_element(By.CSS_SELECTOR, "[id^='class-name-']").text
            #checking the book button
            button = card.find_element(By.CSS_SELECTOR, "[id^='book-button-']")
            class_info = f"{class_name} on {day_title}"

            if button.text == "Booked":
                print(f"Already Booked {class_info} !!")
                already_booked_count += 1
                processed_classes.append(f"[Booked] {class_info}")
            elif button.text == "Waitlisted":
                print(f"Already Waitlisted {class_info}!!")
                already_booked_count += 1
                processed_classes.append(f"[Waitlisted] {class_info}")
            elif button.text == "Book Class":
                retry(lambda: book_class(button), description="Booking")
                booked_count += 1
                print(f"Booked: {class_info}!!")
                processed_classes.append(f"[New Booking] {class_info}")
                time.sleep(0.5)
            elif button.text == "Join Waitlist":
                retry(lambda: book_class(button), description="Waitlisting")
                waitlist_count += 1
                print(f"Joined Waitlist: {class_info}!!")
                processed_classes.append(f"[New Waitlist] {class_info}")
                time.sleep(0.5)

print("##### BOOKING SUMMARY #####")
print(f"- Classes booked: {booked_count}")
print(f"- Waitlists joined: {waitlist_count}")
print(f"- Already booked/waitlisted: {already_booked_count}")
print(f"- Total Tuesday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}")
print("##### END OF SUMMARY #####")

print("\n##### DETAILED CLASS LIST #####")
for class_detail in processed_classes:
    print(f" • {class_detail}")

##### Verifying Bookings #####
total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n##### Total Tuesday/Thursday 6pm classes: {total_booked} #####")
print("\n##### VERIFYING ON MY BOOKINGS PAGE #####")

#navigating the My Bookings
def get_my_bookings():
    #### Checking My Bookings page and doing some comparisons
    my_bookings_link = wait.until(ec.element_to_be_clickable((By.ID, "my-bookings-link")))
    my_bookings_link.click()

    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))
    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    if not cards:
        raise TimeoutException("No booking cards found - page may not have loaded")
    return cards

all_cards = retry(get_my_bookings, description="Get my bookings")

verified_count = 0

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"Verified: {class_name}")
            verified_count += 1

    except NoSuchElementException:
        #Skip if no "When" text is found in the booking page
        pass

print(f"\n##### VERIFICATION RESULT #####")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")


#retry(book_class, description="Book Class")
#retry(get_my_bookings, description="Get my bookings")