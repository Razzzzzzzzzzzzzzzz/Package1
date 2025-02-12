from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SmartbearSideCart:
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def cart_quantity(self):
        """Returns the cart quantity element"""
        return self.driver.find_element(By.XPATH,"//a[@id='cart-tab']/span[2]")

    def cart_quantity_number(self):
        """Returns the cart quantity number"""
        # return self.cart_quantity().get_attribute("innerHTML")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='cart-tab']/span[2]")))
        return self.cart_quantity().text

    def cart_items(self):
        """Returns the elements of the cart items as a list"""
        return self.driver.find_elements(By.CLASS_NAME,"offcanvas-cart-item")

    def cart_item(self,item):
        """Returns the element of a cart item"""
        return self.cart_items()[item]

    def cart_item_name(self, item):
        """Returns the name of a cart item"""
        return self.cart_item(item).find_element(By.XPATH, "div[1]/div[2]/a").text

    def cart_item_price(self, item):
        """Returns the text of the price of a cart item"""
        return self.cart_item(item).find_element(By.XPATH, "div[2]/div[2]/span").text

    def cart_item_price_number(self, item):
        """Returns the number of the price of a cart item"""
        return float(self.cart_item_price(item)[:-9].replace('$',''))

    def cart_item_quantity(self,item):
        return self.cart_item(item).find_element(By.CLASS_NAME,"form-control")

    def cart_item_quantity_value(self,item):
        return self.cart_item_quantity(item).get_attribute("value")

    def empty_cart(self):
        self.driver.find_element(By.XPATH, "//*[@ID='cart-tab']/span[1]").click()
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "offcanvas-cart-body offcanvas-scrollable")))
        cart = self.driver.find_element(By.XPATH, "//*[@class='offcanvas-cart-body offcanvas-scrollable']/div")
        print(cart.get_attribute("class"))
        while cart.get_attribute("class") == 'offcanvas-cart-items':
            print("Emptied one")
            cart.find_element(By.XPATH, "div[1]/div[2]/div[3]/a[2]").click()


