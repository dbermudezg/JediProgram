"""Moves the browser."""
from selenium import webdriver


class Window:
    """Common base class for control the window."""

    def __init__(self, height=400, width=300,
                 pos_x=0, pos_y=0, browser='Firefox'):
        """Construct the class."""
        self.height = height
        self.width = width
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.driver = webdriver.Firefox()
        """{
            'chrome': webdriver.Chrome(),
            'firefox': webdriver.Firefox(),
            'safari': webdriver.Safari(),
            'explorer': webdriver.Ie(),
            'opera': webdriver.Opera()
        }.get(browser, webdriver.Firefox())"""

    def open_new_window(self):
        """Open the window."""
        self.driver.get('http://google.com/')
        self.driver.maximize_window()

    def move_window(self, pos_x, pos_y):
        """Move the window to indicated position."""
        self.driver.set_window_position(pos_x, pos_y)

    def resize_window(self, height, width):
        """Resize the window to given values."""
        self.driver.set_window_size(height, width)

    def print_window_dimension(self):
        """Print in console the dimension os the window."""
        print(self.driver.get_window_size())

    def close_window(self):
        """Close the window and driver."""
        self.driver.close()
