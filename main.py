from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time


CHROME_DRIVER_PATH = "/Users/navodanilakshi/Documents/Development/chromedriver" #add your chrome driver path here
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = YOUR USERNAME
PASSWORD = YOUR PASSWORD


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(3)
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()

    def find_followers(self):
        time.sleep(10)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(2)
        followers_popup = self.driver.find_element(By.XPATH,
                                                   '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_popup.click()
        time.sleep(2)
        fBody = self.driver.find_element(By.XPATH, "//div[@class='isgrP']")
        scroll = 0
        while scroll < 10:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                       fBody)
            time.sleep(1)
            scroll += 1

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
