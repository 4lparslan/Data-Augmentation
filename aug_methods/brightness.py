
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
        FormBrightness.resize(613, 529)
        self.horizontalSlider_brightness = QtWidgets.QSlider(FormBrightness)
        self.horizontalSlider_brightness.setGeometry(QtCore.QRect(160, 370, 331, 16))
        self.horizontalSlider_brightness.setMaximum(100)
        self.horizontalSlider_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_brightness.setObjectName("horizontalSlider_brightness")
        self.label = QtWidgets.QLabel(FormBrightness)
        self.label.setGeometry(QtCore.QRect(60, 366, 81, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(FormBrightness)
        self.pushButton.setGeometry(QtCore.QRect(280, 430, 71, 61))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(FormBrightness)
        self.label_3.setGeometry(QtCore.QRect(530, 370, 31, 17))
        self.label_3.setObjectName("label_3")
        self.label_img = QtWidgets.QLabel(FormBrightness)
        self.label_img.setGeometry(QtCore.QRect(40, 30, 261, 271))
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap("aug_methods/img.png"))
        self.label_img.setObjectName("label_img")
        self.label_img_2 = QtWidgets.QLabel(FormBrightness)
        self.label_img_2.setGeometry(QtCore.QRect(320, 30, 261, 271))
        self.label_img_2.setText("")
        self.label_img_2.setPixmap(QtGui.QPixmap("aug_methods/img.png"))
        self.label_img_2.setObjectName("label_img_2")
        self.checkBox_lighten = QtWidgets.QCheckBox(FormBrightness)
        self.checkBox_lighten.setGeometry(QtCore.QRect(120, 310, 92, 23))
        self.checkBox_lighten.setObjectName("checkBox_lighten")
        self.checkBox_darken = QtWidgets.QCheckBox(FormBrightness)
        self.checkBox_darken.setGeometry(QtCore.QRect(410, 310, 92, 23))
        self.checkBox_darken.setObjectName("checkBox_darken")
        self.label_2 = QtWidgets.QLabel(FormBrightness)
        self.label_2.setGeometry(QtCore.QRect(510, 370, 21, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(FormBrightness)
        self.horizontalSlider_brightness.valueChanged['int'].connect(self.label_3.setNum)
        QtCore.QMetaObject.connectSlotsByName(FormBrightness)

    def retranslateUi(self, FormBrightness):
        _translate = QtCore.QCoreApplication.translate
        FormBrightness.setWindowTitle(_translate("FormBrightness", "Brightness"))
        self.label.setText(_translate("FormBrightness", "Brightness"))
        self.pushButton.setText(_translate("FormBrightness", "OK"))
        self.label_3.setText(_translate("FormBrightness", "0"))
        self.checkBox_lighten.setText(_translate("FormBrightness", "Lighten"))
        self.checkBox_darken.setText(_translate("FormBrightness", "Darken"))
        self.label_2.setText(_translate("FormBrightness", "%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormBrightness = QtWidgets.QWidget()
    ui = Ui_FormBrightness()
    ui.setupUi(FormBrightness)
    FormBrightness.show()
    sys.exit(app.exec_())
