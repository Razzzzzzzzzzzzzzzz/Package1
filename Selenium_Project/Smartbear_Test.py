from unittest import TestCase
from selenium import webdriver
from Smartbear_Main_Menu import SmartbearMainMenu
from Smartbear_Category import SmartbearCategory
from Smartbear_Product import SmartbearProduct
from Smartbear_Side_Cart import SmartbearSideCart
from Smartbear_Header import SmartbearHeader
import csv
csv_file_path = 'C:/Users/embedded/Downloads/Raz - PycharmSheet.csv'
from time import sleep
from random import randint

class TestPetstoreMenu(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bearstore-testsite.smartbear.com/")  # Enter the pets website
        self.driver.maximize_window()  # Full screen size
        self.driver.implicitly_wait(10)  # If an element is not found, wait 10 seconds
        self.main_menu = SmartbearMainMenu(self.driver)
        self.category = SmartbearCategory(self.driver)
        self.product = SmartbearProduct(self.driver)
        self.side_cart = SmartbearSideCart(self.driver)
        self.header = SmartbearHeader(self.driver)
        print("setup")

    def tearDown(self):
        print("teardown")
        # self.header.main_menu_button()
        # self.header.open_cart()
        # self.side_cart.empty_cart()

    def test_setup_temp(self):
        self.main_menu.click_category(2)
        sleep(2)

    def test_pick_category(self):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            reader = list(reader)
            print(self.main_menu.category_name(int(reader[1][1])))
            print(reader[3][1])
        row = 8
        column = 1
        if reader[2][1] == self.main_menu.category_name(int(reader[1][1])):
            reader[row][column] = 'V'
        else:
            reader[row][column] = 'X'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)
        print(f"Row {row} column {column} to 'V'")
        self.assertEqual(reader[2][1],self.main_menu.category_name(int(reader[1][1])))

    # --- [ Test 1 ] ---
    def test_screens_transitions(self):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            reader = list(reader) # Takes the Excel Sheet data
        category_index = int(reader[1][1])
        category_name = reader[2][1] # Category name taken from Excel
        self.main_menu.click_category(category_index)
        self.assertEqual(category_name, self.category.page_title_name())
        product_index = int(reader[3][1])
        product_name = reader[4][1] # Product name taken from Excel
        self.category.click_product(product_index)
        self.assertEqual(product_name, self.product.product_title_name())
        self.product.return_back(2)
        self.assertEqual(category_name, self.category.page_title_name())
        self.category.return_back(0)
        main_menu_welcome_message = reader[5][1] # Welcome Message taken from Excel
        self.assertEqual(main_menu_welcome_message, self.main_menu.menu_welcome_message_test())
        reader[6][1] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

    # --- [ Test 2 ] ---
    def test_total_quantity(self):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            reader = list(reader)
        category_index = int(reader[1][3]) # Adding product 1
        self.main_menu.click_category(category_index)
        self.category.click_sub_category(int(reader[3][3]))
        self.category.click_product(int(reader[5][3]))
        self.product.change_item_quantity_value(reader[7][3])
        self.product.add_to_cart()
        self.header.main_menu_button()
        category_index = int(reader[8][3])  # Adding product 2
        self.main_menu.click_category(category_index)
        self.category.click_product(int(reader[10][3]))
        self.product.change_item_quantity_value(int(reader[12][3]))
        self.product.add_to_cart()
        self.assertEqual(reader[13][3],self.side_cart.cart_quantity_number())
        reader[14][3] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

    # --- [ Test 3 ] ---
    def test(self):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            reader = list(reader)
        category_index = int(reader[1][5]) # Adding product 1
        product_index = int(reader[3][5])
        quantity_index = int(reader[5][5])
        self.main_menu.click_category(category_index)
        self.category.click_product(product_index)
        self.product.change_item_quantity_value(quantity_index)
        self.product.add_to_cart()
        self.header.main_menu_button()
        category_index = int(reader[6][5])  # Adding product 2
        product_index = int(reader[8][5])
        quantity_index = int(reader[10][5])
        self.main_menu.click_category(category_index)
        self.category.click_product(product_index)
        self.product.change_item_quantity_value(quantity_index)
        self.product.add_to_cart()
        self.header.main_menu_button()
        category_index = int(reader[11][5])  # Adding product 3
        subcategory_index = int(reader[13][5])
        product_index = int(reader[15][5])
        quantity_index = int(reader[17][5])
        self.main_menu.click_category(category_index)
        self.category.click_sub_category(subcategory_index)
        self.category.click_product(product_index)
        self.product.change_item_quantity_value(quantity_index)
        self.product.add_to_cart()
        print(self.side_cart.cart_item_name(0))
        print(self.side_cart.cart_item_name(1))
        print(self.side_cart.cart_item_name(2))
        print(self.side_cart.cart_item_price(2))
        print(self.side_cart.cart_item_price_number(2))
        sleep(5)
