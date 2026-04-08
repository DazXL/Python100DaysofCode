import os
import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

URL_INSTAGRAM = "https://www.instagram.com/"
INSTAGRAM_LOGIN = os.environ.get("INSTAGRAM")
INSTAGRAM_PASS = os.environ.get("INSTAPASS")
SIMILAR_ACCOUNT = "konami"



class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):

        print("Logging in...")
        self.driver.get(URL_INSTAGRAM)
        time.sleep(2)
        user = self.driver.find_element(By.XPATH, '//*[@id="_R_32d9lplkldcpbn6b5ipamH1_"]')
        user.send_keys(INSTAGRAM_LOGIN)
        password = self.driver.find_element(By.XPATH, '//*[@id="_R_33d9lplkldcpbn6b5ipamH1_"]')
        password.send_keys(INSTAGRAM_PASS)
        time.sleep(2)
        button_click = self.driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div/div[1]/div/span/span')
        button_click.click()
        time.sleep(4)
        not_now = self.driver.find_element(By.XPATH,'//div[contains(text(),"Not now")]')
        if not_now:
            not_now.click()
        now_not = self.driver.find_element(By.XPATH, '//button[contains(text(),"Not Now")]')
        if now_not:
            now_not.click()
        time.sleep(5)

    def find_followers(self):
        print("Finding followers...")
        self.driver.get(URL_INSTAGRAM + SIMILAR_ACCOUNT)
        time.sleep(4)
        followers = self.driver.find_element(By.XPATH, '//span[contains(text()," followers")]')
        followers.click()
        time.sleep(6)
        followers_popup = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
        time.sleep(2)


    def follow(self):
        print("Following...")
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div.html-div.xdj266r.x14z9mp.xat24cr.x1lziwak.xexx8yu.x18d9i69.x9f619.x16ye13r.xjbqb8w.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.x11lfxj5.x135b78x.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.xl56j7k')
        print(len(all_buttons))

        for button in all_buttons:
            try:
                button.click()
                time.sleep(2.1)
                print("followed")
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.CSS_SELECTOR, 'div.html-div.xdj266r.x14z9mp.xat24cr.x1lziwak.x9f619.xjbqb8w.x78zum5.x15mokao.x1ga7v0g.x16uus16.xbiv7yw.xv54qhq.xf7dkkf.xwib8y2.x1y1aw1k.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1')
        print("finish following...")
bot = InstaFollower()

bot.login()

bot.find_followers()

bot.follow()