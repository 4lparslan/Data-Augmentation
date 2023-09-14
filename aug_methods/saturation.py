# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saturation.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormSaturation(object):
    def setupUi(self, FormSaturation):
        FormSaturation.setObjectName("FormSaturation")
        FormSaturation.resize(650, 453)
        self.pushButton = QtWidgets.QPushButton(FormSaturation)
        self.pushButton.setGeometry(QtCore.QRect(280, 390, 89, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(FormSaturation)
        self.label.setGeometry(QtCore.QRect(500, 340, 31, 17))
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(FormSaturation)
        self.horizontalSlider.setGeometry(QtCore.QRect(190, 340, 281, 16))
        self.horizontalSlider.setMaximum(99)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_2 = QtWidgets.QLabel(FormSaturation)
        self.label_2.setGeometry(QtCore.QRect(100, 340, 81, 17))
        self.label_2.setObjectName("label_2")
        self.label_img_inc = QtWidgets.QLabel(FormSaturation)
        self.label_img_inc.setGeometry(QtCore.QRect(340, 40, 261, 271))
        self.label_img_inc.setText("")
        self.label_img_inc.setPixmap(QtGui.QPixmap("img.png"))
        self.label_img_inc.setObjectName("label_img_inc")
        self.label_img_dec = QtWidgets.QLabel(FormSaturation)
        self.label_img_dec.setGeometry(QtCore.QRect(50, 40, 261, 271))
        self.label_img_dec.setText("")
        self.label_img_dec.setPixmap(QtGui.QPixmap("img.png"))
        self.label_img_dec.setObjectName("label_img_dec")
        self.label_3 = QtWidgets.QLabel(FormSaturation)
        self.label_3.setGeometry(QtCore.QRect(170, 20, 21, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FormSaturation)
        self.label_4.setGeometry(QtCore.QRect(460, 20, 21, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(FormSaturation)
        self.horizontalSlider.valueChanged['int'].connect(self.label.setNum)
        QtCore.QMetaObject.connectSlotsByName(FormSaturation)

    def retranslateUi(self, FormSaturation):
        _translate = QtCore.QCoreApplication.translate
        FormSaturation.setWindowTitle(_translate("FormSaturation", "Saturation"))
        self.pushButton.setText(_translate("FormSaturation", "OK"))
        self.label.setText(_translate("FormSaturation", "0"))
        self.label_2.setText(_translate("FormSaturation", "Saturation"))
        self.label_3.setText(_translate("FormSaturation", "-"))
        self.label_4.setText(_translate("FormSaturation", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSaturation = QtWidgets.QWidget()
    ui = Ui_FormSaturation()
    ui.setupUi(FormSaturation)
    FormSaturation.show()
    sys.exit(app.exec_())
