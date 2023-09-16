from PyQt5.QtWidgets import *
from rotate import Ui_FormRotate
from PyQt5.QtCore import pyqtSignal
import cv2
from PyQt5.QtGui import QImage
from PyQt5 import QtGui

class RotatePage(QWidget):
    the_signal = pyqtSignal(str, str, str)
    def __init__(self):
        super().__init__()
        self.rotatepage = Ui_FormRotate()
        self.rotatepage.setupUi(self)

        self.rotatepage.pushButton.clicked.connect(self.Confirmed)
        self.Preview()

    def Confirmed(self):
        parameter1 = self.rotatepage.checkBox_clockwise.isChecked()
        parameter2 = self.rotatepage.checkBox_counter_clockwise.isChecked()
        parameter3 = self.rotatepage.checkBox_upside_down.isChecked()
        self.the_signal.emit(str(parameter1), str(parameter2), str(parameter3))
        self.close()

    def Preview(self):
        preview_img = cv2.imread("aug_methods/img.png")

        preview_img1 = cv2.rotate(preview_img, cv2.ROTATE_90_CLOCKWISE)
        preview_img1 = cv2.cvtColor(preview_img1, cv2.COLOR_BGR2RGB)

        preview_img2 = cv2.rotate(preview_img, cv2.ROTATE_180)
        preview_img2 = cv2.cvtColor(preview_img2, cv2.COLOR_BGR2RGB)

        preview_img3 = cv2.rotate(preview_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        preview_img3 = cv2.cvtColor(preview_img3, cv2.COLOR_BGR2RGB)

        height, width, channel = preview_img.shape
        bytes_per_line = 3 * width
        q_image1 = QImage(preview_img1.data, width, height, bytes_per_line, QImage.Format_RGB888)
        q_image2 = QImage(preview_img2.data, width, height, bytes_per_line, QImage.Format_RGB888)
        q_image3 = QImage(preview_img3.data, width, height, bytes_per_line, QImage.Format_RGB888)

        self.rotatepage.label_img_clockwise.setPixmap(QtGui.QPixmap(q_image1))
        self.rotatepage.label_img_upside_down.setPixmap(QtGui.QPixmap(q_image2)) 
        self.rotatepage.label_img_counter_clockwise.setPixmap(QtGui.QPixmap(q_image3)) 