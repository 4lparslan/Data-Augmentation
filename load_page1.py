from PyQt5.QtWidgets import *
from page1 import Ui_Form
from load_page2 import Page2
from natsort import natsorted
import os

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
        image_files = natsorted([os.path.join(self.selected_folder_path, f) for f in os.listdir(self.selected_folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))])
        annotation_files = natsorted([os.path.join(self.selected_folder_path, f) for f in os.listdir(self.selected_folder_path) if f.endswith(('.txt'))])
        error = False
        if len(image_files) != len(annotation_files):
            # ERROR MESSAGE
            QMessageBox.warning(self, "ERROR", "Please check your dataset. Make sure there is annotation file for each image.")
            error = True

        elif len(image_files) == len(annotation_files):
            for i in range(len(image_files)):
                im = os.path.basename(image_files[i])
                an = os.path.basename(annotation_files[i])
                if os.path.splitext(im)[0] != os.path.splitext(an)[0]:
                    # ERROR MESSAGE
                    QMessageBox.warning(self, "ERROR", "There is a problem with annotation files. Please check the names of the files in your dataset.")
                    error = True
                    break
                     
        if not error:
            self.ShowPage2()
        

    def ShowPage2(self):
        self.page2_run = Page2(self.selected_folder_path, self.WindowSize)
        self.close()
        self.page2_run.showFullScreen()