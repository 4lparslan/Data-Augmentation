from PyQt5.QtWidgets import *
from hue import Ui_FormHue
from PyQt5.QtCore import pyqtSignal
import numpy as np
import cv2
from PyQt5.QtGui import QImage
from PyQt5 import QtGui

class HuePage(QWidget):
    the_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.huepage = Ui_FormHue()
        self.huepage.setupUi(self)

        self.huepage.pushButton.clicked.connect(self.Confirmed)
        self.huepage.horizontalSlider_hue.valueChanged.connect(self.UpdatePreview)

    def Confirmed(self):
        parameter = self.huepage.horizontalSlider_hue.value()
        self.the_signal.emit(parameter)
        self.close()

    def UpdatePreview(self):
        preview_img = cv2.imread("aug_methods/img.png")
        param = self.huepage.horizontalSlider_hue.value()
        preview_img = cv2.cvtColor(preview_img, cv2.COLOR_BGR2HSV)
        preview_img[:,:,0] = np.clip(preview_img[:,:,0] + param, 0, 255) % 180
        preview_img = cv2.cvtColor(preview_img, cv2.COLOR_HSV2RGB)

        height, width, channel = preview_img.shape
        bytes_per_line = 3 * width
        q_image = QImage(preview_img.data, width, height, bytes_per_line, QImage.Format_RGB888)

        self.huepage.label_img.setPixmap(QtGui.QPixmap(q_image))