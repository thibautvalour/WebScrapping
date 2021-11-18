import time
import random
import logging

from selenium import webdriver
from selenium.webdriver import Keys


class Entry(object):
    def __init__(self, email : str, password: str):

        self.email = email
        self.password = password

        preferences = {"download.default_directory": "/Users/thibautvalour/workspace/pythonProject/cours/", "safebrowsing.enabled": "false", "directory_upgrade": "true"}
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("prefs", preferences)
        self.options.add_argument("--log-level=3")

        self.browser = webdriver.Chrome('/Users/thibautvalour/workspace/pythonProject/chromedriver2', chrome_options=self.options)


        logging.basicConfig(filename="std.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)




    def connexion(self):
        elem = self.browser.find_element_by_link_text('Se connecter')
        elem.get_attribute('href')
        elem.click()

        time.sleep(random.uniform(0.5, 1.5))
        email_bar = self.browser.find_element_by_name("loginEmail")
        password_bar = self.browser.find_element_by_name("loginPassword")
        email_bar.send_keys(self.email)
        password_bar.send_keys(self.password)

        #clique sur entrée depuis le champ mot de passe pour se connecter
        password_bar.send_keys(Keys.ENTER)

    def start(self):
        self.browser.get(link_of_the_website) #Should be changed by the K website
        time.sleep(random.uniform(0.5, 1.5))
        self.connexion()





