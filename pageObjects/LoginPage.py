from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage


class LoginPage(BasePage):
    # Login Page
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[text()='Log in']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver
        #super().__init__(driver)  # driver calling from basepage

    def setUserName(self, username):
        self.clear_text(self.textbox_username_id)
        self.send_value_to_element(self.textbox_username_id, username)
        # self.driver.find_element(By.ID, self.textbox_username_id).clear()
       # self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.clear_text(self.textbox_password_id)
        self.send_value_to_element(self.textbox_password_id, password)
        # self.driver.find_element(By.ID, self.textbox_password_id).clear()
        # self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.click_the_element(self.button_login_xpath)
        #self.driver.find_element(By.XPATH, self.button_login_xpath).click()

