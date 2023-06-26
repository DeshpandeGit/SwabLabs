from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import pyautogui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture()
def setupEdge():
    driver = webdriver.Edge()
    return driver


@pytest.fixture()
def setupFirefox():
    driver = webdriver.Firefox()
    return driver


class Test_03_PasswordMaskingAndDiffBroswer:
    homeURL = "https://www.saucedemo.com/"

    def test_PasswordMasking(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(5)
        myscreen = pyautogui.screenshot()
        myscreen.save('test_PassMask.png')
        self.driver.close()


    def test_EdgeLogin(self, setupEdge):
        self.driver = setupEdge
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            myscreen = pyautogui.screenshot()
            myscreen.save('test_EdgeLogin.png')
            self.driver.close()
            assert True

        else:
            myscreen = pyautogui.screenshot()
            myscreen.save('test_EdgeLogin.png')
            self.driver.close()
            assert False


    def test_FirefoxLogin(self, setupFirefox):
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        self.driver = setupFirefox
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            myscreen = pyautogui.screenshot()
            myscreen.save('test_FFLogin.png')
            self.driver.close()
            assert True

        else:
            myscreen = pyautogui.screenshot()
            myscreen.save('test_FFLogin.png')
            self.driver.close()
            assert False