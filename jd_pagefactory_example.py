#* References
# https://selenium-page-factory.readthedocs.io/en/latest/
# https://www.browserstack.com/guide/page-object-model-in-selenium-python
# https://thoughtcoders.com/blogs/page-object-model-in-python/#google_vignette

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from seleniumpagefactory.Pagefactory import PageFactory
from pages.homepage import Homepage

# We will need to refactor this later on to a separate class 
# For now, we just want to explore the PageFactory implementation        
class Main_navigation(PageFactory):
    # It is necessary to to initialise driver as page class member to implement Page Factory
    def __init__(self, driver):
        self.driver = driver
    
    # define locators dictionary where key name will became WebElement using PageFactory   
    # A bit of trial and error in making the CSS locator work
    # Reference : https://thoughtcoders.com/blogs/page-object-model-in-python/#google_vignette
    locators = {
        'search_icon' : ('CSS', '.header__sub-nav-item.header__nav-item--search'),
        'search_text_field' : ('CSS', '#search-desktop > div > input')
    }
    
    def click_search_icon(self):
        print("Navigation_main - click_search_icon()")
        self.search_icon.click()
        
    def click_search_text_field(self):
        print("Navigation_main - click_search_text_field()")
        self.search_text_field.click()
        
    def enter_text_on_search_text_field(self, item_to_search):
        print(f"Navigation_main - enter_text_on_search_text_field() {item_to_search}")
        self.search_text_field.set_text(item_to_search)
    
        
# Move this later to another file once we have confirmed that it is working
def main():
    driver = webdriver.Chrome()
    try:
        driver.get('https://www.perthmint.com/')
        time.sleep(3)
        driver.maximize_window()
        
        homepage = Homepage(driver)
        homepage.click_accept_cookies()
        
        main_navigation = Main_navigation(driver)
        main_navigation.click_search_icon()
        main_navigation.click_search_text_field()
        main_navigation.enter_text_on_search_text_field("James")
        
    finally:
        print('We finally want this driver to quit')
        driver.quit()
        
if __name__ == "__main__":
    print('This is invoked from main method of jd_pagefactory_example.py')
    main()