from PyQt5.QtWidgets import *
from grayscale import Ui_FormGrayscale
from PyQt5.QtCore import pyqtSignal
import cv2
from PyQt5.QtGui import QImage
from PyQt5 import QtGui

class GrayscalePage(QWidget):
    the_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.grayscalepage = Ui_FormGrayscale()
        self.grayscalepage.setupUi(self)

        self.grayscalepage.pushButton.clicked.connect(self.Confirmed)
        self.Preview()

    def Confirmed(self):
        parameter = self.grayscalepage.checkBox.isChecked()
        self.the_signal.emit(str(parameter))
        self.close()

    def Preview(self):
        preview_img = cv2.imread("aug_methods/img.png")

        preview_img = cv2.cvtColor(preview_img, cv2.COLOR_BGR2GRAY)

        preview_img = cv2.cvtColor(preview_img, cv2.COLOR_BGR2RGB)

        height, width, channel = preview_img.shape
        bytes_per_line = 3 * width
        q_image = QImage(preview_img.data, width, height, bytes_per_line, QImage.Format_RGB888)

        self.grayscalepage.label_img.setPixmap(QtGui.QPixmap(q_image))