from PyQt5.QtWidgets import *
from page3 import Ui_add_augmentation
from load_page4 import Page4

class Page3(QWidget):
    def __init__(self):
        super().__init__()
        self.p3 = Ui_add_augmentation()
        self.p3.setupUi(self)

        self.p3.pushButton_addaug.clicked.connect(self.showPage4)

        self.page4_run = Page4()

    def showPage4(self):
        self.page4_run.show()