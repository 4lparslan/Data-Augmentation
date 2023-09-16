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
        FormSaturation.resize(495, 453)
        self.pushButton = QtWidgets.QPushButton(FormSaturation)
        self.pushButton.setGeometry(QtCore.QRect(200, 390, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(FormSaturation)
        self.label.setGeometry(QtCore.QRect(440, 340, 31, 17))
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(FormSaturation)
        self.horizontalSlider.setGeometry(QtCore.QRect(130, 340, 281, 16))
        self.horizontalSlider.setMaximum(99)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_2 = QtWidgets.QLabel(FormSaturation)
        self.label_2.setGeometry(QtCore.QRect(40, 340, 81, 17))
        self.label_2.setObjectName("label_2")
        self.label_img = QtWidgets.QLabel(FormSaturation)
        self.label_img.setGeometry(QtCore.QRect(120, 40, 261, 271))
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap("aug_methods/img.png"))
        self.label_img.setObjectName("label_img")

        self.retranslateUi(FormSaturation)
        self.horizontalSlider.valueChanged['int'].connect(self.label.setNum)
        QtCore.QMetaObject.connectSlotsByName(FormSaturation)

    def retranslateUi(self, FormSaturation):
        _translate = QtCore.QCoreApplication.translate
        FormSaturation.setWindowTitle(_translate("FormSaturation", "Saturation"))
        self.pushButton.setText(_translate("FormSaturation", "OK"))
        self.label.setText(_translate("FormSaturation", "0"))
        self.label_2.setText(_translate("FormSaturation", "Saturation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSaturation = QtWidgets.QWidget()
    ui = Ui_FormSaturation()
    ui.setupUi(FormSaturation)
    FormSaturation.show()
    sys.exit(app.exec_())
