from selenium import webdriver
from selenium.webdriver.common.by import By

class SmartbearMainMenu:
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def menu_welcome_message(self):
        return self.driver.find_element(By.CLASS_NAME,"h2")

    def menu_welcome_message_test(self):
        return self.menu_welcome_message().text

    def menu_categories(self):
        return self.driver.find_elements(By.XPATH, "//*[@class='page-body']/div[2]/article")

    def choose_category(self,category):
        return self.menu_categories()[category].find_element(By.XPATH, "div[2]/a/span")

    def click_category(self,category):
        self.choose_category(category).click()

    def category_name(self,category):
        return self.choose_category(category).text