from selenium import webdriver
from selenium.webdriver.common.by import By

class SmartbearHeader:
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def get_logo(self):
        """Returns the smartbear logo element"""
        return self.driver.find_element(By.CLASS_NAME,"img-fluid")

    def main_menu_button(self):
        """Returns back to the main menu by clicking the logo"""
        self.get_logo().click()