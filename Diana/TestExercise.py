#Main to test Exercise.py

from Exercise import workOnWindow

e = workOnWindow()


e.setUp()
e.getSize()
e.moveWindow(1800, 1550)
e.resizeWindow(1920,1080)
e.getSize()
e.moveWindow(0 , 0)
e.tearDown()
