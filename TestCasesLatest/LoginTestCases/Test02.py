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


class Test_02_ValidUsername_InvalidPassword:
    homeURL = "https://www.saucedemo.com/"

    def test_InvalidPassword(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("seet_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        act_ErrorMsg = self.driver.find_element(By.XPATH,"//h3")
        assert act_ErrorMsg.text == 'Epic sadface: Username and password do not match any user in this service'
        myscreen = pyautogui.screenshot()
        myscreen.save('test_InvalidPassword.png')
        self.driver.close()

    def test_InvalidUsername(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("stzzzd_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        act_ErrorMsg = self.driver.find_element(By.XPATH,"//h3")
        assert act_ErrorMsg.text == 'Epic sadface: Username and password do not match any user in this service'
        myscreen = pyautogui.screenshot()
        myscreen.save('test_InvalidUsername.png')
        self.driver.close()

# Username and passowrd blank and user clicks on Login button

    def test_blankLogin(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        act_ErrorMsg = self.driver.find_element(By.XPATH,"//h3")
        assert act_ErrorMsg.text == 'Epic sadface: Username is required'
        myscreen = pyautogui.screenshot()
        myscreen.save('test_blankLogin.png')
        self.driver.close()


# Locked Out user test expected to show error message

    def test_LockedOutUser(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        act_ErrorMsg = self.driver.find_element(By.XPATH,"//h3")
        assert act_ErrorMsg.text == 'Epic sadface: Sorry, this user has been locked out.'
        myscreen = pyautogui.screenshot()
        myscreen.save('test_LockedoutUser.png')
        self.driver.close()