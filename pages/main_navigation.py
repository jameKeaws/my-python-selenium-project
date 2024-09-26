#* References
# https://selenium-page-factory.readthedocs.io/en/latest/
# https://www.browserstack.com/guide/page-object-model-in-selenium-python
# https://thoughtcoders.com/blogs/page-object-model-in-python/#google_vignette

from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
     
class MainNavigation(PageFactory):
    # It is necessary to to initialise driver as page class member to implement Page Factory
    def __init__(self, driver):
        self.driver = driver
        self.search_text_field_css_selector = '#search-desktop > div > input'
        self.search_bar_button_css_selector = '#search-desktop > div > button.header__sub-nav-item.search-bar__search-button.px-3'
        self.close_search_bar_icon_css_selector = '#search-desktop > div > button.header__sub-nav-item.search-bar__close-button.px-3.show-for-medium > svg'
    
    # define locators dictionary where key name will became WebElement using PageFactory   
    # A bit of trial and error in making the CSS locator work
    # Reference : https://thoughtcoders.com/blogs/page-object-model-in-python/#google_vignette
    # We might be able to use XPath but we need to explore it more
    # For example search_icon //*[@id="search-desktop"]/div/button[1]
    # search_text_field //*[@id="search-desktop"]/div/input
    locators = {
        'search_icon' : ('CSS', '.header__sub-nav-item.header__nav-item--search'),
        'search_text_field' : ('CSS', '#search-desktop > div > input'),
        'close_search_bar_icon' : ('CSS', '#search-desktop > div > button.header__sub-nav-item.search-bar__close-button.px-3.show-for-medium > svg')
    }
    
    def click_search_icon(self):
        print("MainNavigation - click_search_icon()")
        self.search_icon.click()
        
    def click_search_text_field(self):
        print("MainNavigation - click_search_text_field()")
        self.search_text_field.click()
        
    def enter_text_on_search_text_field(self, item_to_search, wait_time_in_seconds):
        print(f"MainNavigation - enter_text_on_search_text_field() - item_to_search: {item_to_search} , wait_time_in_seconds: {wait_time_in_seconds}")
        # This was the original implementation based on PageFactory, but we are implementing a bit different to see if it still works
        # self.search_text_field.set_text(item_to_search)
        
        search_text_field = WebDriverWait(self.driver, wait_time_in_seconds).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.search_text_field_css_selector))
        )
        search_text_field.send_keys(item_to_search)
        
    def click_search_bar_button(self, wait_time_in_seconds):
        '''Clicks on the Search button after we have entered item/product to search'''
        print("MainNavigation - click_search_bar_button()")
        search_bar_button = WebDriverWait(self.driver, wait_time_in_seconds).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.search_bar_button_css_selector))
        )
        search_bar_button.click()
        
    def close_search_bar(self):
        '''Closes the search bar usign the X button'''
        print("MainNavigation - close_search_bar()")
        self.close_search_bar_icon.click()