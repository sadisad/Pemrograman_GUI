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
    def setupUi(self):
        self.resize(300, 100) # Mengatur ukuran tampilan
        self.move(300, 300) # Mengatur letak tapilan
        self.setWindowTitle('Demo QFontComboBox') # Judul tampilan
        self.fontCombo = QFontComboBox()
        self.fontCombo.setEditable(False) 
        self.label = QLabel('Contoh Teks') # Membuat label dengan nama Contoh Teks
        self.label.setFont(QFont('DejaVu Sans',18)) # Mengatur font label default Dejavu Sans dengan ukuran 18
        layout = QVBoxLayout()
        layout.addWidget(self.fontCombo)
        layout.addWidget(self.label)
        layout.addStretch()
        self.setLayout(layout)
        self.fontCombo.activated.connect(self.fontComboActivated) # Jika comboBox dipilih maka akan menuju ke function fontComboActivated
    # Function fontComboActivated
    def fontComboActivated(self):
        self.label.setFont(QFont(self.fontCombo.currentText(), 18))

# Bagian utama untuk menjalankan program
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
