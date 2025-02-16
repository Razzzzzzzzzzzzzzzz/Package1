from unittest import TestCase
from selenium import webdriver
import logging
from Smartbear_Main_Menu import SmartbearMainMenu
from Smartbear_Category import SmartbearCategory
from Smartbear_Product import SmartbearProduct
from Smartbear_Side_Cart import SmartbearSideCart
from Smartbear_Header import SmartbearHeader
from Smartbear_Cart import SmartbearCart
from Smartbear_Login import SmartbearLogin
from Smartbear_Checkout import SmartbearCheckout
from Smartbear_Order_Details import SmartbearOrderDetails
import csv
csv_file_path = 'C:/Users/razbk/Downloads/Raz - PycharmSheet.csv'

class TestPetstoreMenu(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bearstore-testsite.smartbear.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.main_menu = SmartbearMainMenu(self.driver)
        self.category = SmartbearCategory(self.driver)
        self.product = SmartbearProduct(self.driver)
        self.side_cart = SmartbearSideCart(self.driver)
        self.header = SmartbearHeader(self.driver)
        self.cart = SmartbearCart(self.driver)
        self.login = SmartbearLogin(self.driver)
        self.checkout = SmartbearCheckout(self.driver)
        self.order_details = SmartbearOrderDetails(self.driver)
        logging.basicConfig(level=logging.INFO) # Enables logging for all tests

    def tearDown(self):
        pass
        self.header.main_menu_button()
        self.header.open_cart()
        self.side_cart.empty_cart() # Removes all products when the test ends
        self.main_menu.close_website()

    def test_screens_transitions(self):
        logging.info(" Test 1 Started")
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            reader = list(reader) # Takes the Excel Sheet data
        category_index = int(reader[1][1])
        category_name = reader[2][1] # Category name taken from Excel
        self.main_menu.click_category(category_index)
        self.assertEqual(category_name, self.category.page_title_name())
        logging.info(" [V] Category Name")
        product_index = int(reader[3][1])
        product_name = reader[4][1] # Product name taken from Excel
        self.category.click_product(product_index)
        self.assertEqual(product_name, self.product.product_title_name())
        logging.info(" [V] Product Name")
        self.product.return_back(2)
        self.assertEqual(category_name, self.category.page_title_name())
        logging.info(" [V] Returned to Category Page")
        self.category.return_back(0)
        main_menu_welcome_message = reader[5][1] # Taken from Excel
        self.assertEqual(main_menu_welcome_message,
                         self.main_menu.menu_welcome_message_test())
        logging.info(" [V] Returned to Main Menu")
        reader[6][1] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader) # Writes the info to Excel

    def test_total_quantity(self):
        logging.info(" Test 2 Started")
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
        self.side_cart.wait_for_cart_to_open()
        self.assertEqual(self.side_cart.cart_item_quantity_value(0) +
                        self.side_cart.cart_item_quantity_value(1),
                        self.side_cart.cart_quantity_number())
        logging.info(" [V] Products Total Quantity")
        self.side_cart.close_cart()
        self.side_cart.wait_for_cart_to_close()
        reader[14][3] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

    # --- [ Test 3 ] ---
    def test_name_price_quantity(self):
        logging.info(" Test 3 Started")
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
        logging.info(" [V] Products Names")
        self.assertEqual(self.side_cart.cart_item_price_number(0),
                        float(reader[20][5]))
        self.assertEqual(self.side_cart.cart_item_price_number(1),
                        float(reader[12][5]))
        self.assertEqual(self.side_cart.cart_item_price_number(2),
                        float(reader[6][5]))
        logging.info(" [V] Products Prices")
        self.assertEqual(self.side_cart.cart_item_quantity_value(0),
                        int(reader[19][5]))
        self.assertEqual(self.side_cart.cart_item_quantity_value(1),
                        int(reader[11][5]))
        self.assertEqual(self.side_cart.cart_item_quantity_value(2),
                        int(reader[5][5]))
        logging.info(" [V] Products Quantity")
        self.side_cart.close_cart()
        self.side_cart.wait_for_cart_to_close()
        reader[21][5] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

# --- [ Test 4 ] ---
    def test_product_removal(self):
        logging.info(" Test 4 Started")
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
        self.assertEqual(round(self.side_cart.cart_item_price_number(0)*
                        float(self.side_cart.cart_item_quantity_value(0)),10),
                        self.side_cart.cart_item_subtotal_number())
        logging.info(" [V] Remaining Products Subtotal Change")
        self.assertEqual(self.side_cart.cart_item_name(0),reader[10][7])
        logging.info(" [V] Remaining Product Name")
        self.assertEqual(self.side_cart.cart_item_price_number(0),
                        float(reader[12][7]))
        logging.info(" [V] Remaining Product Price")
        self.assertEqual(int(self.side_cart.cart_item_quantity_value(0)),
                        int(reader[11][7]))
        logging.info(" [V] Remaining Product Quantity")
        self.side_cart.close_cart()
        self.side_cart.wait_for_cart_to_close()
        reader[13][7] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

# --- [ Test 5 ] ---
    def test_cart_products_changes(self):
        logging.info(" Test 5 Started")
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            reader = list(reader)
        category_index = int(reader[1][9]) # Adding product 1
        product_index = int(reader[3][9])
        self.main_menu.click_category(category_index)
        self.category.click_product(product_index)
        self.product.add_to_cart()
        self.side_cart.wait_for_cart_update()
        self.assertEqual(self.side_cart.get_cart_status(),
                        "offcanvas offcanvas-lg offcanvas-overlay "
                        "offcanvas-right offcanvas-shadow on")
        logging.info(" [V] Cart Opening Automatically")
        self.side_cart.close_cart()
        self.assertEqual(self.side_cart.get_cart_status(),
                        "offcanvas offcanvas-lg offcanvas-overlay "
                        "offcanvas-right offcanvas-shadow")
        logging.info(" [V] Cart Closing After Screen Touch")
        self.side_cart.wait_for_cart_to_close()
        self.header.open_cart()
        self.assertEqual(self.side_cart.get_cart_status(),
                         "offcanvas offcanvas-lg offcanvas-overlay "
                         "offcanvas-right offcanvas-shadow on")
        logging.info(" [V] Cart Opening After Shopcart Press")
        self.side_cart.wait_for_cart_to_open()
        self.side_cart.go_to_cart()
        self.assertEqual(self.cart.get_header_text(),reader[5][9])
        logging.info(" [V] \"Go To Cart\" Transfers To Cart ")
        reader[6][9] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

# --- [ Test 6 ] ---
    def test_shopping_carts_info(self):
        logging.info(" Test 6 Started")
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
        self.assertEqual(round(self.side_cart.cart_item_price_number(0) *
                        float(self.side_cart.cart_item_quantity_value(0)), 10)
                        + round(self.side_cart.cart_item_price_number(1) *
                        float(self.side_cart.cart_item_quantity_value(1)), 10)
                        + round(self.side_cart.cart_item_price_number(2) *
                        float(self.side_cart.cart_item_quantity_value(2)), 10)
                        ,self.side_cart.cart_item_subtotal_number())
        logging.info(" [V] Side Cart Subtotal")
        self.side_cart.go_to_cart()
        self.assertEqual(round(self.cart.get_cart_item_price(1) *
                        float(self.cart.get_cart_item_quantity(1)), 10)
                        + round(self.cart.get_cart_item_price(2) *
                        float(self.cart.get_cart_item_quantity(2)), 10)
                        + round(self.cart.get_cart_item_price(3) *
                        float(self.cart.get_cart_item_quantity(3)), 10)
                        , self.cart.get_cart_subtotal_number())
        logging.info(" [V] Cart Page Subtotal")
        logging.info(f" Product 1 | {self.cart.get_cart_item_name(1)}"
                     f" | Quantity: {self.cart.get_cart_item_quantity(1)}"
                     f" | Price: {self.cart.get_cart_item_price(1)}")
        logging.info(f" Product 2 | {self.cart.get_cart_item_name(2)}"
                     f" | Quantity: {self.cart.get_cart_item_quantity(2)}"
                     f" | Price: {self.cart.get_cart_item_price(2)}")
        logging.info(f" Product 3 | {self.cart.get_cart_item_name(3)}"
                     f" | Quantity: {self.cart.get_cart_item_quantity(3)}"
                     f" | Price: {self.cart.get_cart_item_price(3)}")
        reader[16][11] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

# --- [ Test 7 ] ---
    def test(self):
        logging.info(" Test 7 Started")
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
        self.assertEqual(round(self.cart.get_cart_item_price(1) *
                        float(self.cart.get_cart_item_quantity(1)), 10),
                        round(self.cart.get_cart_item_total_price(1),10))
        logging.info(" [V] First Product Total Price")
        self.assertEqual(round(self.cart.get_cart_item_price(2) *
                        float(self.cart.get_cart_item_quantity(2)), 10),
                        round(self.cart.get_cart_item_total_price(2),10))
        logging.info(" [V] Second Product Total Price")
        self.assertEqual(self.cart.get_cart_item_total_price(1) +
                        self.cart.get_cart_item_total_price(2),
                        self.cart.get_cart_subtotal_number())
        logging.info(" [V] Products Subtotal")
        self.header.main_menu_button()
        self.header.open_cart()
        self.assertEqual(round(self.side_cart.cart_item_price_number(0) *
                        float(self.side_cart.cart_item_quantity_value(0)), 10)
                        + round(self.side_cart.cart_item_price_number(1) *
                        float(self.side_cart.cart_item_quantity_value(1)), 10)
                        , self.side_cart.cart_item_subtotal_number())
        logging.info(" [V] Products Side cart Subtotal")
        self.side_cart.close_cart()
        self.side_cart.wait_for_cart_to_close()
        reader[15][13] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

# --- [ Test 8 ] ---
    def test_order_completion(self):
        logging.info(" Test 8 Started")
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            reader = list(reader)
        category_index = int(reader[1][15]) # Adding product 1
        product_index = int(reader[3][15])
        self.main_menu.click_category(category_index)
        self.category.click_product(product_index)
        self.product.add_to_cart()
        self.header.main_menu_button()
        category_index = int(reader[5][15])  # Adding product 2
        subcategory_index = int(reader[7][15])
        product_index = int(reader[9][15])
        self.main_menu.click_category(category_index)
        self.category.click_sub_category(subcategory_index)
        self.category.click_product(product_index)
        self.product.add_to_cart()
        self.side_cart.checkout()
        self.login.change_username(reader[11][15])
        self.login.change_password(reader[12][15])
        self.login.login()
        self.cart.click_checkout()
        self.checkout.change_address_firstname(reader[13][15])
        self.checkout.change_address_lastname(reader[14][15])
        self.checkout.click_address_next_page_button()
        self.checkout.change_address_firstname(reader[13][15])
        self.checkout.change_address_lastname(reader[14][15])
        self.checkout.click_address_next_page_button()
        self.checkout.click_shipping_next_page_button()
        self.checkout.click_payment_next_page_button()
        self.checkout.approve_terms_of_service()
        self.checkout.click_confirm()
        self.assertEqual(self.checkout.order_received_text(),reader[15][15])
        logging.info(" [V] Order Received")
        reader[16][15] = self.checkout.order_number_text()
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader) # Writes the Order Number in Excel
        self.checkout.click_order_details()
        self.assertEqual(reader[16][15],
                        self.order_details.get_order_number_text())
        logging.info(" [V] Order Number Matching Order Details Screen")
        self.header.open_cart()
        self.assertFalse(self.side_cart.cart_items())
        logging.info(" [V] Cart Is Empty")
        self.side_cart.close_cart()
        self.side_cart.wait_for_cart_to_close()
        reader[17][15] = 'V'
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

# --- [ Test 9 ] ---
    def test_login_logout(self):
        logging.info(" Test 9 Started")
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            reader = list(reader)
            self.header.open_login()
            self.login.change_username(reader[1][17])
            self.login.change_password(reader[2][17])
            self.login.login()
            self.assertEqual(self.header.get_logged_in_username_text()
                            .lower(),
                            reader[1][17].lower())
            logging.info(" [V] User Connected")
            self.header.open_login()
            self.header.logout()
            self.assertNotEqual(self.header.get_logged_in_username_text()
                                .lower(),
                                reader[1][17].lower())
            logging.info(" [V] User Disconnected")
            reader[3][17] = 'V'
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(reader)