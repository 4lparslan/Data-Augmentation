from PyQt5.QtWidgets import *
from page4 import Ui_Form
from PyQt5.QtCore import pyqtSignal

import sys
sys.path.append("/home/alp/PycharmProjects/QT-Project/venv/Data_Augmentation_App/aug_methods")
from load_blur import BlurPage
from load_brightness import BrightPage
from load_contrast import ContrastPage
from load_exposure import ExposurePage
from load_flip import FlipPage
from load_hue import HuePage
from load_noise import NoisePage
from load_rotate import RotatePage
from load_saturation import SaturationPage
from load_sensitive_rotate import SensitiveRotatePage
from load_shear import ShearPage
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
        self.contrastpage_run = ContrastPage()
        self.exposurepage_run = ExposurePage()
        self.flippage_run = FlipPage()
        self.huepage_run = HuePage()
        self.noisepage_run = NoisePage()
        self.rotatepage_run = RotatePage()
        self.saturationpage_run = SaturationPage()
        self.sensitiverotatepage_run = SensitiveRotatePage()
        self.shearpage_run = ShearPage()
        self.grayscalepage_run = GrayscalePage()

        # Signal connections
        self.blurpage_run.the_signal.connect(self.BlurConfirm)
        self.brightpage_run.the_signal.connect(self.BrightConfirm)
        self.contrastpage_run.the_signal.connect(self.ContrastConfirm)
        self.exposurepage_run.the_signal.connect(self.ExposureConfirm)
        self.flippage_run.the_signal.connect(self.FlipConfirm)
        self.grayscalepage_run.the_signal.connect(self.GrayscaleConfirm)
        self.huepage_run.the_signal.connect(self.HueConfirm)
        self.noisepage_run.the_signal.connect(self.NoiseConfirm)
        self.rotatepage_run.the_signal.connect(self.RotateConfirm)
        self.saturationpage_run.the_signal.connect(self.SaturationConfirm)
        self.sensitiverotatepage_run.the_signal.connect(self.SensitiveRotateConfirm)
        self.shearpage_run.the_signal.connect(self.ShearConfirm)


        self.p4.pushButton_blur.clicked.connect(self.showBlur)
        self.p4.pushButton_brightness.clicked.connect(self.showBright)
        self.p4.pushButton_contrast.clicked.connect(self.showContrast)
        self.p4.pushButton_exposure.clicked.connect(self.showExposure)
        self.p4.pushButton_flip.clicked.connect(self.showFlip)
        self.p4.pushButton_hue.clicked.connect(self.showHue)
        self.p4.pushButton_noise.clicked.connect(self.showNoise)
        self.p4.pushButton_rotation.clicked.connect(self.showRotate)
        self.p4.pushButton_saturation.clicked.connect(self.showSaturation)
        self.p4.pushButton_rotation2.clicked.connect(self.showSensitiveRotate)
        self.p4.pushButton_shear.clicked.connect(self.showShear)
        self.p4.pushButton_grayscale.clicked.connect(self.showGrayscale)

    def showBlur(self):
        self.close()
        self.blurpage_run.show()
    def BlurConfirm(self, val):
        self.augmentation_list['blur'] = val
        self.page4to3_signal.emit('blur')

    def showBright(self):
        self.close()
        self.brightpage_run.show()
    def BrightConfirm(self, val, val2, val3):
        self.augmentation_list['brightness'] = [val,val2,val3]
        self.page4to3_signal.emit('brightness')

    def showContrast(self):
        self.close()
        self.contrastpage_run.show()
    def ContrastConfirm(self, val):
        self.augmentation_list['contrast'] = val
        self.page4to3_signal.emit('contrast')

    def showExposure(self):
        self.close()
        self.exposurepage_run.show()
    def ExposureConfirm(self, val):
        self.augmentation_list['exposure'] = val
        self.page4to3_signal.emit('exposure')

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

    def showShear(self):
        self.close()
        self.shearpage_run.show()
    def ShearConfirm(self, val, val2):
        self.augmentation_list['shear'] = [val, val2]
        self.page4to3_signal.emit('shear')

    def showGrayscale(self):
        self.close()
        self.grayscalepage_run.show()
    def GrayscaleConfirm(self, val):
        self.augmentation_list['grayscale'] = val
        self.page4to3_signal.emit('grayscale')