import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sort(BrowserInstance):
    driver = BrowserInstance

    browserSortedVegi = []

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    driver.maximize_window()

    ##Click on column header.

    driver.find_element(By.XPATH, "//span[text()= 'Veg/fruit name']").click()

    ## Collect all vegi name in to the list. for putting into the list use find_elements

    vegiWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

    for ele in vegiWebElements:
        browserSortedVegi.append(ele.text)

    originalBrowserSortedlist = browserSortedVegi.copy()

    ## Sort this Browser sorted list.

    browserSortedVegi.sort()

    time.sleep(3)

    assert browserSortedVegi == originalBrowserSortedlist


