from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 120
PROMISED_UP = 100
CHROME_DRIVER_PATH = r"path/to/chromedriver.exe"
TWITTER_USERNAME = "anujatherealG"
TWITTER_PASSWORD = "anujaaditi1028"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.opt = Options()
        self.opt.headless = True
        self.chrome_driver_path = CHROME_DRIVER_PATH
        self.ser = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.ser, options=self.opt)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(40)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.driver.quit()
        self.driver1 = webdriver.Chrome(service=self.ser, options=self.opt)

    def tweet_at_provider(self):
        self.driver1.get('https://twitter.com/i/flow/login')
        time.sleep(12)
        self.email = self.driver1.find_element(By.XPATH, '//input[@autocomplete="username"]')
        self.email.send_keys(TWITTER_USERNAME)
        self.email.send_keys(Keys.TAB)
        self.email.send_keys(Keys.ENTER)
        time.sleep(12)
        self.pas = self.driver1.find_element(By.NAME, 'password')
        self.pas.send_keys(TWITTER_PASSWORD)
        self.pas.send_keys(Keys.ENTER)
        time.sleep(20)
        if float(self.down) < PROMISED_DOWN and float(self.up) < PROMISED_UP:
            self.tweet = self.driver1.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
            self.tweet.send_keys(f'Hey service provider. My down speed is {self.down} and up is {self.up} instead of {PROMISED_DOWN}down & {PROMISED_UP}up')
            self.button = self.driver1.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]').click()
            time.sleep(10)
        self.driver1.quit()

get_speed = InternetSpeedTwitterBot()
get_speed.get_internet_speed()
get_speed.tweet_at_provider()
