from PyQt5.QtWidgets import *
from flip import Ui_FormFlip

class FlipPage(QWidget):
    def __init__(self):
        super().__init__()
        self.flippage = Ui_FormFlip()
        self.flippage.setupUi(self)
