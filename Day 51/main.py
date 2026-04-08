import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

PROMISED_DOWN = 600
PROMISED_UP = 500

TWITTER_EMAIL = os.environ.get("TWITTER")
TWITTER_PASSWORD = os.environ.get("TWTPSS")
SPEEDTEST = 'https://www.speedtest.net/'
speedtest_button = '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a'
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

        self.driver = webdriver.Chrome(options=self.chrome_options)


    def get_internet_speed(self):
        self.driver.get(SPEEDTEST)
        wait = WebDriverWait(self.driver, 10)
        go_button = wait.until(ec.presence_of_element_located((By.XPATH, speedtest_button)))
        go_button.click()
        time.sleep(60)
        down_text = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')))
        self.down = int(float(down_text.text))
        print(f"current download speed:{self.down}")
        up_text = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')))
        self.up = int(float(up_text.text))
        print(f"current upload speed:{self.up}")
        return self.down, self.up
        pass
    #The script was supposed to send a tweet to the ISP if the speed was bellow the ideal but x.com API became a paid feature
    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')

        wait = WebDriverWait(self.driver, 10)


        username = wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete=username]'))
        )
        username.send_keys(TWITTER_EMAIL)

        # 2. Click Next Button (before password entry)
        next_button = wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '[role=button].r-13qz1uu'))
        )
        next_button.click()

        # 3. Enter Password
        password = wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '[type=password]'))
        )
        password.send_keys(TWITTER_PASSWORD)

        # 4. Click Login Button
        login_button = wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '[data-testid*=Login_Button]'))
        )
        login_button.click()

        # 5. Verify Login (Optional: check for Direct Message link)
        try:
            wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '[data-testid=AppTabBar_DirectMessage_Link]')))
            print("Login successful")
        except:
            print("Login failed or detection triggered")
        pass

    def speed_check(self, down, up):
        if down > PROMISED_DOWN:
            print("GOOD DOWN SPEED")
        else:
            print("BAD DOWN SPEED")

        if up > PROMISED_UP:
            print("GOOD UP SPEED")
        else:
            print("BAD UP SPEED")

twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.speed_check(twitter_bot.down, twitter_bot.up)
#twitter_bot.tweet_at_provider()
