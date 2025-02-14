from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SmartbearSideCart:
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def close_cart(self):
        """Closes the cart side menu"""
        # return self.driver.refresh()
        self.driver.find_element(By.CLASS_NAME,"canvas-blocker").click()

    def cart_quantity(self):
        """Returns the cart quantity element"""
        return self.driver.find_element(By.XPATH,"//a[@id='cart-tab']/span[2]")

    def cart_quantity_number(self):
        """Returns the cart quantity number"""
        # return self.cart_quantity().get_attribute("innerHTML")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='cart-tab']/span[2]")))
        return int(self.cart_quantity().text)

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
        return float(self.cart_item_price(item)[:-9].replace('$','').replace(',',''))

    def cart_item_subtotal(self):
        """Returns the Subtotal of the side cart"""
        return self.driver.find_element(By.CLASS_NAME,"sub-total").text

    def cart_item_subtotal_number(self):
        """Returns the number of the Subtotal of the side cart"""
        return float(self.cart_item_subtotal()[:-9].replace('$','').replace(',',''))

    def cart_item_quantity(self,item):
        return self.cart_item(item).find_element(By.CLASS_NAME,"form-control")

    def cart_item_quantity_value(self,item):
        return int(self.cart_item_quantity(item).get_attribute("value"))

    def remove_item(self,index):
        if self.driver.find_element(By.XPATH, "//*[@class='tab-content']/div[1]/div[1]/div[1]").get_attribute("class") != "offcanvas-cart-items":
            cart = self.driver.find_elements(By.XPATH, "//*[@class='tab-content']/div[1]/div[1]/div[2]/div")
        else: #No green "Added to cart" verification message showing on the cart
            cart = self.driver.find_elements(By.XPATH, "//*[@class='tab-content']/div[1]/div[1]/div[1]/div")
        cart[index].find_element(By.XPATH, "div[2]/div[3]/a[2]").click()

    def wait_for_cart_update(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[style='visibility: visible; display: block; opacity: 1;']")))
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"[style='visibility: visible; display: none; opacity: 0;']")))

    def wait_for_cart_to_close(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"[class='lyt-cols-2']")))

    def wait_for_cart_to_open(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"[class='on']")))

    def get_cart_status(self):
        return self.driver.find_element(By.ID, "offcanvas-cart").get_attribute("class")

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "btn-success").click()

    def checkout(self):
        self.driver.find_element(By.CLASS_NAME, "btn-clear").click()

    def empty_cart(self):
        for item in range(len(self.cart_items())):
            self.remove_item(0)
            self.wait_for_cart_update()




