from selenium.webdriver.common.by import By


class Locators:


    QUOTE_LOCATOR = (By.XPATH, '//div[@class="quote"]')
    SINGLE_AUTHOR_LOCATOR = (By.XPATH, '(//small[@class="author"])[1]')
    AUTHOR_LOCATOR = (By.XPATH, '//small[@class="author"]')
    TAG_LOCATOR = (By.XPATH, './/div[@class="tags"]')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//a[contains(text(),"Next")]')
    
    
   