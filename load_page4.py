from PyQt5.QtWidgets import *
from page4 import Ui_Form
from PyQt5.QtCore import pyqtSignal

import sys
sys.path.append("/home/alp/PycharmProjects/QT-Project/venv/Data_Augmentation_App/aug_methods")
from load_blur import BlurPage
from load_brightness import BrightPage
from load_flip import FlipPage
from load_hue import HuePage
from load_noise import NoisePage
from load_rotate import RotatePage
from load_saturation import SaturationPage
from load_sensitive_rotate import SensitiveRotatePage
from load_grayscale import GrayscalePage



class Page4(QWidget):
    page4to3_signal= pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.p4 = Ui_Form()
        self.p4.setupUi(self)

        # This dictionary holds the choosen data augmentation methods with their parameter values.
        self.augmentation_list = {}

        self.blurpage_run = BlurPage()
        self.brightpage_run = BrightPage()
        self.flippage_run = FlipPage()
        self.huepage_run = HuePage()
        self.noisepage_run = NoisePage()
        self.rotatepage_run = RotatePage()
        self.saturationpage_run = SaturationPage()
        self.sensitiverotatepage_run = SensitiveRotatePage()
        self.grayscalepage_run = GrayscalePage()

        # Signal connections
        self.blurpage_run.the_signal.connect(self.BlurConfirm)
        self.brightpage_run.the_signal.connect(self.BrightConfirm)
        self.flippage_run.the_signal.connect(self.FlipConfirm)
        self.grayscalepage_run.the_signal.connect(self.GrayscaleConfirm)
        self.huepage_run.the_signal.connect(self.HueConfirm)
        self.noisepage_run.the_signal.connect(self.NoiseConfirm)
        self.rotatepage_run.the_signal.connect(self.RotateConfirm)
        self.saturationpage_run.the_signal.connect(self.SaturationConfirm)
        self.sensitiverotatepage_run.the_signal.connect(self.SensitiveRotateConfirm)


        self.p4.pushButton_blur.clicked.connect(self.showBlur)
        self.p4.pushButton_brightness.clicked.connect(self.showBright)
        self.p4.pushButton_flip.clicked.connect(self.showFlip)
        self.p4.pushButton_hue.clicked.connect(self.showHue)
        self.p4.pushButton_noise.clicked.connect(self.showNoise)
        self.p4.pushButton_rotation.clicked.connect(self.showRotate)
        self.p4.pushButton_saturation.clicked.connect(self.showSaturation)
        self.p4.pushButton_rotation2.clicked.connect(self.showSensitiveRotate)
        self.p4.pushButton_grayscale.clicked.connect(self.showGrayscale)

        self.p4.pushButton_shear.setEnabled(False)
        self.p4.pushButton_contrast.setEnabled(False)
        self.p4.pushButton_exposure.setEnabled(False)

    def showBlur(self):
        self.close()
        self.blurpage_run.show()
    def BlurConfirm(self, val):
        self.augmentation_list['blur'] = val
        self.page4to3_signal.emit('blur')

    def showBright(self):
        self.close()
        self.brightpage_run.show()
    def BrightConfirm(self, val):
        self.augmentation_list['brightness'] = val
        self.page4to3_signal.emit('brightness')

    def showFlip(self):
        self.close()
        self.flippage_run.show()
    def FlipConfirm(self, val, val2):
        self.augmentation_list['flip'] = [val, val2]
        self.page4to3_signal.emit('flip')

    def showHue(self):
        self.close()
        self.huepage_run.show()
    def HueConfirm(self, val):
        self.augmentation_list['hue'] = val
        self.page4to3_signal.emit('hue')

    def showNoise(self):
        self.close()
        self.noisepage_run.show()
    def NoiseConfirm(self, val):
        self.augmentation_list['noise'] = val
        self.page4to3_signal.emit('noise')

    def showRotate(self):
        self.close()
        self.rotatepage_run.show()
    def RotateConfirm(self, val, val2, val3):
        self.augmentation_list['rotation'] = [val, val2, val3]
        self.page4to3_signal.emit('rotation')

    def showSaturation(self):
        self.close()
        self.saturationpage_run.show()
    def SaturationConfirm(self, val):
        self.augmentation_list['saturation'] = val
        self.page4to3_signal.emit('saturation')

    def showSensitiveRotate(self):
        self.close()
        self.sensitiverotatepage_run.show()
    def SensitiveRotateConfirm(self, val):
        self.augmentation_list['sensitive_rotation'] = val
        self.page4to3_signal.emit('sensitive_rotation')

    def showGrayscale(self):
        self.close()
        self.grayscalepage_run.show()
    def GrayscaleConfirm(self, val):
        self.augmentation_list['grayscale'] = val
        self.page4to3_signal.emit('grayscale')
        
