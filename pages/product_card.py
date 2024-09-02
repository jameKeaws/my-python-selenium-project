#* References
# https://selenium-page-factory.readthedocs.io/en/latest/
# https://www.browserstack.com/guide/page-object-model-in-selenium-python
# https://thoughtcoders.com/blogs/page-object-model-in-python/#google_vignette

from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProductCard(PageFactory):
    # It is necessary to to initialise driver as page class member to implement Page Factory
    def __init__(self, driver, product_card_url, sku):
        self.driver = driver
        self.product_card_url = product_card_url
        self.sku = sku
    
    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        'cookies_accept' : ('ID', 'onetrust-accept-btn-handler')
    }
    
    def click_target_product_card_url(self):
        print(f"ProductCard - click_target_product_card_url() - {self.product_card_url}")
        target_product_card_link = self.driver.find_element(By.XPATH, '//a[@href="'+self.product_card_url+'"]')
        target_product_card_link.click()
    
    # Reference : https://stackoverflow.com/questions/3206975/xpath-selecting-elements-that-equal-a-value
    # https://stackoverflow.com/questions/20996392/how-to-get-text-with-selenium-webdriver-in-python      
    def find_target_product_card_sku_element(self):
        print(f"ProductCard - find_target_product_card_sku_element() - {self.sku}")
        target_product_sku = self.driver.find_element(By.XPATH, '//*[text()="'+self.sku+'"]')
        print(f"target_product_sku.text : {target_product_sku.text}")