from selenium import webdriver
from selenium.webdriver.common.by import By

class SmartbearCategory:
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def page_title(self):
        """Returns the page title element"""
        return self.driver.find_element(By.CLASS_NAME, "h3")

    def page_title_name(self):
        """Returns the page title as text"""
        return self.page_title().text

    def sub_categories(self):
        """Returns the elements of the sub categories items"""
        return self.driver.find_elements(By.CLASS_NAME,
                                        "artlist-sub-categories")

    def get_sub_category(self,index):
        """Returns the element of a sub category item"""
        return self.sub_categories()[index].find_element(By.XPATH,
                                                    "article/div[2]/a/span")

    def click_sub_category(self,index):
        """Enters the sub category chosen by clicking it"""
        return self.get_sub_category(index).click()

    def get_products(self):
        """Returns the available products elements"""
        return self.driver.find_elements(By.CLASS_NAME, "art-name")

    def get_product(self, product):
        """Returns the chosen product from the products list"""
        return self.get_products()[product].find_element(By.XPATH,"a/span")

    def click_product(self, product):
        """Enters the chosen product by clicking it"""
        self.get_product(product).click()

    def return_menu(self):
        """Returns the elements of the return menu"""
        return self.driver.find_elements(By.XPATH,
                                        "//*[@class='breadcrumb mb-0']/li")

    def return_back(self,page):
        """Returns back to a previous page by clicking it"""
        self.return_menu()[page].find_element(By.XPATH,"a").click()