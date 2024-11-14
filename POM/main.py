import re
import time
from linecache import cache

from exceptiongroup import catch
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from POM.forgot_password import ForgotPasswordPage
from POM.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/locatorspractice/")
driver.implicitly_wait(20)
# Instantiate LoginPage
login_page = LoginPage(driver)

# Login Page actions
username = input("Enter your name: ")
password = input("Enter your password: ")

login_page.enter_username(username)
login_page.enter_password(password)
login_page.click_login()

# Check for error message and navigate to Forgot Password if error appears
if login_page.get_error_message():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")

    login_page.click_forgot_password()
    # time.sleep(200)

    # Forgot Password Page actions
    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.enter_name(name)
    forgot_password_page.enter_email(email)
    forgot_password_page.enter_phone(phone)
    time.sleep(1)
    forgot_password_page.click_reset_password()
    resetName = input("Enter your new user name: ")

    # Retrieve temporary password and use it to log in
    new_error_message = forgot_password_page.get_info_message()


    match = re.search(r"'(.*)'", new_error_message)

    if match:
        temporary_password = match.group(1)
        print("Extracted Password:", temporary_password)
        try:
            forgot_password_page.click_go_to_login()
            driver.implicitly_wait(5)
            # time.sleep(5)
            # WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, "overlay-panel"))
            # )
        except Exception as e:
            print(f"An unexpected exception occurred: {str(e)}")

        # Re-login with temporary password

        login_page.enter_username(resetName)
        login_page.enter_password(temporary_password)
        driver.implicitly_wait(5)
        login_page.click_login()
        expected_title = "Rahul Shetty Academy - Login page"
        actual_title = driver.title  # Retrieves the current page title
        assert expected_title == actual_title, f"Expected title '{expected_title}', but got '{actual_title}'"
        print(actual_title, "is equal", expected_title,)

driver.quit()
