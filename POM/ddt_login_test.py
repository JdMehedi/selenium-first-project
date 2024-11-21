import re
import time
import unittest
from ddt import ddt, unpack, data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM.forgot_password import ForgotPasswordPage
from POM.login_page import LoginPage

@ddt
class DDTLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://rahulshettyacademy.com/locatorspractice/")
        self.driver.implicitly_wait(10)
        time.sleep(5)

    @data(
        ("mehedi", "1234567a", "Mehedi Hasan", "mehedi@@gmail.com", "01782314143"),
                ("ashik", "123456b", "Ashiqur Rahman", "jashiq@gmail.com", "01647781717"),
    )
    @unpack
    def testLogin(self, username, password, name, email, phone):
        driver = self.driver
        login_page = LoginPage(driver)

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

        if login_page.get_error_message():
            login_page.click_forgot_password()
            forgot_password_page = ForgotPasswordPage(driver)

            forgot_password_page.enter_name(name)
            forgot_password_page.enter_email(email)
            forgot_password_page.enter_phone(phone)
            time.sleep(5)
            forgot_password_page.click_reset_password()

            new_error_message = forgot_password_page.get_info_message()
            match = re.search(r"'(.*)'", new_error_message)

            if match:
                temporary_password = match.group(1)

                forgot_password_page.click_go_to_login()
                time.sleep(5)

                login_page.enter_username(name)
                login_page.enter_password(temporary_password)
                login_page.click_login()

                expected_title = "Rahul Shetty Academy - Login page"
                actual_title = driver.title
                assert expected_title == actual_title, f"Expected '{expected_title}', but got '{actual_title}'"
                print(f"Login successful: {actual_title}")

    def tearDown(self):
        self.driver.quit()
