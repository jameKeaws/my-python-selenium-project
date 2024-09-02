from seleniumpagefactory.Pagefactory import PageFactory

# We will need to refactor this later on to a separate class 
# For now, we just want to explore the PageFactory implementation
class Homepage(PageFactory):
    # It is necessary to to initialise driver as page class member to implement Page Factory
    def __init__(self, driver):
        self.driver = driver
    
    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        'cookies_accept' : ('ID', 'onetrust-accept-btn-handler')
    }
    
    # define locators dictionary where key name will became WebElement using PageFactory
    def click_accept_cookies(self):
        print("Homepage - click_accept_cookies()")
        self.cookies_accept.click()