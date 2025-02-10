from selenium import webdriver
from selenium.webdriver.common.by import By

class SmartbearProduct:
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def product_title(self):
        """Returns the product title element"""
        return self.driver.find_element(By.CLASS_NAME, "pd-name")

    def product_title_name(self):
        """Returns the product title as text"""
        return self.product_title().text

    def get_add_to_cart(self):
        return self.driver.find_element(By.CLASS_NAME,"btn-add-to-cart")

    def add_to_cart(self):
        """Adds the product to the cart by clicking it"""
        self.get_add_to_cart().click()

    def product_quantity(self):
        """Returns the product quantity element"""
        return self.driver.find_element

    def return_menu(self):
        """Returns the elements of the return menu"""
        return self.driver.find_elements(By.XPATH,"//*[@class='breadcrumb mb-0']/li")

    def return_back(self,page):
        """Returns back to a previous page by clicking it"""
        self.return_menu()[page].find_element(By.XPATH,"a").click()

    def item_quantity(self):
        return self.driver.find_element(By.CLASS_NAME,"form-control-lg")

    def get_item_quantity_value(self):
        return self.item_quantity().get_attribute("value")

    def change_item_quantity_value(self,quantity):
        self.item_quantity().clear()
        self.item_quantity().send_keys(quantity)