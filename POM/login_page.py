from selenium.webdriver.common.by import By
from POM.base_page import BasePage  # Ensure this path is correct

class LoginPage(BasePage):
    inputUser = "inputUsername"
    inputPassword = "inputPassword"
    # loginButton = "button[type='submit']"
    loginButton = "button[type='submit']"
    err_massage = "p[class='error']"
    frgt_pass = "Forgot your password?"
    ActualTitle = "#root > div > div > div > h1 > strong"

    def enter_username(self, username):
        self.enter_text(By.ID, self.inputUser, username)

    def enter_password(self, password):
        self.enter_text(By.NAME, self.inputPassword, password)

    def click_login(self):
        self.click(By.CSS_SELECTOR, self.loginButton)

    def get_error_message(self):
        return self.find_element(By.CSS_SELECTOR, self.err_massage).text

    def click_forgot_password(self):
        self.click(By.LINK_TEXT, self.frgt_pass)

    def actual_title(self):
        return self.find_element(By.CSS_SELECTOR, self.ActualTitle).text

