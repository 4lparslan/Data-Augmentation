# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensitive_rotate.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormSensitiveRotation(object):
    def setupUi(self, FormSensitiveRotation):
        FormSensitiveRotation.setObjectName("FormSensitiveRotation")
        FormSensitiveRotation.resize(651, 563)
        self.horizontalSlider = QtWidgets.QSlider(FormSensitiveRotation)
        self.horizontalSlider.setGeometry(QtCore.QRect(180, 410, 311, 20))
        self.horizontalSlider.setMaximum(45)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton = QtWidgets.QPushButton(FormSensitiveRotation)
        self.pushButton.setGeometry(QtCore.QRect(280, 460, 89, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(FormSensitiveRotation)
        self.label.setGeometry(QtCore.QRect(520, 410, 31, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(FormSensitiveRotation)
        self.label_3.setGeometry(QtCore.QRect(170, 20, 21, 17))
        self.label_3.setObjectName("label_3")
        self.label_img_dec = QtWidgets.QLabel(FormSensitiveRotation)
        self.label_img_dec.setGeometry(QtCore.QRect(50, 40, 261, 271))
        self.label_img_dec.setText("")
        self.label_img_dec.setPixmap(QtGui.QPixmap("aug_methods/img.png"))
        self.label_img_dec.setObjectName("label_img_dec")
        self.label_4 = QtWidgets.QLabel(FormSensitiveRotation)
        self.label_4.setGeometry(QtCore.QRect(460, 20, 21, 17))
        self.label_4.setObjectName("label_4")
        self.label_img_inc = QtWidgets.QLabel(FormSensitiveRotation)
        self.label_img_inc.setGeometry(QtCore.QRect(340, 40, 261, 271))
        self.label_img_inc.setText("")
        self.label_img_inc.setPixmap(QtGui.QPixmap("aug_methods/img.png"))
        self.label_img_inc.setObjectName("label_img_inc")
        self.label_2 = QtWidgets.QLabel(FormSensitiveRotation)
        self.label_2.setGeometry(QtCore.QRect(100, 410, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(FormSensitiveRotation)
        self.label_5.setGeometry(QtCore.QRect(90, 330, 471, 41))
        self.label_5.setStyleSheet("color: rgb(239, 41, 41);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(FormSensitiveRotation)
        self.horizontalSlider.valueChanged['int'].connect(self.label.setNum)
        QtCore.QMetaObject.connectSlotsByName(FormSensitiveRotation)

    def retranslateUi(self, FormSensitiveRotation):
        _translate = QtCore.QCoreApplication.translate
        FormSensitiveRotation.setWindowTitle(_translate("FormSensitiveRotation", "Sensitive Rotation"))
        self.pushButton.setText(_translate("FormSensitiveRotation", "OK"))
        self.label.setText(_translate("FormSensitiveRotation", "0"))
        self.label_3.setText(_translate("FormSensitiveRotation", "-"))
        self.label_4.setText(_translate("FormSensitiveRotation", "+"))
        self.label_2.setText(_translate("FormSensitiveRotation", "Rotation"))
        self.label_5.setText(_translate("FormSensitiveRotation", "Note: As the rotation amount increases, the gap between the bbox and the object increases and the bbox accuracy deteriorates."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSensitiveRotation = QtWidgets.QWidget()
    ui = Ui_FormSensitiveRotation()
    ui.setupUi(FormSensitiveRotation)
    FormSensitiveRotation.show()
    sys.exit(app.exec_())
