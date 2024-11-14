# forgot_password_page.py
from selenium.webdriver.common.by import By
from POM.base_page import BasePage

class ForgotPasswordPage(BasePage):
    enterName = "input[placeholder='Name']"
    enterEmail = "input[placeholder='Email']"
    enterPhone = "input[placeholder='Phone Number']"
    resetPass = "//button[@class='reset-pwd-btn']"
    infoMsg = "#container > div.form-container.sign-up-container > form > p"
    clickLogin = "//button[@class='go-to-login-btn']"


    def enter_name(self, name):
        self.enter_text(By.CSS_SELECTOR, self.enterName, name)

    def enter_email(self, email):
        self.enter_text(By.CSS_SELECTOR,self.enterEmail , email)

    def enter_phone(self, phone):
        self.enter_text(By.CSS_SELECTOR,self.enterPhone , phone)

    def click_reset_password(self):
        return self.click(By.XPATH, self.resetPass)

    def get_info_message(self):
        return self.find_element(By.CSS_SELECTOR, self.infoMsg).text

    def click_go_to_login(self):
        self.click(By.XPATH, self.clickLogin)
