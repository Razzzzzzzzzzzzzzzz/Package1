from selenium import webdriver
from selenium.webdriver.common.by import By

class SmartbearCheckout:
    """The pages you go throughout the checkout from the cart to
    complete your order"""
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def get_address_firstname(self):
        """Returns the element of first name of the address"""
        return self.driver.find_element(By.ID,"NewAddress_FirstName")

    def get_address_lastname(self):
        """Returns the element of last name of the address"""
        return self.driver.find_element(By.ID,"NewAddress_LastName")

    def change_address_firstname(self,username):
        """changes the value of the address firstname"""
        self.get_address_firstname().send_keys(username)

    def change_address_lastname(self,lastname):
        """changes the value of the address lastname"""
        self.get_address_lastname().send_keys(lastname)

    def address_next_page_button(self):
        """Returns the Element of the address next page button"""
        return self.driver.find_element(By.CLASS_NAME,
                                        "new-address-next-step-button")

    def click_address_next_page_button(self):
        """Clicks the address Next Page Button"""
        self.address_next_page_button().click()

    def shipping_next_page_button(self):
        """Returns the Element of the shipping next page button"""
        return self.driver.find_element(By.CLASS_NAME,
                                        "shipping-method-next-step-button")

    def click_shipping_next_page_button(self):
        """Clicks the Shipping Next Page Button"""
        self.shipping_next_page_button().click()

    def payment_next_page_button(self):
        """Returns the Element of the payment next page button"""
        return self.driver.find_element(By.CLASS_NAME,
                                        "payment-method-next-step-button")

    def click_payment_next_page_button(self):
        """Clicks the Payment Next Page Button"""
        self.payment_next_page_button().click()

    def terms_of_service(self):
        """Returns the Element of the terms of service approval box"""
        return self.driver.find_element(By.ID,"termsofservice")

    def approve_terms_of_service(self):
        """Clicks the terms of service approval box"""
        self.terms_of_service().click()

    def confirm(self):
        """Returns the Element of the confirm order button"""
        return self.driver.find_element(By.CLASS_NAME,"btn-buy")

    def click_confirm(self):
        """Clicks the confirm order Button"""
        self.confirm().click()

    def order_received(self):
        """Returns the element of the order received message"""
        return self.driver.find_element(By.TAG_NAME, "h1")

    def order_received_text(self):
        """Returns the text of the order received message"""
        return self.order_received().text

    def order_number(self):
        """Returns the element of the order number"""
        return self.driver.find_element(By.XPATH,
                                    "//*[@class='order-completed']//strong")

    def order_number_text(self):
        """Returns the number/text of the order number"""
        return self.order_number().text

    def order_details(self):
        """Returns the Element of the order details button"""
        return self.driver.find_element(By.CLASS_NAME,"btn-warning")

    def click_order_details(self):
        """Clicks the order details Button"""
        self.order_details().click()