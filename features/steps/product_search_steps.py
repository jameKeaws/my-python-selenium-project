from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.homepage import HomePage
from pages.main_navigation import MainNavigation
from pages.product_card import ProductCard

# We need to study this > : https://behave.readthedocs.io/en/stable/tutorial.html

# We need to convert this later to a PageFactory version, yeah later, let us explore Behave first
@given("a Google Chrome browser is at The Perth Mint home page : '{site_home_page}'")
def open_website(context, site_home_page):
    context.driver = webdriver.Chrome()
    context.driver.get(site_home_page)
    time.sleep(5)
    context.driver.maximize_window()
    # On the perthmint.com home page, click "OK" for the "Our site uses cookies" prompt
    homepage = HomePage(context.driver)
    homepage.click_accept_cookies()
    
# value_to_search value is coming from product_search.feature
@when("the user enters '{value_to_search}' into the search bar")
def search_product(context, value_to_search):
    # On the perthmint.com home page, click on the search icon on the upper right hand side of the page
    # Code refactor to use PageFactory
    main_navigation = MainNavigation(context.driver)
    # Click on the Search icon on the navigation bar <upper right hand side of the page>
    main_navigation.click_search_icon()
    # Click on the Search text field
    main_navigation.click_search_text_field()
    # Enter applicable item/product to search
    wait_time = 5
    main_navigation.enter_text_on_search_text_field(value_to_search, wait_time)
    time.sleep(3)
    main_navigation.click_search_bar_button(wait_time)
    time.sleep(3)
        
@then("product cards related to '{value_to_search}' are shown on the search results page")
def verify_search_result(context, value_to_search):
    # For now we have theh product hard coded, I think we need to do a Python Data Factory
    # James Bond Skyfall 2022 1/2oz Silver Proof Coloured Coin
    target_product_card_url = 'https://www.perthmint.com/shop/collector-coins/coins/james-bond-skyfall-2022-1-2oz-silver-proof-coloured-coin/'
    target_sku = '22J15AAA'
    product_card = ProductCard(context.driver, target_product_card_url, target_sku)
    # product_card.find_target_product_card_sku_element()
    product_card.click_target_product_card_url()
    time.sleep(5)
    context.driver.quit()