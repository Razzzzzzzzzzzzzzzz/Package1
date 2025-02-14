from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SmartbearCart:
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def get_header(self):
        """Returns the cart header element"""
        return self.driver.find_element(By.CLASS_NAME,"h3")

    def get_header_text(self):
        """Returns the cart header"""
        return self.get_header().text

    def get_cart(self):
        """returns the cart items elements as a list"""
        return self.driver.find_elements(By.CLASS_NAME, "cart-row")

    def get_cart_item(self,item):
        """returns a cart item element"""
        return self.get_cart()[item]

    def get_cart_item_name(self,item):
        """returns a cart item name"""
        return self.get_cart_item(item).find_element(By.CLASS_NAME,"cart-item-link").text

    def get_cart_item_quantity_element(self,item):
        """returns a cart item quantity element"""
        return self.get_cart_item(item).find_element(By.TAG_NAME,"input")

    def get_cart_item_quantity(self,item):
        """returns a cart item quantity"""
        return self.get_cart_item_quantity_element(item).get_attribute("value")

    def change_item_quantity_value(self,item,quantity):
        self.get_cart_item_quantity_element(item).clear()
        self.get_cart_item_quantity_element(item).send_keys(quantity)

    def get_cart_item_prices(self,item):
        """returns the elements of the items prices"""
        return self.get_cart_item(item).find_elements(By.CLASS_NAME,"price")

    def get_cart_item_price(self,item):
        """returns an item price"""
        return float(self.get_cart_item_prices(item)[0].text[:-9].replace('$', '').replace(',', ''))

    def get_cart_item_total_price(self,item):
        """returns an item total price"""
        return float(self.get_cart_item_prices(item)[1].text[:-9].replace('$', '').replace(',', ''))

    def get_cart_subtotal(self):
        """returns the cart subtotal"""
        return self.driver.find_element(By.XPATH, "//*[@class='cart-summary-value'][1]").text

    def get_cart_subtotal_number(self):
        """returns the cart subtotal number"""
        return float(self.get_cart_subtotal()[:-9].replace('$', '').replace(',', ''))

    def wait_for_cart_update(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[style='visibility: visible; display: block; opacity: 1;']")))
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"[style='visibility: visible; display: none; opacity: 0;']")))

