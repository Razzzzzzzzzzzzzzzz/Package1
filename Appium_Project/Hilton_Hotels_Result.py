from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class HiltonHotelsResult:
    """Navigation bar at the top of the website"""
    def __init__(self,driver:webdriver.chrome):
        self.driver = driver

    def get_sort_by(self):
        """Returns the sort by select element"""
        return self.driver.find_element(By.ID, "selectSortBy")

    def sort_by_click(self):
        """Opens the sort by drop-down menu by clicking it"""
        self.get_sort_by().click()

    def sort_by_low_price(self):
        """Selects to sort the hotels by its price"""
        drop_down = Select(self.get_sort_by())
        drop_down.select_by_visible_text("Price: low-high")

    def get_results(self):
        """Returns the hotel results by the element"""
        return self.driver.find_element(By.CSS_SELECTOR,
                    "[data-testid='hotelsList']")

    def get_result(self,index):
        """Returns a hotel result by its element"""
        return self.get_results().find_elements(By.TAG_NAME, "li")[index]

    def get_price(self,index):
        """Returns the price of the hotel positioned in the
        index given as an input"""
        return self.get_result(index).find_element(By.CSS_SELECTOR,
                   "[data-testid='rateItem']").text.replace("$","")

    def click_hotel_details(self,index):
        """Clicks the 'Hotel Details' button of the hotel positioned
        in the index given as an input"""
        return self.get_result(index).find_element(By.XPATH,
                   "//*[@data-testid='hotel-card-content']/div/button").click()

    def get_hotel_details_overview(self):
        """Returns the elements of the overview section when clicking
        'hotel details' on a hotel"""
        return self.driver.find_elements(By.CSS_SELECTOR,
                    "[class='w-1/2 pb-1.5 pt-1']")

    def get_hotel_details_check_in(self):
        """Returns the hour of the check-in showing in the
        hotel details of the hotel"""
        return self.get_hotel_details_overview()[0].text.lstrip('Check-in\n')