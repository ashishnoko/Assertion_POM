from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locators


class Author:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        
        
    def get_author(self):
      return self.wait.until(EC.presence_of_all_elements_located(Locators.AUTHOR_LOCATOR))
  
    def get_singleauthor(self):
      return self.wait.until(EC.presence_of_element_located(Locators.SINGLE_AUTHOR_LOCATOR))
    
    def get_top10tagsauthor(self):
      return self.wait.until(EC.presence_of_element_located(Locators.SINGLE_AUTHOR_LOCATOR))
    
    
    def get_nextbutton(self):
      return self.wait.until(EC.presence_of_element_located(Locators.NEXT_BUTTON_LOCATOR))
    
    def get_about(self):
      return self.wait.until(EC.presence_of_element_located(Locators.ABOUT_LOCATOR))
    
    
    
    
  