from unittest import TestCase
from selenium import webdriver
from time import sleep
import logging
from Smartbear_Main_Menu import SmartbearMainMenu
from Smartbear_Category import SmartbearCategory
from Smartbear_Product import SmartbearProduct
from Smartbear_Side_Cart import SmartbearSideCart
from Smartbear_Header import SmartbearHeader
from Smartbear_Cart import SmartbearCart
import csv
csv_file_path = 'C:/Users/razbk/Downloads/Raz - PycharmSheet.csv'

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
        self.cart = SmartbearCart(self.driver)

    def tearDown(self):
        pass
        # self.side_cart.close_cart()
        # self.header.main_menu_button()
        # self.header.open_cart()
        # self.side_cart.remove_item(0)

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
        # self.assertEqual(reader[13][3],self.side_cart.cart_quantity_number())
        self.assertEqual(self.side_cart.cart_item_quantity_value(0) + self.side_cart.cart_item_quantity_value(1),self.side_cart.cart_quantity_number())
        reader[14][3] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

    # --- [ Test 3 ] ---
    def test_name_price_quantity(self):
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
        category_index = int(reader[7][5])  # Adding product 2
        product_index = int(reader[9][5])
        quantity_index = int(reader[11][5])
        self.main_menu.click_category(category_index)
        self.category.click_product(product_index)
        self.product.change_item_quantity_value(quantity_index)
        self.product.add_to_cart()
        self.header.main_menu_button()
        category_index = int(reader[13][5])  # Adding product 3
        subcategory_index = int(reader[15][5])
        product_index = int(reader[17][5])
        quantity_index = int(reader[19][5])
        self.main_menu.click_category(category_index)
        self.category.click_sub_category(subcategory_index)
        self.category.click_product(product_index)
        self.product.change_item_quantity_value(quantity_index)
        self.product.add_to_cart()
        self.assertEqual(self.side_cart.cart_item_name(0),reader[18][5])
        self.assertEqual(self.side_cart.cart_item_name(1),reader[10][5])
        self.assertEqual(self.side_cart.cart_item_name(2),reader[4][5])
        self.assertEqual(self.side_cart.cart_item_price_number(0),float(reader[20][5]))
        self.assertEqual(self.side_cart.cart_item_price_number(1),float(reader[12][5]))
        self.assertEqual(self.side_cart.cart_item_price_number(2),float(reader[6][5]))
        self.assertEqual(self.side_cart.cart_item_quantity_value(0),int(reader[19][5]))
        self.assertEqual(self.side_cart.cart_item_quantity_value(1),int(reader[11][5]))
        self.assertEqual(self.side_cart.cart_item_quantity_value(2),int(reader[5][5]))
        reader[21][5] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

# --- [ Test 4 ] ---
    def test_product_removal(self):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            reader = list(reader)
        category_index = int(reader[1][7]) # Adding product 1
        product_index = int(reader[3][7])
        quantity_index = int(reader[5][7])
        self.main_menu.click_category(category_index)
        self.category.click_product(product_index)
        self.product.change_item_quantity_value(quantity_index)
        self.product.add_to_cart()
        self.header.main_menu_button()
        category_index = int(reader[7][7])  # Adding product 2
        product_index = int(reader[9][7])
        quantity_index = int(reader[11][7])
        self.main_menu.click_category(category_index)
        self.category.click_product(product_index)
        self.product.change_item_quantity_value(quantity_index)
        self.product.add_to_cart()
        self.side_cart.remove_item(1)
        self.side_cart.wait_for_cart_update()
        sleep(2)
        self.assertEqual(round(self.side_cart.cart_item_price_number(0)*float(self.side_cart.cart_item_quantity_value(0)),10),self.side_cart.cart_item_subtotal_number())
        self.assertEqual(self.side_cart.cart_item_name(0),reader[10][7])
        self.assertEqual(self.side_cart.cart_item_price_number(0),float(reader[12][7]))
        self.assertEqual(int(self.side_cart.cart_item_quantity_value(0)),int(reader[11][7]))
        reader[12][7] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

# --- [ Test 5 ] ---
    def test_cart_products_changes(self):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            reader = list(reader)
        category_index = int(reader[1][9]) # Adding product 1
        product_index = int(reader[3][9])
        self.main_menu.click_category(category_index)
        self.category.click_product(product_index)
        self.product.add_to_cart()
        self.side_cart.wait_for_cart_update()
        self.assertEqual(self.side_cart.get_cart_status(), "offcanvas offcanvas-lg offcanvas-overlay offcanvas-right offcanvas-shadow on")
        self.side_cart.close_cart()
        self.assertEqual(self.side_cart.get_cart_status(),"offcanvas offcanvas-lg offcanvas-overlay offcanvas-right offcanvas-shadow")
        self.side_cart.wait_for_cart_to_close()
        self.header.open_cart()
        self.assertEqual(self.side_cart.get_cart_status(), "offcanvas offcanvas-lg offcanvas-overlay offcanvas-right offcanvas-shadow on")
        self.side_cart.wait_for_cart_to_open()
        self.side_cart.go_to_cart()
        self.assertEqual(self.cart.get_header_text(),reader[5][9])
        reader[6][9] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

# --- [ Test 6 ] ---
    def test_shopping_carts_info(self):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            reader = list(reader)
        category_index = int(reader[1][11]) # Adding product 1
        product_index = int(reader[3][11])
        quantity_index = int(reader[5][11])
        self.main_menu.click_category(category_index)
        self.category.click_product(product_index)
        self.product.change_item_quantity_value(quantity_index)
        self.product.add_to_cart()
        self.header.main_menu_button()
        category_index = int(reader[6][11])  # Adding product 2
        product_index = int(reader[8][11])
        quantity_index = int(reader[10][11])
        self.main_menu.click_category(category_index)
        self.category.click_product(product_index)
        self.product.change_item_quantity_value(quantity_index)
        self.product.add_to_cart()
        self.header.main_menu_button()
        category_index = int(reader[11][11])  # Adding product 3
        product_index = int(reader[13][11])
        quantity_index = int(reader[15][11])
        self.main_menu.click_category(category_index)
        self.category.click_product(product_index)
        self.product.change_item_quantity_value(quantity_index)
        self.product.add_to_cart()
        self.assertEqual(round(self.side_cart.cart_item_price_number(0) * float(self.side_cart.cart_item_quantity_value(0)), 10)
                         + round(self.side_cart.cart_item_price_number(1) * float(self.side_cart.cart_item_quantity_value(1)), 10)
                         + round(self.side_cart.cart_item_price_number(2) * float(self.side_cart.cart_item_quantity_value(2)), 10)
                         ,self.side_cart.cart_item_subtotal_number())
        self.side_cart.go_to_cart()
        self.assertEqual(round(self.cart.get_cart_item_price(1) * float(self.cart.get_cart_item_quantity(1)), 10)
                         + round(self.cart.get_cart_item_price(2) * float(self.cart.get_cart_item_quantity(2)), 10)
                         + round(self.cart.get_cart_item_price(3) * float(self.cart.get_cart_item_quantity(3)), 10)
                         , self.cart.get_cart_subtotal_number())
        logging.basicConfig(level=logging.INFO)
        logging.info(f" Product 1 | {self.cart.get_cart_item_name(1)} | Quantity: {self.cart.get_cart_item_quantity(1)} | Price: {self.cart.get_cart_item_price(1)}")
        logging.info(f" Product 2 | {self.cart.get_cart_item_name(2)} | Quantity: {self.cart.get_cart_item_quantity(2)} | Price: {self.cart.get_cart_item_price(2)}")
        logging.info(f" Product 3 | {self.cart.get_cart_item_name(3)} | Quantity: {self.cart.get_cart_item_quantity(3)} | Price: {self.cart.get_cart_item_price(3)}")
        reader[16][11] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

# --- [ Test 7 ] ---
    def test(self):
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            reader = list(reader)
        category_index = int(reader[1][13]) # Adding product 1
        product_index = int(reader[3][13])
        quantity_index = int(reader[5][13])
        self.main_menu.click_category(category_index)
        self.category.click_product(product_index)
        self.product.change_item_quantity_value(quantity_index)
        self.product.add_to_cart()
        self.header.main_menu_button()
        category_index = int(reader[7][13])  # Adding product 2
        subcategory_index = int(reader[9][13])
        product_index = int(reader[11][13])
        quantity_index = int(reader[13][13])
        self.main_menu.click_category(category_index)
        self.category.click_sub_category(subcategory_index)
        self.category.click_product(product_index)
        self.product.change_item_quantity_value(quantity_index)
        self.product.add_to_cart()
        self.side_cart.go_to_cart()
        self.cart.change_item_quantity_value(1,int(reader[6][13]))
        self.cart.change_item_quantity_value(2,int(reader[14][13]))
        self.cart.wait_for_cart_update()
        self.assertEqual(round(self.cart.get_cart_item_price(1) * float(self.cart.get_cart_item_quantity(1)), 10),round(self.cart.get_cart_item_total_price(1),10))
        self.assertEqual(round(self.cart.get_cart_item_price(2) * float(self.cart.get_cart_item_quantity(2)), 10),round(self.cart.get_cart_item_total_price(2),10))
        self.assertEqual(self.cart.get_cart_item_total_price(1) + self.cart.get_cart_item_total_price(2),self.cart.get_cart_subtotal_number())
        self.header.main_menu_button()
        self.header.open_cart()
        self.assertEqual(round(self.side_cart.cart_item_price_number(0) * float(self.side_cart.cart_item_quantity_value(0)), 10)
                         + round(self.side_cart.cart_item_price_number(1) * float(self.side_cart.cart_item_quantity_value(1)), 10)
                         , self.side_cart.cart_item_subtotal_number())
        reader[15][13] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)