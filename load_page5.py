from PyQt5.QtWidgets import *
from page5 import Ui_Form
from load_page6 import Page6
from augmentation_worker import Augmentation_Worker

class Page5(QWidget):
    def __init__(self, input_path, aug_list):
        super().__init__()
        self.p5 = Ui_Form()
        self.p5.setupUi(self)

        # all parameters
        self.output_parameters = {}
        self.dataset_input_path = input_path
        self.augmentation_list = aug_list
        self.output_path = None

        self.page6_run = Page6()
        self.selected_output_path = ""
        self.p5.pushButton_output_path.clicked.connect(self.ShowFolderDialog)
        self.p5.pushButton_prepare.setEnabled(False)
        self.p5.pushButton_prepare.clicked.connect(self.ShowPage6)

        self.p5.horizontalSlider_train.setValue(70)
        self.p5.horizontalSlider_validation.setValue(20)
        self.p5.horizontalSlider_test.setValue(10)

        # Update slider values to keep sum value 100
        self.p5.horizontalSlider_train.valueChanged.connect(self.updateSliders)
        self.p5.horizontalSlider_validation.valueChanged.connect(self.updateSliders)
        self.p5.horizontalSlider_test.valueChanged.connect(self.updateSliders)
        self.updateSliders()


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
        self.output_parameters['train'] = val1
        self.output_parameters['validation'] = val2
        self.output_parameters['test'] = val3
        self.output_parameters['size'] = val4
        self.output_path = self.p5.label_output_path.text()

        ### Augmentation'ı başlatacak fonksiyonu burada ÇAĞIR
        Augmentation_Worker(output_param= self.output_parameters, dataset_input=self.dataset_input_path, aug_list=self.augmentation_list, out_path=self.output_path)

        self.page6_run.show()

    def ShowFolderDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose Folder', '', options=options)
        if folder_path:
            self.selected_output_path = folder_path
            self.p5.label_output_path.setText(self.selected_output_path)
            self.p5.pushButton_prepare.setEnabled(True)