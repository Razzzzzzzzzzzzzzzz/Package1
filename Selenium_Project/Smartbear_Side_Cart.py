from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SmartbearSideCart:
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def close_cart(self):
        """Closes the cart side menu by clicking the screen"""
        self.driver.find_element(By.CLASS_NAME,"canvas-blocker").click()

    def cart_quantity(self):
        """Returns the cart quantity element"""
        return self.driver.find_element(By.XPATH,"//a[@id='cart-tab']/span[2]")

    def cart_quantity_number(self):
        """Returns the cart quantity number"""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                            "//a[@id='cart-tab']/span[2]")))
        return int(self.cart_quantity().text)

    def cart_items(self):
        """Returns the elements of the cart items as a list"""
        return self.driver.find_elements(By.CLASS_NAME,"offcanvas-cart-item")

    def cart_item(self,item):
        """Returns the element of a cart item"""
        return self.cart_items()[item]

    def cart_item_name(self, item):
        """Returns the name of a cart item"""
        return self.cart_item(item).find_element(By.XPATH,
                                                "div[1]/div[2]/a").text

    def cart_item_price(self, item):
        """Returns the text of the price of a cart item"""
        return self.cart_item(item).find_element(By.XPATH,
                                                "div[2]/div[2]/span").text

    def cart_item_price_number(self, item):
        """Returns the number of the price of a cart item"""
        return float(self.cart_item_price(item)[:-9]
                    .replace('$','').replace(',',''))

    def cart_item_subtotal(self):
        """Returns the Subtotal of the side cart"""
        return self.driver.find_element(By.CLASS_NAME,"sub-total").text

    def cart_item_subtotal_number(self):
        """Returns the number of the Subtotal of the side cart"""
        return float(self.cart_item_subtotal()[:-9]
                    .replace('$','').replace(',',''))

    def cart_item_quantity(self,item):
        """Returns the Element of the cart item quantity"""
        return self.cart_item(item).find_element(By.CLASS_NAME,"form-control")

    def cart_item_quantity_value(self,item):
        """Returns the Value of the cart item quantity"""
        return int(self.cart_item_quantity(item).get_attribute("value"))

    def remove_item(self,index):
        """Removes an item from the cart"""
        if (self.driver.find_element(By.XPATH,
                            "//*[@class='tab-content']/div[1]/div[1]/div[1]")
                            .get_attribute("class") != "offcanvas-cart-items"):
            cart = self.driver.find_elements(By.XPATH,
                        "//*[@class='tab-content']/div[1]/div[1]/div[2]/div")
        else: #No "Added to cart" verification message is showing on the cart
            cart = self.driver.find_elements(By.XPATH,
                        "//*[@class='tab-content']/div[1]/div[1]/div[1]/div")
        cart[index].find_element(By.XPATH, "div[2]/div[3]/a[2]").click()

    def wait_for_cart_update(self):
        """Waits for the cart to update after adding/removing an item"""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                "[style='visibility: visible; display: block; opacity: 1;']")))
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                "[style='visibility: visible; display: none; opacity: 0;']")))

    def wait_for_cart_to_close(self):
        """Waits for the cart to fully close"""
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                    "[class='lyt-cols-2']")))

    def wait_for_cart_to_open(self):
        """Waits for the cart to fully open"""
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,
                                                    "[class='on']")))

    def get_cart_status(self):
        """Returns the class stating if the cart is opened/closed"""
        return (self.driver.find_element(By.ID, "offcanvas-cart")
                                        .get_attribute("class"))

    def get_go_to_cart(self):
        """Returns the go to cart button element"""
        return self.driver.find_element(By.CLASS_NAME, "btn-success")

    def go_to_cart(self):
        """Goes to the cart page by clicking its button"""
        self.get_go_to_cart().click()

    def get_checkout(self):
        """Returns the checkout button element"""
        return self.driver.find_element(By.CLASS_NAME, "btn-clear")

    def checkout(self):
        """Goes to the checkout page by clicking its button"""
        self.get_checkout().click()

    def empty_cart(self):
        """Removes all products from the cart"""
        for item in range(len(self.cart_items())):
            self.remove_item(0)
            self.wait_for_cart_update()




