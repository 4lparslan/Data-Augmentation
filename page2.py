# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowState(QtCore.Qt.WindowFullScreen)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_img = QtWidgets.QLabel(Form)
        self.label_img.setText("")
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setObjectName("label_img")
        self.verticalLayout_2.addWidget(self.label_img)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_prev = QtWidgets.QPushButton(Form)
        self.pushButton_prev.setObjectName("pushButton_prev")
        self.horizontalLayout.addWidget(self.pushButton_prev)
        self.pushButton_next = QtWidgets.QPushButton(Form)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_approve = QtWidgets.QPushButton(Form)
        self.pushButton_approve.setObjectName("pushButton_approve")
        self.verticalLayout.addWidget(self.pushButton_approve)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Show Dataset"))
        self.pushButton_prev.setText(_translate("Form", "Previous"))
        self.pushButton_next.setText(_translate("Form", "Next"))
        self.pushButton_approve.setText(_translate("Form", "Go To Next Step"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
