from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locators


class Tags:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        
   
   
    def get_totaltags(self):
      return self.wait.until(EC.presence_of_all_elements_located(Locators.TAG_LOCATOR))
  
    
    def get_total10tags(self):
      return self.wait.until(EC.presence_of_element_located(Locators.FIRST_TOP_10_TAGS))
  
    def get_author_top10(self):
        return self.wait.until(EC.presence_of_element_located(Locators.TOP_10_TAGS_AUTHOR))
        
  
    
    
  
    
    
      
