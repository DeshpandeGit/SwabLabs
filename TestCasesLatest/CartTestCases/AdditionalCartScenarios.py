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


class Test_04_CartScenarios:
    homeURL = "https://www.saucedemo.com/"

    # added items to cart and verifying correct number is reflected in cart icon and also the cart page
    def test_NumOfCartItemsAdded(self, setup):
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
        myscreen = pyautogui.screenshot()
        myscreen.save('CartIcon.png')
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(4)
        myscreen = pyautogui.screenshot()
        myscreen.save('CartPage.png')
        self.driver.close()

    # Verifying your cart page

    def test_YourCartPage(self, setup):
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
        myscreen = pyautogui.screenshot()
        myscreen.save('CartIcon.png')
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(4)
        myscreen = pyautogui.screenshot()
        myscreen.save('CartPage.png')
        self.driver.find_element(By.XPATH, "//button[@id='continue-shopping']").click()
        time.sleep(4)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(4)
        myscreen = pyautogui.screenshot()
        myscreen.save('UpdatedItemsList.png')
        self.driver.close()

    # User can remove item from your cart page

    def test_CanRemoveItemYourCartPage(self, setup):
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
        myscreen = pyautogui.screenshot()
        myscreen.save('CartIcon.png')
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(4)
        myscreen = pyautogui.screenshot()
        myscreen.save('CartPage.png')
        self.driver.find_element(By.XPATH, "//button[@id='continue-shopping']").click()
        time.sleep(4)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(4)
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(3)
        myscreen = pyautogui.screenshot()
        myscreen.save('UserCanRemove.png')
        self.driver.close()

    # Negative scenario when no items added , view cart page

    def test_CheckOutClickable(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.homeURL)
        time.sleep(6)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(4)
        myscreen = pyautogui.screenshot()
        myscreen.save('ZeroItemCartPage.png')
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
        time.sleep(3)
        myscreen = pyautogui.screenshot()
        myscreen.save('CheckOutClickable.png')
        self.driver.close()
