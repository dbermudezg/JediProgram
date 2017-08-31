"""Moves the browser.

This script moves the firefox browser window around screen using Selenium
"""
from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get('http://google.com/')
print(driver.get_window_size())
driver.maximize_window()
driver.set_window_position(200, 200)
print(driver.get_window_position())
print("       ")
time.sleep(2)
driver.set_window_size(300, 300)
time.sleep(2)
pos_x = 0
pos_y = 0

for i in range(9):
    driver.set_window_position(pos_x, pos_y)
    print("Posicion de i" + str(i))
    print(driver.get_window_position())
    time.sleep(1)
    if (pos_x < 70 and (i+1) % 2 != 0):
        pos_x = 800
    elif (pos_x > 70 and (i+1) % 2 != 0):
        pos_x = 0
    if (pos_y < 40 and (i+1) % 2 == 0):
        pos_y = 600
    elif (pos_y > 40 and (i+1) % 2 == 0):
        pos_y = 0
time.sleep(1)
driver.set_window_position(1200, 1000)
time.sleep(3)
driver.set_window_position(0, 0)
driver.maximize_window()
