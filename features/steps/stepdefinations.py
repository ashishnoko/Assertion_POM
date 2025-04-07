from behave import given, when, then
import time
from features.steps.utils.browser_manager import BrowserManager
from features.pages.login import Login_Page

@given("the browser is open")
def step_open_browser(context):
    context.driver = BrowserManager.start_browser()
    context.login_page = Login_Page(context.driver)

   

@when("the user navigates to the login page")
def step_navigate_to_login(context):
    context.driver.get("https://quotes.toscrape.com/")
    #context.login_page = Login_Page(context.driver)
    
    
    
    context.login_page.click_login()
    
    

@when("enters valid credentials")
def step_enter_credentials(context):
    context.login_page.enter_username("Admin")
    context.login_page.enter_password("Admin")
    context.login_page.login_btn()

@then("the user should be redirected to the homepage")
def step_verify_dashboard(context):
    assert "https://quotes.toscrape.com" in context.driver.current_url