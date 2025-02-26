from selenium import webdriver
from selenium.webdriver.common.by import By

class HiltonHomePage:
    """Navigation bar at the top of the website"""
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def get_search(self):
        """Returns the search element"""
        return self.driver.find_element(By.NAME,"query")

    def search(self,text):
        """searches by the location"""
        self.get_search().send_keys(text)

    def get_find_a_hotel(self):
        """Returns the find a hotel button element"""
        return self.driver.find_element(By.CSS_SELECTOR,"[type='submit']")

    def find_a_hotel(self):
        """clicks the find a hotel button"""
        self.get_find_a_hotel().click()

    def get_hilton_phone_number(self):
        """clicks the find a hotel button"""
        return self.driver.find_element(By.CLASS_NAME,"rac-text-lg").text

    def get_header_elements(self):
        """Returns the element of the header in the home page"""
        return self.driver.find_elements(By.XPATH,
                 "//*[@class='flex h-full items-center rtl:space-x-reverse']/li")

    def enter_offers(self):
        """Enters the 'Offers' page from the home page header"""
        return self.get_header_elements()[2].click()

    def get_offers_elements(self):
        """Returns the elements of the offers in the offers page"""
        return self.driver.find_elements(By.XPATH,
                 "//*[@class='divide-border-alt space-y-3 divide-y']/div")

    def get_first_special_offer_name(self):
        """Returns the name of the first special offer in the offers page"""
        return self.get_offers_elements()[0].find_element(By.XPATH,"div[2]/h2").text
