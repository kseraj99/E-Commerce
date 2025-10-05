import json
import os
import sys
import time

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.login import LoginPage
# from pageObjects.shop import ShopPage
## whenever you want to come out from the folder use '../'

test_data_path = './data/test_e2eFrameworkTest.json'

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


## Marking test with custom tag

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(BrowserInstance, test_list_item):
    driver = BrowserInstance
    ## Constructor argument has to give when you create the object
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shop_page = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.getTitle())
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()



