# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_method.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(499, 380)
        self.pushButton_blur = QtWidgets.QPushButton(Form)
        self.pushButton_blur.setGeometry(QtCore.QRect(40, 40, 81, 81))
        self.pushButton_blur.setObjectName("pushButton_blur")
        self.pushButton_noise = QtWidgets.QPushButton(Form)
        self.pushButton_noise.setGeometry(QtCore.QRect(150, 40, 81, 81))
        self.pushButton_noise.setObjectName("pushButton_noise")
        self.pushButton_rotation = QtWidgets.QPushButton(Form)
        self.pushButton_rotation.setGeometry(QtCore.QRect(260, 40, 81, 81))
        self.pushButton_rotation.setObjectName("pushButton_rotation")
        self.pushButton_hue = QtWidgets.QPushButton(Form)
        self.pushButton_hue.setGeometry(QtCore.QRect(370, 260, 81, 81))
        self.pushButton_hue.setObjectName("pushButton_hue")
        self.pushButton_flip = QtWidgets.QPushButton(Form)
        self.pushButton_flip.setGeometry(QtCore.QRect(40, 150, 81, 81))
        self.pushButton_flip.setObjectName("pushButton_flip")
        self.pushButton_brightness = QtWidgets.QPushButton(Form)
        self.pushButton_brightness.setGeometry(QtCore.QRect(260, 150, 81, 81))
        self.pushButton_brightness.setObjectName("pushButton_brightness")
        self.pushButton_saturation = QtWidgets.QPushButton(Form)
        self.pushButton_saturation.setGeometry(QtCore.QRect(370, 150, 81, 81))
        self.pushButton_saturation.setObjectName("pushButton_saturation")
        self.pushButton_shear = QtWidgets.QPushButton(Form)
        self.pushButton_shear.setGeometry(QtCore.QRect(260, 260, 81, 81))
        self.pushButton_shear.setStyleSheet("")
        self.pushButton_shear.setObjectName("pushButton_shear")
        self.pushButton_exposure = QtWidgets.QPushButton(Form)
        self.pushButton_exposure.setGeometry(QtCore.QRect(40, 260, 81, 81))
        self.pushButton_exposure.setStyleSheet("")
        self.pushButton_exposure.setObjectName("pushButton_exposure")
        self.pushButton_grayscale = QtWidgets.QPushButton(Form)
        self.pushButton_grayscale.setGeometry(QtCore.QRect(150, 150, 81, 81))
        self.pushButton_grayscale.setObjectName("pushButton_grayscale")
        self.pushButton_contrast = QtWidgets.QPushButton(Form)
        self.pushButton_contrast.setGeometry(QtCore.QRect(150, 260, 81, 81))
        self.pushButton_contrast.setStyleSheet("")
        self.pushButton_contrast.setObjectName("pushButton_contrast")
        self.pushButton_rotation2 = QtWidgets.QPushButton(Form)
        self.pushButton_rotation2.setGeometry(QtCore.QRect(370, 40, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_rotation2.setFont(font)
        self.pushButton_rotation2.setObjectName("pushButton_rotation2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Select Method"))
        self.pushButton_blur.setText(_translate("Form", "Blur"))
        self.pushButton_noise.setText(_translate("Form", "Noise"))
        self.pushButton_rotation.setText(_translate("Form", "Rotation"))
        self.pushButton_hue.setText(_translate("Form", "Hue"))
        self.pushButton_flip.setText(_translate("Form", "Flip"))
        self.pushButton_brightness.setText(_translate("Form", "Brightness"))
        self.pushButton_saturation.setText(_translate("Form", "Saturation"))
        self.pushButton_shear.setText(_translate("Form", "Shear"))
        self.pushButton_exposure.setText(_translate("Form", "Exposure"))
        self.pushButton_grayscale.setText(_translate("Form", "Grayscale"))
        self.pushButton_contrast.setText(_translate("Form", "Contrast"))
        self.pushButton_rotation2.setText(_translate("Form", "Rotation 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
