# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flip.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormFlip(object):
    def setupUi(self, FormFlip):
        FormFlip.setObjectName("FormFlip")
        FormFlip.resize(641, 431)
        self.checkBox_horizontal = QtWidgets.QCheckBox(FormFlip)
        self.checkBox_horizontal.setGeometry(QtCore.QRect(130, 300, 101, 21))
        self.checkBox_horizontal.setObjectName("checkBox_horizontal")
        self.checkBox_vertical = QtWidgets.QCheckBox(FormFlip)
        self.checkBox_vertical.setGeometry(QtCore.QRect(420, 300, 92, 23))
        self.checkBox_vertical.setObjectName("checkBox_vertical")
        self.pushButton = QtWidgets.QPushButton(FormFlip)
        self.pushButton.setGeometry(QtCore.QRect(280, 340, 71, 61))
        self.pushButton.setObjectName("pushButton")
        self.label_img_horizontal = QtWidgets.QLabel(FormFlip)
        self.label_img_horizontal.setGeometry(QtCore.QRect(50, 20, 261, 271))
        self.label_img_horizontal.setText("")
        self.label_img_horizontal.setObjectName("label_img_horizontal")
        self.label_img_vertical = QtWidgets.QLabel(FormFlip)
        self.label_img_vertical.setGeometry(QtCore.QRect(330, 20, 261, 271))
        self.label_img_vertical.setText("")
        self.label_img_vertical.setObjectName("label_img_vertical")

        self.retranslateUi(FormFlip)
        QtCore.QMetaObject.connectSlotsByName(FormFlip)

    def retranslateUi(self, FormFlip):
        _translate = QtCore.QCoreApplication.translate
        FormFlip.setWindowTitle(_translate("FormFlip", "Flip"))
        self.checkBox_horizontal.setText(_translate("FormFlip", "Horizontal"))
        self.checkBox_vertical.setText(_translate("FormFlip", "Vertical"))
        self.pushButton.setText(_translate("FormFlip", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormFlip = QtWidgets.QWidget()
    ui = Ui_FormFlip()
    ui.setupUi(FormFlip)
    FormFlip.show()
    sys.exit(app.exec_())
