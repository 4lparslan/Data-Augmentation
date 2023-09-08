from PyQt5.QtWidgets import *
from load_page1 import Page1

app = QApplication([])
win = Page1()
win.show()
app.exec_()