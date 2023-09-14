# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brightness.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormBrightness(object):
    def setupUi(self, FormBrightness):
        FormBrightness.setObjectName("FormBrightness")
        FormBrightness.resize(564, 500)
        self.horizontalSlider_brightness = QtWidgets.QSlider(FormBrightness)
        self.horizontalSlider_brightness.setGeometry(QtCore.QRect(140, 340, 331, 16))
        self.horizontalSlider_brightness.setMaximum(100)
        self.horizontalSlider_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_brightness.setObjectName("horizontalSlider_brightness")
        self.label = QtWidgets.QLabel(FormBrightness)
        self.label.setGeometry(QtCore.QRect(50, 340, 81, 17))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(FormBrightness)
        self.pushButton.setGeometry(QtCore.QRect(260, 400, 71, 61))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(FormBrightness)
        self.label_3.setGeometry(QtCore.QRect(500, 340, 31, 17))
        self.label_3.setObjectName("label_3")
        self.label_img = QtWidgets.QLabel(FormBrightness)
        self.label_img.setGeometry(QtCore.QRect(150, 30, 261, 271))
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap("img.png"))
        self.label_img.setObjectName("label_img")

        self.retranslateUi(FormBrightness)
        self.horizontalSlider_brightness.valueChanged['int'].connect(self.label_3.setNum)
        QtCore.QMetaObject.connectSlotsByName(FormBrightness)

    def retranslateUi(self, FormBrightness):
        _translate = QtCore.QCoreApplication.translate
        FormBrightness.setWindowTitle(_translate("FormBrightness", "Brightness"))
        self.label.setText(_translate("FormBrightness", "Brightness"))
        self.pushButton.setText(_translate("FormBrightness", "OK"))
        self.label_3.setText(_translate("FormBrightness", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormBrightness = QtWidgets.QWidget()
    ui = Ui_FormBrightness()
    ui.setupUi(FormBrightness)
    FormBrightness.show()
    sys.exit(app.exec_())
