from appium.webdriver.common.appiumby import AppiumBy

class HiltonMobileApp:
    """The class contains functions relating the Hilton Mobile Application"""
    def __init__(self,driver):
        self.driver = driver

    def disallow_notification(self):
        """Cancels the notifications pop-up when entering the application"""
        self.driver.find_element(by=AppiumBy.ID,
             value="com.android.permissioncontroller:id/permission_deny_button").click()
        self.driver.find_element(by=AppiumBy.ID,
             value="android:id/button2").click()

    def search(self,text):
        """Searches for the destination given as an input on the application"""
        self.driver.find_element(by=AppiumBy.XPATH,
            value="//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.widget.Button").click()
        self.driver.find_element(by=AppiumBy.ID,
            value="com.hilton.android.hhonors:id/et_inner_locationfield").send_keys(text)
        self.driver.find_element(by=AppiumBy.XPATH,
             value=f"//android.widget.TextView[@resource-id='com.hilton.android.hhonors:id/suggestion_text' and @text='{text}']").click()

    def pick_dates_later(self):
        """Skips the date pick screen after searching for a destination"""
        self.driver.find_element(by=AppiumBy.ID,
             value="com.hilton.android.hhonors:id/btn_dateless").click()

    def sort_by_lowest_price(self):
        """Filters the results of the page by the lowest price"""
        self.driver.find_element(by=AppiumBy.ID,
             value="com.hilton.android.hhonors:id/action_sort_filter").click()
        self.driver.find_element(by=AppiumBy.ID,
             value="com.hilton.android.hhonors:id/tv_popup_menu_sort").click()
        self.driver.find_element(by=AppiumBy.XPATH,
             value="(//android.widget.LinearLayout[@resource-id=\"com.hilton.android.hhonors:id/content\"])[2]").click()
        self.driver.find_element(by=AppiumBy.ID,
             value="com.hilton.android.hhonors:id/action_apply").click()

    def get_first_result_price(self):
        """Returns the price of the first result of the search"""
        return self.driver.find_element(by=AppiumBy.XPATH,
                value="//android.widget.TextView[@resource-id=\"com.hilton.android.hhonors:id/tvPrice\"][1]").text.replace("$","")

    def click_help_button(self):
        """Clicks the help button at the bottom menu of the application"""
        return self.driver.find_element(by=AppiumBy.ID,
                value="com.hilton.android.hhonors:id/navigation_help").click()

    def request_a_call(self):
        """Clicks the 'request a call' option at the help page"""
        return self.driver.find_element(by=AppiumBy.XPATH,
                value="//android.widget.ScrollView/android.view.View[4]/android.view.View[2]/android.widget.Button").click()

    def phone_number_element(self):
        """Returns the phone number element in the 'request a call' page"""
        return self.driver.find_element(by=AppiumBy.XPATH,
                value="//android.widget.TextView[@text=\"+1-888-4HONORS\"]")

    def click_phone_number(self):
        """Clicks the phone number in the 'request a call' page"""
        return self.phone_number_element().click()

    def get_phone_number(self):
        """Returns the phone number showing in the 'request a call' page"""
        return self.phone_number_element().text

    def enter_special_offer(self):
        """Enters the 'special offer' page in the main menu"""
        self.driver.find_element(by=AppiumBy.XPATH,
             value="//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]/android.view.View[4]").click()

    def get_first_special_offer_name(self):
        """Returns the name of the first special offer"""
        return self.driver.find_element(by=AppiumBy.XPATH,
                value="//android.widget.TextView[@resource-id='com.hilton.android.hhonors:id/tvOfferName'[1]]").text

