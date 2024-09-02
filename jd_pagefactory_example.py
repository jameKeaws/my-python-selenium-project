#* References
# https://selenium-page-factory.readthedocs.io/en/latest/
# https://www.browserstack.com/guide/page-object-model-in-selenium-python
# https://thoughtcoders.com/blogs/page-object-model-in-python/#google_vignette

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from seleniumpagefactory.Pagefactory import PageFactory
from pages.homepage import Homepage
from pages.main_navigation import Main_navigation
from pages.product_card import Product_card


def main():
    driver = webdriver.Chrome()
    
    try:
        driver.get('https://www.perthmint.com/')
        time.sleep(3)
        driver.maximize_window()
        wait_time = 3
        
        # Upon load of Home page, click "OK" for the "Our site uses cookies" prompt
        homepage = Homepage(driver)
        homepage.click_accept_cookies()
        
        main_navigation = Main_navigation(driver)
        # Click on the Search icon on the navigation bar <upper right hand side of the page>
        main_navigation.click_search_icon()
        # Click on the Search text field
        main_navigation.click_search_text_field()
        # Enter applicable item/product to search
        main_navigation.enter_text_on_search_text_field("James", wait_time)
        time.sleep(3)
        # Click the Search button
        main_navigation.click_search_bar_button(wait_time)
        time.sleep(3)
        
        # James Bond Legacy Series - 5th Issue 2024 1oz Silver Proof Coloured Coin
        target_product_card_url = 'https://www.perthmint.com/shop/collector-coins/coins/james-bond-legacy-series-5th-issue-2024-1oz-silver-proof-coloured-coin/'
        target_sku = '24S84AAA'
        
        # James Bond Skyfall 2022 1/2oz Silver Proof Coloured Coin
        target_product_card_url = 'https://www.perthmint.com/shop/collector-coins/coins/james-bond-skyfall-2022-1-2oz-silver-proof-coloured-coin/'
        target_sku = '22J15AAA'
        product_card = Product_card(driver, target_product_card_url, target_sku)
        product_card.find_target_product_card_sku_element()
        product_card.click_target_product_card_url()
        time.sleep(5)
        
    finally:
        print('We finally want this driver to quit')
        driver.quit()
        
if __name__ == "__main__":
    print('This is invoked from main method of jd_pagefactory_example.py')
    main()