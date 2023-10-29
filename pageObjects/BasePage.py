from selenium.webdriver.common.by import By


class BasePage:
    def __int__(self, driver):
        self.driver = driver

    def clear_text(self, element):
        self.driver.find_element(By.ID, element).clear()

    def send_value_to_element(self, element, value):
        self.driver.find_element(By.ID, element).send_keys(value)

    def click_the_element(self, element):
        self.driver.find_element(By.XPATH, element).click()