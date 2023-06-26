from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import pyautogui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select


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


class Test_02_FilterItems:
    homeURL = "https://www.saucedemo.com/"

    def test_FilterItemsChrome(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        dropdown = Select(self.driver.find_element(By.XPATH,"//select[@class='product_sort_container']"))
        dropdown.select_by_index(1)
        time.sleep(4)
        sle = Select(self.driver.find_element(By.XPATH,"//select"))
        time.sleep(4)
        sle.select_by_index(2)
        time.sleep(4)
        lat = Select(self.driver.find_element(By.XPATH, "//select"))
        time.sleep(4)
        lat.select_by_index(3)
        time.sleep(4)
        myscreen = pyautogui.screenshot()
        myscreen.save('FilterItemsChrome.png')
        self.driver.close()

    def test_FilterItemsEdge(self, setupEdge):
        self.driver = setupEdge
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        dropdown = Select(self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
        dropdown.select_by_index(1)
        time.sleep(4)
        sle = Select(self.driver.find_element(By.XPATH, "//select"))
        time.sleep(4)
        sle.select_by_index(2)
        time.sleep(4)
        lat = Select(self.driver.find_element(By.XPATH, "//select"))
        time.sleep(4)
        lat.select_by_index(3)
        time.sleep(4)
        myscreen = pyautogui.screenshot()
        myscreen.save('FilterItemsEdge.png')
        self.driver.close()

    def test_FilterItemsFirefox(self, setupFirefox):
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
        dropdown = Select(self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
        dropdown.select_by_index(1)
        time.sleep(4)
        sle = Select(self.driver.find_element(By.XPATH, "//select"))
        time.sleep(4)
        sle.select_by_index(2)
        time.sleep(4)
        lat = Select(self.driver.find_element(By.XPATH, "//select"))
        time.sleep(4)
        lat.select_by_index(3)
        time.sleep(4)
        myscreen = pyautogui.screenshot()
        myscreen.save('FilterItemsFF.png')
        self.driver.close()
