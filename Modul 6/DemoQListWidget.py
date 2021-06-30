# ANDRA AULIA RIZALDY
# 19104062
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    # Function untuk membuat tampilan GUI
    def setupUi(self):
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle('Demo QListWidget')
        self.label = QLabel('&Elemen baru')
        self.itemEdit = QLineEdit()
        self.label.setBuddy(self.itemEdit)
        self.addItemButton = QPushButton('Tambah')
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.itemEdit)
        hbox1.addWidget(self.addItemButton)
        hbox1.addStretch()
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label)
        vbox1.addLayout(hbox1)
        self.list1 = QListWidget()
        self.moveRightButton = QPushButton('>')
        self.moveRightAllButton = QPushButton('>>')
        self.moveLeftButton = QPushButton('<')
        self.moveLeftAllButton = QPushButton('<<')
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.moveRightButton)
        vbox2.addWidget(self.moveRightAllButton)
        vbox2.addWidget(self.moveLeftButton)
        vbox2.addWidget(self.moveLeftAllButton)
        vbox2.addStretch()
        self.list2 = QListWidget()
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.list1)
        hbox2.addLayout(vbox2)
        hbox2.addWidget(self.list2)
        layout = QVBoxLayout()
        layout.addLayout(vbox1)
        layout.addLayout(hbox2)
        self.setLayout(layout)
        self.addItemButton.clicked.connect(self.addItemButtonClick) # Connect ke function addItemButton
        self.moveRightButton.clicked.connect(self.moveRightButtonClick) # Connect ke function moveRightButton
        self.moveRightAllButton.clicked.connect(self.moveRightAllButtonClick) # Connect ke function moveRightAllButton
        self.moveLeftButton.clicked.connect(self.moveLeftButtonClick) # Connect ke function moveLeftButton
        self.moveLeftAllButton.clicked.connect(self.moveLeftAllButtonClick) # Connect ke function moveLeftAllButton
    # Function addItemButton 
    def addItemButtonClick(self):
        if len(self.itemEdit.text()) == 0: return 
        item = self.itemEdit.text()
        self.list1.addItem(item)
        self.itemEdit.clear()
        self.itemEdit.setFocus()
    # Function moveRightButtonClick
    def moveRightButtonClick(self):
        if self.list1.currentRow() < 0: return
        self.list2.addItem(self.list1.currentItem().text())
        self.list1.takeItem(self.list1.currentRow())
    # Function moveRightAllButtonClick
    def moveRightAllButtonClick(self):
        for index in range(self.list1.count()):
            self.list2.addItem(self.list1.item(index).text())
            self.list1.clear()
    # Function moveLeftButtonClick
    def moveLeftButtonClick(self):
        if self.list2.currentRow() < 0: return
        self.list1.addItem(self.list2.currentItem().text())
        self.list2.takeItem(self.list2.currentRow())
    # Function moveLeftAllButtonClick
    def moveLeftAllButtonClick(self):
        for index in range(self.list2.count()):
            self.list1.addItem(self.list2.item(index).text())
            self.list2.clear()

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
