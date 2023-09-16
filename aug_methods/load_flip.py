from PyQt5.QtWidgets import *
from flip import Ui_FormFlip
from PyQt5.QtCore import pyqtSignal
import cv2
from PyQt5.QtGui import QImage
from PyQt5 import QtGui

class FlipPage(QWidget):
    the_signal = pyqtSignal(str,str)
    def __init__(self):
        super().__init__()
        self.flippage = Ui_FormFlip()
        self.flippage.setupUi(self)
        self.flippage.pushButton.clicked.connect(self.Confirmed)
        self.Preview()

    def Confirmed(self):
        parameter1 = self.flippage.checkBox_horizontal.isChecked()
        parameter2 = self.flippage.checkBox_vertical.isChecked()
        self.the_signal.emit(str(parameter1), str(parameter2))
        self.close()

    def Preview(self):
        preview_img = cv2.imread("aug_methods/img.png")

        preview_img1 = cv2.flip(preview_img, 1)
        preview_img1 = cv2.cvtColor(preview_img1, cv2.COLOR_BGR2RGB)
        preview_img2 = cv2.flip(preview_img, 0)
        preview_img2 = cv2.cvtColor(preview_img2, cv2.COLOR_BGR2RGB)

        height, width, channel = preview_img.shape
        bytes_per_line = 3 * width
        q_image1 = QImage(preview_img1.data, width, height, bytes_per_line, QImage.Format_RGB888)
        q_image2 = QImage(preview_img2.data, width, height, bytes_per_line, QImage.Format_RGB888)

        self.flippage.label_img_horizontal.setPixmap(QtGui.QPixmap(q_image1))
        self.flippage.label_img_vertical.setPixmap(QtGui.QPixmap(q_image2)) 