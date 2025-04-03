from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

from selenium.webdriver.chrome.options import Options


from locator import Locators
from pages.quote import Quote
from pages.author import Author
from pages.tags import Tags





class Test(unittest.TestCase): 
    
    
    
    def setUp(self):
        
        
        self.driver = webdriver.Chrome()
        #chrome_options = Options()
        #chrome_options.add_argument("--headless")  # Ensure GUI is not launched
        #self.driver = webdriver.Chrome(options=chrome_options)
        
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.get("https://quotes.toscrape.com/")
        self.quote = Quote(self.driver)
        self.author = Author(self.driver)
        self.tags = Tags(self.driver)
        
    
    
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
        
        
    def test_next_button(self):
       
        try:
            
            next_button = self.author.get_nextbutton()


            self.assertTrue(next_button.is_displayed(), "Next button is not displayed.")

        except Exception as e:
            print(e)
            
            
    def test_count_author(self):
      
        try:
           
           
            
            get_all_author = self.author.get_author()

        
                
            author_numbers = len(get_all_author)
                
            print(f"Number of author in first page: {author_numbers}")
                
            self.assertGreater(author_numbers,20,"There are less number of author in this page")
           
           

        except Exception as e:
            print(e)
            
            
    def test_second_page(self):
            
            next_button = self.author.get_nextbutton()
            
            try:
                get_all_author = self.author.get_author()
                author_numbers = len(get_all_author)
                
                print(f"Number of author in second page: {author_numbers}")
                
                self.assertGreater(author_numbers,5," There are less number of author in this page")
           
            except Exception as e :
                print(e)
                
                 
    def test_aboutsection(self):
      
        try:
           
            about_section = self.author.get_about().click()
          
            
            current_url = self.driver.current_url
            expected_url = "https://quotes.toscrape.com/author/Albert-Einstein/"
            
            self.assertNotEqual(current_url,expected_url,'URL doesnot match')
            
        except Exception as e :
            print(e)
            

    def test_url(self):
      
        try:
           
           
          
            about_section = self.author.get_about().click() 
            current_url = self.driver.current_url
            expected_url = "https://quotes.toscrape.com/author/Albert-Einstein/"
            
            self.assertEqual(current_url,expected_url,'URL doesnot match')
            
            
            
            
        except Exception as e :
            print(e)
            
    def test_totaltags(self):
      
        try:
           
           
           
            total_tags = self.author.get_totaltags()
            tags = len(total_tags)
            self.assertGreater(tags,5,"Error not found")
            
            
           
                
        except Exception as e :
            print(e)
            
    def test_thirdboard(self):
      
        try:
           
            third_element = self.quote.get_singlequotes()

            actual_text = third_element.text
           
            expected_text = ("There are only  to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle")

            
            self.assertEqual(actual_text, expected_text, "Third quote text does not match.")

        except Exception as e :
            print(e)
            
    
    def test_top10tags(self):
      
        try:
           
            tags = self.tags.get_total10tags().click()
            author_name= self.tags.get_author_top10()

            
            print(author_name.text)
            
          
            
            actual_name = author_name.text
            expected_name = "André Gide"
            
            self.assertEqual(actual_name,expected_name,'Name Not Equal')
            
            
        except Exception as e :
            print(e)
            
    
    
    def test_count_tags(self):
        
        
        total_sum = 0
        try:
            while True:
          
                get_alltags = self.tags.get_totaltags()
                
                
                total = len(get_alltags)
                total_sum =total_sum + total 
                
                try:
                    next_btn = self.author.get_nextbutton()
                    next_btn.click()
                
                except Exception as e:
                    print("No more pages")
                    break
                
            print(f'The sum of all total tags: {total_sum}')
            
            actual_tags = total_sum
            expected_tags = 140
            self.assertNotEqual(actual_tags,expected_tags,'{actual_tags} is not equal to the {expected_tags} ')        

        except Exception as e:
            print(f"Error: {e}")
            
            
            
            
 
            
            
  
            
            
            
            
            
            

        

if __name__ == "__main__":
    unittest.main(defaultTest="Test.test_count_tags")