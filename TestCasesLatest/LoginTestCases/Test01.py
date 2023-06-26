from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import pyautogui
from PIL import Image


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


class Test_01_Login:
    homeURL = "https://www.saucedemo.com/"

    def test_SuccessfullLogin(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(10)

        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
            self.driver.close()

        else:
            myscreen = pyautogui.screenshot()
            myscreen.save('test_01.png')
            self.driver.close()
            assert False
