from selenium.webdriver.common.by import By


class Locators:


    QUOTE_LOCATOR = (By.XPATH, '//div[@class="quote"]')
    SINGLE_QUOTE_LOCATOR = (By.XPATH, '(//span[@class="text"])[3]')
    SINGLE_AUTHOR_LOCATOR = (By.XPATH, '(//small[@class="author"])[1]')
    AUTHOR_LOCATOR = (By.XPATH, '//small[@class="author"]')
    TOP_10_TAGS_AUTHOR =  (By.XPATH, '(//small[@class])[1]')
    TAG_LOCATOR = (By.XPATH, '//div[@class="tags"]')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//li/a')
    ABOUT_LOCATOR = (By.XPATH,'(//span/a)[3]')
    FIRST_TOP_10_TAGS = (By.XPATH,'(//span/a[@class="tag"])[1]')
    TOP_10_TAGS = (By.XPATH,'//span/a[@class="tag"]')
    
    
   