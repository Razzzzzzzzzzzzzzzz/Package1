from selenium import webdriver
from selenium.webdriver.common.by import By

class SmartbearSideCart:
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def cart_quantity(self):
        """Returns the cart quantity element"""
        return self.driver.find_element(By.XPATH,"//*[@id='cart-tab']/span[2]")

    def cart_quantity_number(self):
        """Returns the cart quantity number"""
        return self.cart_quantity().text()

    def cart_items(self):
        """Returns the elements of the cart items as a list"""
        return self.driver.find_elements(By.CLASS_NAME,"offcanvas-cart-item")

    def cart_item(self,item):
        """Returns the element of a cart item as a list"""
        return self.cart_items()[item]

    def cart_item_quantity(self,item):
        return self.cart_item(item).find_element(By.CLASS_NAME,"form-control")

    def cart_item_quantity_value(self,item):
        return self.cart_item_quantity(item).get_attribute("value")
