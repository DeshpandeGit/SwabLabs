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


class Test_03_AddRemoveItems:
    homeURL = "https://www.saucedemo.com/"

    def test_AddRemoveChrome(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(2)
        Remove = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        assert Remove.text == 'Remove'
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(2)
        myscreen = pyautogui.screenshot()
        myscreen.save('AddRemoveChrome.png')
        self.driver.close()

    def test_AddRemoveEdge(self, setupEdge):
        self.driver = setupEdge
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(2)
        Remove = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        assert Remove.text == 'Remove'
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(2)
        myscreen = pyautogui.screenshot()
        myscreen.save('AddRemoveEdge.png')
        self.driver.close()

    def test_AddRemoveFirefox(self, setupFirefox):
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
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(2)
        Remove = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        assert Remove.text == 'Remove'
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(2)
        myscreen = pyautogui.screenshot()
        myscreen.save('AddRemoveFirefox.png')
        self.driver.close()
