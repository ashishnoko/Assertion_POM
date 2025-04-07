from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locators


class Login_Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        
        
        
   
   
    def click_login(self):
        return self.wait.until(EC.presence_of_element_located(Locators.LOGIN_BUTTON)).click()
  
    def enter_username(self,username):
        return self.wait.until(EC.presence_of_element_located(Locators.USERNAME_FIELD)).send_keys(username)
    
    
    def enter_password(self,password):
        return self.wait.until(EC.presence_of_element_located(Locators.PASSWORD_FIELD)).send_keys(password)
    
    
     
    def login_btn(self):
        return self.wait.until(EC.presence_of_element_located(Locators.SUBMIT_BUTTON)).click()
    
     
    def logout_btn(self):
        return self.wait.until(EC.presence_of_element_located(Locators.LOGOUT_BUTTON)).click()
    
    
    def logout_visible(self):
        return self.wait.until(EC.presence_of_element_located(Locators.LOGOUT_BUTTON)).text 
    
    
    def login_errorlink(self):
        return self.wait.until(EC.presence_of_element_located(Locators.LOGIN_ERROR_LINK)).text 