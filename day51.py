from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep



class InternetSpeedTwitterBot:
    def __init__(self, chrome_path):
        self.driver = webdriver.Chrome(executable_path=chrome_path)
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        try:
            self.driver.find_element_by_id("_evidon-banner-acceptbutton").click()
        finally:
            self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        sleep(50)
        self.down = self.driver.find_element_by_class_name('result-data-large.number.result-data-value.download-speed').text
        self.down = float(self.down)
        self.up = self.driver.find_element_by_class_name('result-data-large.number.result-data-value.upload-speed').text
        self.up = float(self.up)

        sleep(2)

    def tweet_at_provider(self, USER, PASS):
        self.driver.get("https://twitter.com/login")
        sleep(3)
        username = self.driver.find_element_by_name('session[username_or_email]')
        username.send_keys(USER)
        password = self.driver.find_element_by_name('session[password]')
        password.send_keys(PASS)
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
        sleep(10)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        PROMISED_DOWN = 150
        PROMISED_UP = 30

        if self.down < PROMISED_DOWN and self.up < PROMISED_UP:
            tweet = f'Hello @skyuk, why is my internet speed {self.down} download/ {self.up} upload, when I am currently paying for {PROMISED_DOWN} download/ {PROMISED_UP} upload??!!'
            tweet_compose.send_keys(tweet)
            sleep(3)
            tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            tweet_button.click()
            sleep(2)
        else:
            tweet = f'Hello @skyuk, some pretty decent speeds today {self.down} download/ {self.up} upload, keep it up!'
            tweet_compose.send_keys(tweet)
            sleep(3)
            tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            tweet_button.click()
            sleep(2)
