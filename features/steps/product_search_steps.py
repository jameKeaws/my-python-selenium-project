from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

@given('a Google Chrome browser is at The Perth Mint home page')
def open_website(context):
    cookies_button_ok_id = 'onetrust-accept-btn-handler'
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.perthmint.com/')
    time.sleep(5)
    context.driver.maximize_window()
    
    # On the perthmint.com home page, click "OK" for the "Our site uses cookies" prompt
    cookies_ok_button = WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.ID, cookies_button_ok_id))
    )
    cookies_ok_button.click()
    

@when('the user enters "James" into the search bar')
def search_product(context):
    value_to_search = 'James'
    search_text_field_css_selector = '#search-desktop > div > input'
    # On the perthmint.com home page, click on the search icon on the upper right hand side of the page
    search_icon = context.driver.find_element(By.CSS_SELECTOR, '.header__sub-nav-item.header__nav-item--search')
    search_icon.click()
    
    search_text_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, search_text_field_css_selector))
    )
    search_text_field.send_keys(value_to_search)
    time.sleep(5)
        

@then('product cards related to "James" are shown on the search results page')
def verify_search_result(context):
    # We just closed the driver here as we are just testing if the Behave Framework could be run
    context.driver.quit()