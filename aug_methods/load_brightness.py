from PyQt5.QtWidgets import *
from brightness import Ui_FormBrightness
from PyQt5.QtCore import pyqtSignal
import numpy as np
import cv2
from PyQt5.QtGui import QImage
from PyQt5 import QtGui

class BrightPage(QWidget):
    the_signal = pyqtSignal(int, str, str)
    def __init__(self):
        super().__init__()
        self.brightpage = Ui_FormBrightness()
        self.brightpage.setupUi(self)

        self.brightpage.pushButton.clicked.connect(self.Confirmed)
        self.brightpage.horizontalSlider_brightness.valueChanged.connect(self.UpdatePreview)

    def Confirmed(self):
        parameter1 = self.brightpage.horizontalSlider_brightness.value()
        parameter2 = self.brightpage.checkBox_lighten.isChecked()
        parameter3 = self.brightpage.checkBox_darken.isChecked()
        self.the_signal.emit(parameter1, str(parameter2), str(parameter3))
        self.close()

    def UpdatePreview(self):

        preview_img = cv2.imread("aug_methods/img.png")
        value = self.brightpage.horizontalSlider_brightness.value()
        param1 = 1.0 + (value / 100)
        param2 = 1.0 - (value / 100)

        preview_img1 = np.clip(preview_img * param1, 0, 255).astype(np.uint8)
        preview_img1 = cv2.cvtColor(preview_img1, cv2.COLOR_BGR2RGB)
        preview_img2 = np.clip(preview_img * param2, 0, 255).astype(np.uint8)
        preview_img2 = cv2.cvtColor(preview_img2, cv2.COLOR_BGR2RGB)

        height, width, channel = preview_img1.shape
        bytes_per_line = 3 * width
        q_image1 = QImage(preview_img1.data, width, height, bytes_per_line, QImage.Format_RGB888)
        q_image2 = QImage(preview_img2.data, width, height, bytes_per_line, QImage.Format_RGB888)

        self.brightpage.label_img.setPixmap(QtGui.QPixmap(q_image1))
        self.brightpage.label_img_2.setPixmap(QtGui.QPixmap(q_image2))









        
