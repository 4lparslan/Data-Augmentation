# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'noise.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormNoise(object):
    def setupUi(self, FormNoise):
        FormNoise.setObjectName("FormNoise")
        FormNoise.resize(466, 480)
        self.horizontalSlider = QtWidgets.QSlider(FormNoise)
        self.horizontalSlider.setGeometry(QtCore.QRect(59, 320, 351, 20))
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(FormNoise)
        self.label.setGeometry(QtCore.QRect(210, 360, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(FormNoise)
        self.pushButton.setGeometry(QtCore.QRect(190, 420, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_img = QtWidgets.QLabel(FormNoise)
        self.label_img.setGeometry(QtCore.QRect(110, 30, 261, 271))
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap("aug_methods/img.png"))
        self.label_img.setObjectName("label_img")

        self.retranslateUi(FormNoise)
        self.horizontalSlider.valueChanged['int'].connect(self.label.setNum) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(FormNoise)

    def retranslateUi(self, FormNoise):
        _translate = QtCore.QCoreApplication.translate
        FormNoise.setWindowTitle(_translate("FormNoise", "Noise"))
        self.label.setText(_translate("FormNoise", "0"))
        self.pushButton.setText(_translate("FormNoise", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormNoise = QtWidgets.QWidget()
    ui = Ui_FormNoise()
    ui.setupUi(FormNoise)
    FormNoise.show()
    sys.exit(app.exec_())
