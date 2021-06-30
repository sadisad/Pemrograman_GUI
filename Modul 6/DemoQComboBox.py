# ANDRA AULIA RIZALDY
# 19104062
import sys

from PyQt5.QtWidgets import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.resize(300, 100) # Mengatur ukuran tampilan (x = 300, y = 100)
        self.move(300, 300) # Mengatur letak tampilan
        self.setWindowTitle('Demo QComboBox') # Judul tampilan
        self.combo = QComboBox() # Membuat comboBox dengan perulangan
        for i in range(1, 11): # Looping dimulai dari 1 hingga 11
            self.combo.addItem('Item ke-%d' % i) # Pada comboBox akan ditampilkan nilai yang ada pada looping
        self.getTextButton = QPushButton('Ambil Teks') # Membuat pushbutton dengan nama Ambil Teks
        layout = QVBoxLayout() 
        layout.addWidget(self.combo) 
        layout.addWidget(self.getTextButton)
        layout.addStretch()
        self.setLayout(layout)
        self.getTextButton.clicked.connect(self.getTextButtonClick) # Jika button di klik maka menuju ke function getTextButtonClick


    # Function getTextButtonClick
    def getTextButtonClick(self):
        # Isi function yaitu menampilkan pesan dengan isi seperti berikut:
        QMessageBox.information(self, 'Informasi',
                                'Anda memilih: ' + self.combo.currentText())


# Bagian utama untuk menjalankan program
if __name__ == '__main__':    a = QApplication(sys.argv)
form = MainForm()
form.show()
a.exec_()
