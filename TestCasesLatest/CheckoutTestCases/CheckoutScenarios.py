from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import pyautogui
from selenium.webdriver.support.select import Select


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


class Test_05_CheckoutScenarios:
    homeURL = "https://www.saucedemo.com/"

    def test_MandatoryFieldCheck(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='cancel']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(3)
        act_ErrorMsg = self.driver.find_element(By.XPATH, "//h3")
        assert act_ErrorMsg.text == 'Error: First Name is required'
        myscreen = pyautogui.screenshot()
        myscreen.save('test_ErrorMsgMandatoryField.png')
        self.driver.close()

    def test_CheckOutPageAndFinish(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Anup")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Deshpande")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("411038")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[@class='summary_info']").is_displayed()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='cancel']").click()
        time.sleep(3)
        myscreen = pyautogui.screenshot()
        myscreen.save('test_Cartpage.png')
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Anup")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Deshpande")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("411038")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Finish')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//h2").is_displayed()
        myscreen = pyautogui.screenshot()
        myscreen.save('test_Lastpage.png')
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Back Home')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[contains(text(),'Swag Labs')]").is_displayed()
        time.sleep(3)
        myscreen = pyautogui.screenshot()
        myscreen.save('test_Lastpage.png')
        self.driver.close()

    def test_BackToProducts(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Anup")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Deshpande")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("411038")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Sauce Labs Backpack')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
        time.sleep(3)
        myscreen = pyautogui.screenshot()
        myscreen.save('test_BackForth.png')
        self.driver.close()