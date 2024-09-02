#* References
# https://selenium-page-factory.readthedocs.io/en/latest/
# https://www.browserstack.com/guide/page-object-model-in-selenium-python
# https://thoughtcoders.com/blogs/page-object-model-in-python/#google_vignette

from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Product_card(PageFactory):
    # It is necessary to to initialise driver as page class member to implement Page Factory
    def __init__(self, driver, target_product_card_url):
        self.driver = driver
        self.product_card_url = target_product_card_url
    
    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        'cookies_accept' : ('ID', 'onetrust-accept-btn-handler')
    }
    
    def click_target_product_card_url(self):
        print("Product_card - click_target_product_card_url()")
        target_product_card_link = self.driver.find_element(By.XPATH, '//a[@href="'+self.product_card_url+'"]')
        target_product_card_link.click()