from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from page3 import Ui_add_augmentation
from load_page4 import Page4
from load_page5 import Page5

class Page3(QWidget):
    def __init__(self, the_path=None):
        super().__init__()
        self.p3 = Ui_add_augmentation()
        self.p3.setupUi(self)

        self.dataset_input_path = the_path
        self.augmentation_list = {}

        self.p3.pushButton_addaug.clicked.connect(self.ShowPage4)
        self.p3.pushButton_removeaug.clicked.connect(self.RemoveListItem)

        self.page4_run = Page4()
        

        self.page4_run.page4to3_signal.connect(self.GetListItem)
        self.p3.pushButton_next.setEnabled(False)
        self.p3.pushButton_next.clicked.connect(self.ShowPage5)

    def ShowPage4(self):
        self.page4_run.show()
    def GetListItem(self, val):
        item = QListWidgetItem(val.upper())
        self.p3.listWidget_aug.addItem(item)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.p3.pushButton_next.setEnabled(True)
    def RemoveListItem(self):
        selected_item = self.p3.listWidget_aug.selectedItems()
        if selected_item != []:
            row = self.p3.listWidget_aug.row(selected_item[0])
            item = self.p3.listWidget_aug.item(row)
            key = item.text()
            del self.page4_run.augmentation_list[key.lower()]
            self.p3.listWidget_aug.takeItem(row)
        if not bool(self.page4_run.augmentation_list):
            self.p3.pushButton_next.setEnabled(False)
    def ShowPage5(self):
        self.augmentation_list = self.page4_run.augmentation_list.copy()
        self.close()
        self.page5_run = Page5(self.dataset_input_path, self.augmentation_list)
        self.page5_run.show()
