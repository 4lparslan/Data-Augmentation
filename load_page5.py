from PyQt5.QtWidgets import *
from page5 import Ui_Form
from PyQt5.QtCore import pyqtSignal
from load_page6 import Page6

class Page5(QWidget):
    page5to3_signal = pyqtSignal(int, int, int, int)
    def __init__(self):
        super().__init__()
        self.p5 = Ui_Form()
        self.p5.setupUi(self)

        self.page6_run = Page6()

        self.p5.horizontalSlider_train.setValue(70)
        self.p5.horizontalSlider_validation.setValue(20)
        self.p5.horizontalSlider_test.setValue(10)

        # Update slider values to keep sum value 100
        self.p5.horizontalSlider_train.valueChanged.connect(self.updateSliders)
        self.p5.horizontalSlider_validation.valueChanged.connect(self.updateSliders)
        self.p5.horizontalSlider_test.valueChanged.connect(self.updateSliders)
        self.updateSliders()
        self.p5.pushButton.clicked.connect(self.ShowPage6)

    def updateSliders(self):
        total = self.p5.horizontalSlider_train.value() + self.p5.horizontalSlider_validation.value() + self.p5.horizontalSlider_test.value()
        remaining = 100 - total

        sender = self.sender()  # Değişiklik yapan sliderı al

        if total > 100:
            # Toplam 100'den büyükse, fazla olan değeri diğer sliderlara dağıtın
            diff = total - 100
            if sender == self.p5.horizontalSlider_train:
                if self.p5.horizontalSlider_validation.value() >= diff:
                    self.p5.horizontalSlider_validation.setValue(self.p5.horizontalSlider_validation.value() - diff)
                else:
                    self.p5.horizontalSlider_test.setValue(self.p5.horizontalSlider_test.value() - (diff - self.p5.horizontalSlider_validation.value()))
                    self.p5.horizontalSlider_validation.setValue(self.p5.horizontalSlider_validation.value() - self.p5.horizontalSlider_validation.value())

            elif sender == self.p5.horizontalSlider_validation:
                if self.p5.horizontalSlider_train.value() >= diff:
                    self.p5.horizontalSlider_train.setValue(self.p5.horizontalSlider_train.value() - diff)
                else:
                    self.p5.horizontalSlider_test.setValue(self.p5.horizontalSlider_test.value() - (diff - self.p5.horizontalSlider_train.value()))
                    self.p5.horizontalSlider_train.setValue(self.p5.horizontalSlider_train.value() - self.p5.horizontalSlider_train.value())

            elif sender == self.p5.horizontalSlider_test:
                if self.p5.horizontalSlider_train.value() >= diff:
                    self.p5.horizontalSlider_train.setValue(self.p5.horizontalSlider_train.value() - diff)
                else:
                    self.p5.horizontalSlider_test.setValue(self.p5.horizontalSlider_test.value() - (diff - self.p5.horizontalSlider_train.value()))
                    self.p5.horizontalSlider_train.setValue(self.p5.horizontalSlider_train.value() - self.p5.horizontalSlider_train.value())

        elif total < 100:
            # Toplam 100'den küçükse, kalan değeri diğer sliderlara dağıtın
            if sender == self.p5.horizontalSlider_train:
                the_val = (100 - self.p5.horizontalSlider_validation.value())
                if (100 - self.p5.horizontalSlider_validation.value()) >= remaining:
                    self.p5.horizontalSlider_validation.setValue(self.p5.horizontalSlider_validation.value() + remaining)
                else:
                    self.p5.horizontalSlider_validation.setValue(100)
                    self.p5.horizontalSlider_test.setValue(self.p5.horizontalSlider_test.value() + (remaining - the_val))


            elif sender == self.p5.horizontalSlider_validation:
                the_val = (100 - self.p5.horizontalSlider_train.value())
                if (100 - self.p5.horizontalSlider_train.value()) >= remaining:
                    self.p5.horizontalSlider_train.setValue(self.p5.horizontalSlider_train.value() + remaining)
                else:
                    self.p5.horizontalSlider_train.setValue(100)
                    self.p5.horizontalSlider_test.setValue(self.p5.horizontalSlider_test.value() + (remaining - the_val))

            elif sender == self.p5.horizontalSlider_test:
                the_val = (100 - self.p5.horizontalSlider_train.value())
                if (100 - self.p5.horizontalSlider_train.value()) >= remaining:
                    self.p5.horizontalSlider_train.setValue(self.p5.horizontalSlider_train.value() + remaining)
                else:
                    self.p5.horizontalSlider_train.setValue(100)
                    self.p5.horizontalSlider_validation.setValue(self.p5.horizontalSlider_validation.value() + (remaining - the_val))

    def ShowPage6(self):
        val1 = self.p5.horizontalSlider_train.value()
        val2 = self.p5.horizontalSlider_validation.value()
        val3 = self.p5.horizontalSlider_test.value()
        val4 = self.p5.horizontalSlider_size.value()
        self.page5to3_signal.emit(val1, val2, val3, val4)
        self.close()
        self.page6_run.show()