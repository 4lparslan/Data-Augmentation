from PyQt5.QtWidgets import *
from load_page1 import Page1

app = QApplication([])

screen = app.primaryScreen()
screen_geometry = screen.geometry()
screen_width, screen_height = screen_geometry.width(), screen_geometry.height()

win = Page1([screen_width, screen_height])
win.show()
app.exec_()
