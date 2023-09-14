from PyQt5.QtWidgets import *
from page1 import Ui_Form
from load_page2 import Page2

class Page1(QWidget):
    def __init__(self, WindowSize = []):
        super().__init__()
        self.p1 = Ui_Form()
        self.p1.setupUi(self)
        self.WindowSize = WindowSize

        self.selected_folder_path = ""
        self.p1.pushButton_dataset.clicked.connect(self.ShowFolderDialog)

        self.p1.pushButton_check.setEnabled(False)
        self.p1.pushButton_check.clicked.connect(self.CheckDataset)

    def ShowFolderDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose Folder', '', options=options)
        if folder_path:
            self.selected_folder_path = folder_path
            self.p1.label_dataset.setText(self.selected_folder_path)
            self.p1.pushButton_check.setEnabled(True)

    def CheckDataset(self):
        self.page2_run = Page2(self.selected_folder_path, self.WindowSize)
        self.close()
        self.page2_run.showFullScreen()