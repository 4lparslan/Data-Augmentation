# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hue.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormHue(object):
    def setupUi(self, FormHue):
        FormHue.setObjectName("FormHue")
        FormHue.resize(421, 482)
        self.label = QtWidgets.QLabel(FormHue)
        self.label.setGeometry(QtCore.QRect(30, 340, 81, 17))
        self.label.setObjectName("label")
        self.horizontalSlider_hue = QtWidgets.QSlider(FormHue)
        self.horizontalSlider_hue.setGeometry(QtCore.QRect(80, 340, 271, 16))
        self.horizontalSlider_hue.setMaximum(179)
        self.horizontalSlider_hue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_hue.setObjectName("horizontalSlider_hue")
        self.label_3 = QtWidgets.QLabel(FormHue)
        self.label_3.setGeometry(QtCore.QRect(380, 340, 31, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(FormHue)
        self.pushButton.setGeometry(QtCore.QRect(170, 380, 71, 61))
        self.pushButton.setObjectName("pushButton")
        self.label_img = QtWidgets.QLabel(FormHue)
        self.label_img.setGeometry(QtCore.QRect(90, 40, 261, 271))
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap("aug_methods/img.png"))
        self.label_img.setObjectName("label_img")

        self.retranslateUi(FormHue)
        self.horizontalSlider_hue.valueChanged['int'].connect(self.label_3.setNum)
        QtCore.QMetaObject.connectSlotsByName(FormHue)

    def retranslateUi(self, FormHue):
        _translate = QtCore.QCoreApplication.translate
        FormHue.setWindowTitle(_translate("FormHue", "Hue"))
        self.label.setText(_translate("FormHue", "Hue"))
        self.label_3.setText(_translate("FormHue", "0"))
        self.pushButton.setText(_translate("FormHue", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormHue = QtWidgets.QWidget()
    ui = Ui_FormHue()
    ui.setupUi(FormHue)
    FormHue.show()
    sys.exit(app.exec_())
