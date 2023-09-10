from PyQt5.QtWidgets import *
from page6 import Ui_Form

class Page6(QWidget):
    def __init__(self):
        super().__init__()
        self.p6 = Ui_Form()
        self.p6.setupUi(self)
        self.selected_output_path = ""
        self.p6.pushButton_output_path.clicked.connect(self.ShowFolderDialog)
        self.p6.pushButton_prepare.setEnabled(False)
        self.p6.pushButton_prepare.clicked.connect(self.PrepareDataset)

    def ShowFolderDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose Folder', '', options=options)
        if folder_path:
            self.selected_output_path = folder_path
            self.p6.label_output_path.setText(self.selected_output_path)
            self.p6.pushButton_prepare.setEnabled(True)
    def PrepareDataset(self):
        pass