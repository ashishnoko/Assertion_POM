from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locators


class Quote:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        
        
    def get_quotes(self):
      return self.wait.until(EC.presence_of_all_elements_located(Locators.QUOTE_LOCATOR))
  
  
         
    def get_singlequotes(self):
      return self.wait.until(EC.presence_of_all_elements_located(Locators.SINGLE_QUOTE_LOCATOR))
  
  
  
  
    
        
        
    