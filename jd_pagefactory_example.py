#* References
# https://selenium-page-factory.readthedocs.io/en/latest/
# https://www.browserstack.com/guide/page-object-model-in-selenium-python
# https://thoughtcoders.com/blogs/page-object-model-in-python/#google_vignette

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from seleniumpagefactory.Pagefactory import PageFactory
from pages.homepage import Homepage
from pages.main_navigation import Main_navigation

def main():
    driver = webdriver.Chrome()
    
    try:
        driver.get('https://www.perthmint.com/')
        time.sleep(3)
        driver.maximize_window()
        wait_time = 3
        
        homepage = Homepage(driver)
        homepage.click_accept_cookies()
        
        main_navigation = Main_navigation(driver)
        main_navigation.click_search_icon()
        main_navigation.click_search_text_field()
        main_navigation.enter_text_on_search_text_field("James", wait_time)
        time.sleep(3)
        main_navigation.click_search_bar_button(wait_time)
        time.sleep(3)
    finally:
        print('We finally want this driver to quit')
        driver.quit()
        
if __name__ == "__main__":
    print('This is invoked from main method of jd_pagefactory_example.py')
    main()