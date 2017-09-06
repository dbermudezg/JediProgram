"""This script does the following.

1. Get the actual size of the window
2. Moves the window out of the sight
3. Redimention the size of the window being unfocused
4. Get the actual size of the window
5. Moves the window to be visible again(focus it)
6. Close the driver
"""
from window_control import Window
import time


window = Window()
window.open_new_window()
window.move_window(0, 0)
window.print_window_dimension()
time.sleep(3)
window.move_window(2000, 4000)
time.sleep(3)
window.resize_window(500, 300)
window.print_window_dimension()
time.sleep(3)
window.move_window(0, 0)
time.sleep(3)
window.close_window()
