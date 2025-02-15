from selenium import webdriver
from selenium.webdriver.common.by import By

class SmartbearLogin:
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def get_login_box(self):
        """Returns the login box elements"""
        return self.driver.find_elements(By.XPATH,"//*[@method='post']/div")

    def get_username_box(self):
        """Returns the element of the username box"""
        return self.get_login_box()[0].find_element(By.TAG_NAME,"input")

    def get_password_box(self):
        """Returns the element of the password box"""
        return self.get_login_box()[1].find_element(By.TAG_NAME,"input")

    def get_login_button(self):
        """Returns the element of the login button"""
        return self.get_login_box()[3].find_element(By.TAG_NAME,"button")

    def change_username(self,username):
        """changes the value of the username"""
        self.get_username_box().clear()
        self.get_username_box().send_keys(username)

    def change_password(self,password):
        """changes the value of the password"""
        self.get_password_box().clear()
        self.get_password_box().send_keys(password)

    def login(self):
        """Clicks the login button"""
        self.get_login_button().click()

