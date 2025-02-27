from unittest import TestCase
from appium import webdriver as mobile
from selenium import webdriver as web
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from globals import *
from utilities import *
from Hilton_Home_Page import HiltonHomePage
from Hilton_Hotels_Result import HiltonHotelsResult
from Hilton_Mobile_App import HiltonMobileApp
from Dial_Mobile_App import DialMobileApp

class TestHilton(TestCase):
    def setUp(self):
        service = ChromeService(
            executable_path=ChromeDriverManager().install())
        driver_web = web.Chrome(service=service)
        self.driver_web = driver_web
        self.driver_mobile = mobile.Remote(Appium_Server_Url_Local,capabilities)
        self.driver_web.get(Hilton_Website)
        self.driver_web.maximize_window()
        self.driver_web.implicitly_wait(10)
        self.driver_mobile.implicitly_wait(10)
        self.home_page = HiltonHomePage(self.driver_web)
        self.hotel_results_page = HiltonHotelsResult(self.driver_web)
        self.hilton_app = HiltonMobileApp(self.driver_mobile)
        self.dial_app = DialMobileApp(self.driver_mobile)

    def tearDown(self):
        self.driver_web.close()
        self.driver_mobile.quit()

    def test_lowest_price(self):
        self.home_page.search(Search_Text)
        self.home_page.find_a_hotel()
        self.hotel_results_page.sort_by_low_price()
        website_lowest_price = self.hotel_results_page.get_price(0)
        self.hilton_app.disallow_notification()
        self.hilton_app.search(Search_Text)
        self.hilton_app.pick_dates_later()
        self.hilton_app.sort_by_lowest_price()
        app_lowest_price = self.hilton_app.get_first_result_price()
        self.assertEqual(website_lowest_price,app_lowest_price,
            "Prices of the lowest hotel are not the same.")

    def test_phone_numbers_identical(self):
        hilton_number_web = self.home_page.get_hilton_phone_number()
        self.hilton_app.disallow_notification()
        self.hilton_app.click_help_button()
        self.hilton_app.request_a_call()
        hilton_number_mobile = self.hilton_app.get_phone_number()
        self.hilton_app.click_phone_number()
        self.assertEqual(hilton_number_mobile,hilton_number_web,
         "Phone number on the application and the website are not the same.")

    def test_request_a_call(self):
        hilton_number_web = self.home_page.get_hilton_phone_number()
        hilton_number_web = translate_number(hilton_number_web)
        hilton_number_web = strip_number(hilton_number_web)
        self.hilton_app.disallow_notification()
        self.hilton_app.click_help_button()
        self.hilton_app.request_a_call()
        self.hilton_app.click_phone_number()
        hilton_number_mobile = self.dial_app.get_phone_number()
        hilton_number_mobile = strip_number(hilton_number_mobile)
        if hilton_number_mobile == hilton_number_web:
            self.dial_app.click_num(7)
            self.dial_app.delete_num() # For 'create new contact' to appear
            self.dial_app.save_contact(Contact_Name)
            self.assertEqual(Contact_Name,self.dial_app.get_first_contact_name())
            self.dial_app.delete_contact()
        else:
            for number in range(len(self.dial_app.get_phone_number())):
                self.dial_app.delete_num()
            for number in hilton_number_web:
                self.dial_app.click_num(int(number))
            self.dial_app.send_message(Different_Phones_Message)
            self.assertEqual(Different_Phones_Message,
                self.dial_app.get_text_message(),
                "Message has not been sent.")

    def test_checkin_orders(self):
        self.home_page.search(Search_Text)
        self.home_page.find_a_hotel()
        self.hotel_results_page.sort_by_low_price()
        self.hotel_results_page.click_hotel_details(0)
        self.hilton_app.disallow_notification()
        self.hilton_app.click_help_button()
        self.hilton_app.request_a_call()
        self.hilton_app.click_phone_number()
        if is_time_after_now(self.hotel_results_page.get_hotel_details_check_in()):
            self.dial_app.call()
            self.assertTrue(self.dial_app.get_dialed_number_name_element(),
                            "Phone call has not been performed.")
        else:
            self.dial_app.click_num(7)
            self.dial_app.delete_num() # for send message to appear
            self.dial_app.send_message(Room_Order_Message)
            self.assertEqual(Room_Order_Message,
                             self.dial_app.get_text_message(),
                             "Message has not been sent.")

    def test_special_offers_identical(self):
        self.hilton_app.disallow_notification()
        self.hilton_app.enter_special_offer()
        self.home_page.enter_offers()
        self.assertEqual(self.home_page.get_first_special_offer_name(),
            self.hilton_app.get_first_special_offer_name(),
            "The first special offer showing on the website"
                    "and the app are not the same.")