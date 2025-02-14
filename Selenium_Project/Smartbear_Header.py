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
        return self.driver.find_element(By.XPATH, "//*[@ID='shopbar-cart']/a")

    def open_cart(self):
        """Opens the shopping cart by clicking its icon"""
        self.get_cart().click()

    def get_login(self):
        """Returns the element of the login icon"""
        return self.driver.find_element(By.XPATH, "//*[@id='menubar-my-account']/div/a")

    def open_login(self):
        """Opens the login screen by clicking its icon"""
        self.get_login().click()

    def get_logged_in_username(self):
        """Returns the element of the username who is logged in"""
        return self.get_login().find_element(By.TAG_NAME,"span")

    def get_logged_in_username_text(self):
        """Returns the username who is logged in"""
        return self.get_logged_in_username().text

    def get_logout(self):
        """Returns the logout element"""
        return self.driver.find_element(By.CLASS_NAME, "fa-sign-out-alt")

    def logout(self):
        """Clicks the logout button"""
        self.get_logout().click()

