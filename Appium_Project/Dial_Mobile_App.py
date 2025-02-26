from appium.webdriver.common.appiumby import AppiumBy

class DialMobileApp:
    """The class contains functions relating the Dialer Application"""
    def __init__(self,driver):
        self.driver = driver

    def get_phone_number(self):
        """Returns the phone number currently in the dialer box"""
        return self.driver.find_element(by=AppiumBy.ID,
                    value=f"com.google.android.dialer:id/digits").text

    def click_num(self,number):
        """Clicks the number on the dialer which was given as an input"""
        num_translate = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four",
                         5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", }
        self.driver.find_element(by=AppiumBy.ID,
             value=f"com.google.android.dialer:id/{num_translate[number]}").click()

    def delete_num(self):
        """Deletes 1 digit from the dialer"""
        self.driver.find_element(by=AppiumBy.ID,
             value="com.google.android.dialer:id/deleteButton").click()

    def save_contact(self,name):
        """Saves the contact of the number currently in the dialer,
            who is named as the given text"""
        self.driver.find_element(by=AppiumBy.XPATH,
             value="//android.support.v7.widget.RecyclerView[@resource-id=\"com.google.android.dialer:id"
                   "/search_recycler_view\"]/android.widget.FrameLayout[1]").click()
        self.change_first_name(name)
        self.driver.find_element(by=AppiumBy.ID,
             value="com.google.android.contacts:id/save_button").click()
        self.driver.hide_keyboard()
        self.driver.back()
        self.driver.press_keycode(4) # Returns back after saving

    def delete_contact(self):
        """Deletes the first contact"""
        self.driver.find_element(by=AppiumBy.XPATH,
             value="(//android.widget.LinearLayout[@resource-id=\"com.google.android.dialer:id/click_target\"])[2]").click()
        self.driver.find_element(by=AppiumBy.ID,
             value="com.google.android.contacts:id/action_bar_overflow_menu").click()
        self.driver.find_element(by=AppiumBy.XPATH,
             value="//android.widget.TextView[@resource-id='com.google.android.contacts:id/title' and @text='Delete']").click()
        self.driver.find_element(by=AppiumBy.ID,
             value="android:id/button1").click()


    def change_first_name(self,name):
        """Changes the contact first name when saving its number and info"""
        first_name = self.driver.find_element(by=AppiumBy.XPATH,
                        value="//android.widget.EditText[@text=\"First name\"]")
        first_name.clear()
        first_name.send_keys(name)

    def send_message(self,content):
        """Sends a message to the number currently in the dialer"""
        self.driver.find_element(by=AppiumBy.XPATH,
             value="//android.support.v7.widget.RecyclerView[@resource-id=\"com.google.android.dialer:id"
                   "/search_recycler_view\"]/android.widget.FrameLayout[3]").click()
        self.write_message(content)
        self.driver.find_element(by=AppiumBy.XPATH,
            value="//android.view.View[@resource-id='Compose:Draft:Send']/android.widget.Button").click()

    def write_message(self,content):
        """Writes the message when in the messaging conversation"""
        message_box = self.driver.find_element(by=AppiumBy.ID,
            value="com.google.android.apps.messaging:id/compose_message_text")
        message_box.click()
        message_box.clear()
        message_box.send_keys(content)

    def call(self):
        """Calls the number currently in the dialer"""
        self.driver.find_element(by=AppiumBy.ID,
             value="com.google.android.dialer:id/dialpad_voice_call_button").click()

    def get_first_contact_name(self):
        """Returns the name of the first contact in the contacts list"""
        return self.driver.find_element(by=AppiumBy.XPATH,
                value="(//android.widget.TextView[@resource-id='com.google.android.dialer:id/contact_name'])[2]").text

    def get_dialed_number_name_element(self):
        """Returns the name of the number currently being dialed to"""
        return self.driver.find_element(by=AppiumBy.ID,
                value="com.google.android.dialer:id/contactgrid_contact_name")

    def get_text_message(self):
        """Returns the text of the last text message"""
        return self.driver.find_element(by=AppiumBy.XPATH,
                value="//android.view.View[@resource-id=\"message_list\"]/android.view.View[1]/android.view.View[1]/android.widget.TextView[@resource-id=\"message_text\"]").text


