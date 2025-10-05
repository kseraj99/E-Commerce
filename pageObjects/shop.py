from selenium.webdriver.common.by import By

from pageObjects.checkout_confirmation import CheckoutConfirmation
from utils.browserutils import BrowserUtils


## * will split the tuple into two parameter

class ShopPage(BrowserUtils):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.shop_link = (By.XPATH, "//a[@href='/angularpractice/shop']")
        self.product_card = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def add_product_to_cart(self, product_name):

        self.driver.find_element(*self.shop_link).click()

        products = self.driver.find_elements(*self.product_card)

        for product in products:
            productName = product.find_element(By.XPATH, "//div[@class='card h-100']/div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "//div[@class='card h-100']/div[2]/button").click()

    def goToCart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation = CheckoutConfirmation(self.driver)
        return checkout_confirmation