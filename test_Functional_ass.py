import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_function(BrowserInstance):
    driver = BrowserInstance
    driver = webdriver.Chrome()

    expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]

    actualList = []  ## using append to fill the date into the list.

    driver.implicitly_wait(2)
    ## 5 sec is max time ,if it's done is 2 sec then it will save your 3 sec time.

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']").send_keys("ber")
    time.sleep(2)  ## We use time.sleep() before plural form
    results = driver.find_elements(By.XPATH,"//div[@class='products']/div") ## Returns list[]
    count = len(results)
    assert count >0

    for result in results:
        actualList.append(result.find_element(By.XPATH, "h4").text) ## adding data into list
        result.find_element(By.XPATH, "div/button").click()

    assert expectedList == actualList

    driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
    driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

    ## Sum validation..

    prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
    sum = 0
    for price in prices:
        sum = sum+ int(price.text)

    print(sum)
    totalAmount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
    assert sum == totalAmount

    driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR,"button[class='promoBtn']").click()


    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
    print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

    discountAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

    assert totalAmount > discountAmount

    # driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
    driver.find_element(By.XPATH,"//button[text()='Place Order']").click()

    countries = driver.find_elements(By.XPATH, "//select[@style='width: 200px;']")

    for country in countries:
        if country.text == "India":
            country.click()
            break

    driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()
    driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
    time.sleep(2)
    driver.close()
