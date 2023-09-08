from PyQt5.QtWidgets import *
from page4 import Ui_Form

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
    def __init__(self):
        super().__init__()
        self.p4 = Ui_Form()
        self.p4.setupUi(self)

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
    def showBright(self):
        self.close()
        self.brightpage_run.show()
    def showContrast(self):
        self.close()
        self.contrastpage_run.show()
    def showExposure(self):
        self.close()
        self.exposurepage_run.show()
    def showFlip(self):
        self.close()
        self.flippage_run.show()
    def showHue(self):
        self.close()
        self.huepage_run.show()
    def showNoise(self):
        self.close()
        self.noisepage_run.show()
    def showRotate(self):
        self.close()
        self.rotatepage_run.show()
    def showSaturation(self):
        self.close()
        self.saturationpage_run.show()
    def showSensitiveRotate(self):
        self.close()
        self.sensitiverotatepage_run.show()
    def showShear(self):
        self.close()
        self.shearpage_run.show()
    def showGrayscale(self):
        self.close()
        self.grayscalepage_run.show()