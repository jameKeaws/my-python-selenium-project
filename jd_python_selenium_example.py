from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#* References
#https://www.youtube.com/watch?v=b5jt2bhSeXs&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ&index=2
#https://stackoverflow.com/questions/51336849/selenium-implicit-and-explicit-waits-not-working-has-no-effect

def main():
    value_to_search = 'James'
    # search_text_field = driver.find_element(By.CSS_SELECTOR, '#search-desktop > div > input')
    # Move this to a configuration file
    search_text_field_css_selector = '#search-desktop > div > input'
    search_bar_button_css_selector ='#search-desktop > div > button.header__sub-nav-item.search-bar__search-button.px-3'
    target_product_url = 'https://www.perthmint.com/shop/collector-coins/coins/james-bond-legacy-series-5th-issue-2024-1oz-silver-proof-coloured-coin/'
    target_product_image_url = 'https://www.perthmint.com/globalassets/assets/product-images-e-com-pages/coins/24s84aaa/01-legacy-series-5th-issue-2024-1oz-silver-proof-coloured-coin-onedge-highres.jpg?width=200&format=webp'
    
    driver = webdriver.Chrome()

    try:
        # Navigate to perthmint.com
        driver.get('https://www.perthmint.com/')
        time.sleep(5)
        driver.maximize_window()
        
        # On the perthmint.com home page, click on 
        search_iconx = driver.find_element(By.CSS_SELECTOR, '.header__sub-nav-item.header__nav-item--search')
        search_iconx.click()
        search_text_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, search_text_field_css_selector))
        )
        search_text_field.send_keys(value_to_search)
        time.sleep(5)
        
        # search_bar = driver.find_element(By.CSS_SELECTOR, '#search-desktop > div > button.header__sub-nav-item.search-bar__search-button.px-3')
        # search_bar.click()
        # time.sleep(5)
        search_bar_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, search_bar_button_css_selector))
        )
        search_bar_button.click()
        time.sleep(5)

        # targetProductDetailsPageLink = driver.find_element_by_xpath('//a[@href="'+targetProductUrl+'"]')
        target_product_details_page_link = driver.find_element(By.XPATH, '//a[@href="'+target_product_url+'"]')
        # target_product_image = driver.find_element(By.XPATH, '//img[@src="'+target_product_image_url+'")]')
        # hover = ActionChains(driver).move_to_element(target_product_details_page_link)
        # hover.perform()
        time.sleep(5)
        target_product_details_page_link.click()
        driver.save_screenshot('foo.png')
        time.sleep(5)
        # product_text = 'My This 1oz silver proof piece pays tribute to Daniel Craig, the sixth actor to play fictional British Secret Service agent James Bond on the big screen.'
        
        # product_description_text = driver.find_element(By.XPATH,'//*[text()="'+product_text+'"]')
        # product_description_text = driver.find_element(By.XPATH, "//*[text()='My This 1oz silver proof piece pays tribute to Daniel Craig, the sixth actor to play fictional British Secret Service agent James Bond on the big screen.']");

        
        driver.back()
        # print(product_description_text.text)
        # assert 'This 1oz silver proof piece pays tribute to Daniel Craig' in product_description_text.text

        
    finally:
        print('We finally want this driver to quit')
        driver.quit()
        
if __name__ == "__main__":
    print('This is invoked from main method of jd_python_selenium_example.py')
    main()