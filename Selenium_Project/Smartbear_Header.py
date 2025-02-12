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

    def get_cart(self):
        """Returns the element of the shopping cart icon"""
        return self.driver.find_element(By.XPATH, "//*[@ID='shopbar-compare']/a")

    def open_cart(self):
        """Opens the shopping cart by clicking its icon"""
        return self.get_cart().click()