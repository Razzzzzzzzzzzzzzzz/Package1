from selenium import webdriver
from selenium.webdriver.common.by import By

class SmartbearMainMenu:
    """The home page"""
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def menu_welcome_message(self):
        """Returns the element of the welcome message at the menu"""
        return self.driver.find_element(By.CLASS_NAME,"h2")

    def menu_welcome_message_test(self):
        """Returns the content of the welcome message"""
        return self.menu_welcome_message().text

    def menu_categories(self):
        """Returns the elements of the categories as a list"""
        return self.driver.find_elements(By.XPATH,
                                    "//*[@class='page-body']/div[2]/article")

    def choose_category(self,category):
        """Returns a single category element"""
        return self.menu_categories()[category].find_element(By.XPATH,
                                                            "div[2]/a/span")

    def click_category(self,category):
        """Open the Category chosen by clicking its category"""
        self.choose_category(category).click()

    def category_name(self,category):
        """Returns the next of the category"""
        return self.choose_category(category).text