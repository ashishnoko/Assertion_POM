from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.common.exceptions import TimeoutException

from locator import Locators
from pages.quote import Quote
from pages.author import Author





class Test(unittest.TestCase): 
    
    
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.get("https://quotes.toscrape.com/")
        self.quote = Quote(self.driver)
        self.author = Author(self.driver)
    
    
    def test_firstquote(self):
        
        extract_quote = self.quote.get_quotes()
        for quotes in extract_quote:
            print(quotes.text)
            
            
    def test_firstauthor(self):
        
        extract_author = self.author.get_author()
        for author in extract_author:
            print(author.text) 
        
        
        
    def test_author(self):
        
        first_author = self.author.get_singleauthor()
        expected_value ="Albert Einstein"
        self.assertEqual(first_author.text,expected_value,' Name Not Match')
        
        
    def test_authorname(self):
        
        author_name = self.author.get_singleauthor()
        self.assertTrue(author_name.is_displayed(),'Name not found')
        
        
        
    
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    def tearDown(self):
        self.driver.quit()
        
    
        

if __name__ == "__main__":
    unittest.main(defaultTest="Test.test_author")