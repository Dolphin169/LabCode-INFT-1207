# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLab4KevinOwen():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_lab4KevinOwen(self):
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    self.driver.set_window_size(550, 696)
    # VALID WOMEN VALUES
    self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").clear()
    self.driver.find_element(By.NAME, "cage").send_keys("40")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("100")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.NAME, "cheightmeter").clear()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("189")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.NAME, "cneckmeter").clear()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("57")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.NAME, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("98")
    self.driver.find_element(By.ID, "chipmeter").click()
    self.driver.find_element(By.NAME, "chipmeter").clear()
    self.driver.find_element(By.ID, "chipmeter").send_keys("100")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 23.0%"
    # VALID MEN VALUES
    self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(1) > .rbmark").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").clear()
    self.driver.find_element(By.NAME, "cage").send_keys("15")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("220")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.NAME, "cheightmeter").clear()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("90")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.NAME, "cneckmeter").clear()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("18")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.NAME, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("100")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font > b").text == "Body Fat: 60.7%"
    # INVALID WOMEN AGE
    self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").clear()
    self.driver.find_element(By.NAME, "cage").send_keys("abc")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").clear()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("2")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.NAME, "cheightmeter").clear()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("9")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.NAME, "cneckmeter").clear()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("180")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.NAME, "cwaistmeter").clear()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("95")
    self.driver.find_element(By.ID, "chipmeter").click()
    self.driver.find_element(By.NAME, "chipmeter").clear()
    self.driver.find_element(By.ID, "chipmeter").send_keys("74")
    self.driver.find_element(By.NAME, "x").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "font").text == "Please provide a positive age."
  
