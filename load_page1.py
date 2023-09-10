from PyQt5.QtWidgets import *
from page1 import Ui_Form
from load_page3 import Page3

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        self.p1 = Ui_Form()
        self.p1.setupUi(self)

        self.selected_folder_path = ""
        self.p1.pushButton_dataset.clicked.connect(self.ShowFolderDialog)

        self.p1.pushButton_check.setEnabled(False)
        self.p1.pushButton_check.clicked.connect(self.CheckDataset)

        self.page3_run = Page3()

    def ShowFolderDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose Folder', '', options=options)
        if folder_path:
            self.selected_folder_path = folder_path
            self.p1.label_dataset.setText(self.selected_folder_path)
            self.p1.pushButton_check.setEnabled(True)

    def CheckDataset(self):
        #
        #
        #
        self.close()
        self.page3_run.show()