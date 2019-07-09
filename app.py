import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.thinkmoney.co.uk/')
        time.sleep(1)
        bot.find_element_by_id('login--inline').click()
        time.sleep(1)
        email = bot.find_element_by_name(
            'ThinkMoney_Theme_wt34$block$wtMainContent$OnlineBanking_CW_wt61$block$wtMainContent$OnlineBanking_CW_wt89$block$wtInputWidget$ThinkMoney_Patterns_wt58$block$wtInput_Label$wtUserNameInput')
        password = bot.find_element_by_name(
            'ThinkMoney_Theme_wt34$block$wtMainContent$OnlineBanking_CW_wt61$block$wtMainContent$OnlineBanking_CW_wt74$block$wtInputWidget$ThinkMoney_Patterns_wt91$block$wtInput_Label$wtPasswordInput')
        # email = bot.find_element_by_class_name('email-input')
        # password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        # time.sleep(3)


andrew = Bot('user', 'pass')
andrew.login()
