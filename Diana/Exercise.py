from selenium import webdriver
import time

class workOnWindow:

        def setUp(self):
                self.browser = webdriver.Firefox()
                self.browser.get('https://misterneutron.com/videoTag/index.html')

        def moveWindow(self, positionX, positionY):
                driver = self.browser
                driver.set_window_position(positionX, positionY)
                time.sleep(15)

        def resizeWindow(self, height, width):
                self.browser.set_window_size(height, width)

        def getSize(self):
                size = self.browser.get_window_size()
                print size


        def tearDown(self):
                self.browser.quit()



