# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hue.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormHue(object):
    def setupUi(self, FormHue):
        FormHue.setObjectName("FormHue")
        FormHue.resize(669, 494)
        self.label = QtWidgets.QLabel(FormHue)
        self.label.setGeometry(QtCore.QRect(150, 350, 81, 17))
        self.label.setObjectName("label")
        self.horizontalSlider_hue = QtWidgets.QSlider(FormHue)
        self.horizontalSlider_hue.setGeometry(QtCore.QRect(200, 350, 271, 16))
        self.horizontalSlider_hue.setMaximum(180)
        self.horizontalSlider_hue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_hue.setObjectName("horizontalSlider_hue")
        self.label_3 = QtWidgets.QLabel(FormHue)
        self.label_3.setGeometry(QtCore.QRect(500, 350, 31, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(FormHue)
        self.pushButton.setGeometry(QtCore.QRect(290, 390, 71, 61))
        self.pushButton.setObjectName("pushButton")
        self.label_img_dec = QtWidgets.QLabel(FormHue)
        self.label_img_dec.setGeometry(QtCore.QRect(60, 50, 261, 271))
        self.label_img_dec.setText("")
        self.label_img_dec.setPixmap(QtGui.QPixmap("img.png"))
        self.label_img_dec.setObjectName("label_img_dec")
        self.label_img_inc = QtWidgets.QLabel(FormHue)
        self.label_img_inc.setGeometry(QtCore.QRect(350, 50, 261, 271))
        self.label_img_inc.setText("")
        self.label_img_inc.setPixmap(QtGui.QPixmap("img.png"))
        self.label_img_inc.setObjectName("label_img_inc")
        self.label_2 = QtWidgets.QLabel(FormHue)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 21, 17))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(FormHue)
        self.label_4.setGeometry(QtCore.QRect(470, 30, 21, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(FormHue)
        self.horizontalSlider_hue.valueChanged['int'].connect(self.label_3.setNum) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(FormHue)

    def retranslateUi(self, FormHue):
        _translate = QtCore.QCoreApplication.translate
        FormHue.setWindowTitle(_translate("FormHue", "Hue"))
        self.label.setText(_translate("FormHue", "Hue"))
        self.label_3.setText(_translate("FormHue", "0"))
        self.pushButton.setText(_translate("FormHue", "OK"))
        self.label_2.setText(_translate("FormHue", "-"))
        self.label_4.setText(_translate("FormHue", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormHue = QtWidgets.QWidget()
    ui = Ui_FormHue()
    ui.setupUi(FormHue)
    FormHue.show()
    sys.exit(app.exec_())
