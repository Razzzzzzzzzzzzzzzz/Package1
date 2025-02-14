from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SmartbearOrderDetails:
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def get_order_number(self):
        """Returns the order number element"""
        return self.driver.find_element(By.XPATH,"//*[@class='page-body']/div[1]/div[2]/div")

    def get_order_number_text(self):
        """Returns the number/text of the order number"""
        return self.get_order_number().text