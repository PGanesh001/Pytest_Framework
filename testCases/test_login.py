import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.BaseTest import BaseTest
from utilites.read_csv_testdata_file import read_csvfile

@allure.severity(allure.severity_level.NORMAL)
class Test_001_login(BaseTest):

    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_page_title(self):

        exp_page_title = self.driver.title
        if exp_page_title == "Your store. Login":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_verify_page_title", attachment_type=AttachmentType.PNG)
            self.driver.get_screenshot_as_png(
                "C:\\Users\\Admin\\PycharmProjects\\pythonProject1\\ScreenShots" + "test_verify_page_title01.png")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_verify_page_title.png")
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_flow(self):
        data = read_csvfile("C:\\Users\\Admin\\PycharmProjects\\pythonProject1\\TestData\\logindata.csv")

        self.loginpage = LoginPage(self.driver)
        print("time stamp : " + self.generate_time_stamp())
        self.loginpage.setUserName(data.get('userName'))
        self.loginpage.setPassword(data.get('password'))
        self.loginpage.clickLogin()
        exp_home_page_title = self.driver.title
        if exp_home_page_title == "Dashboard / nopCommerce administration1":
            assert True
        else:
            self.driver.get_screenshot_as_png("C:\\Users\\Admin\\PycharmProjects\\pythonProject1\\ScreenShots"+"test_login_flow01.png")
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login_flow.png")
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_verify_reports(self):
        pytest.skip("reports not yet completed..")