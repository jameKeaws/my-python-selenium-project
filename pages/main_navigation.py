#* References
# https://selenium-page-factory.readthedocs.io/en/latest/
# https://www.browserstack.com/guide/page-object-model-in-selenium-python
# https://thoughtcoders.com/blogs/page-object-model-in-python/#google_vignette

from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
     
class Main_navigation(PageFactory):
    # It is necessary to to initialise driver as page class member to implement Page Factory
    def __init__(self, driver):
        self.driver = driver
        self.search_text_field_css_selector = '#search-desktop > div > input'
        self.search_bar_button_css_selector = '#search-desktop > div > button.header__sub-nav-item.search-bar__search-button.px-3'
    
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
        
    def enter_text_on_search_text_field(self, item_to_search, wait_time_in_seconds):
        print(f"Navigation_main - enter_text_on_search_text_field() - item_to_search: {item_to_search} , wait_time_in_seconds: {wait_time_in_seconds}")
        # This was the original implementation based on PageFactory, but we are implementing a bit different to see if it still works
        # self.search_text_field.set_text(item_to_search)
        
        search_text_field = WebDriverWait(self.driver, wait_time_in_seconds).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.search_text_field_css_selector))
        )
        search_text_field.send_keys(item_to_search)
        
    def click_search_bar_button(self, wait_time_in_seconds):
        print("Navigation_main - click_search_bar_button()")
        search_bar_button = WebDriverWait(self.driver, wait_time_in_seconds).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.search_bar_button_css_selector))
        )
        search_bar_button.click()