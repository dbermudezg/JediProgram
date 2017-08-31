"""Moves the browser.

This script moves the firefox browser window around screen using Selenium
"""
from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get('https://misterneutron.com/videoTag/index.html')
driver.maximize_window()
driver.set_window_size(800, 600)
time.sleep(2)
driver.set_window_position(2300, 0)
time.sleep(30)
driver.set_window_position(0, 0)
