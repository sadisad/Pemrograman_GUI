# ANDRA AULIA RIZALDY
# 19104062
import sys

from PyQt5.QtWidgets import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.resize(300, 100) # mengatur ukuran tampilan 
        self.move(300, 300) # mengatur letak tampilan 
        self.setWindowTitle('Demo QCheckBox') # judul tampilan 
        self.label = QLabel() 
        self.label.setText('Bahasa Pemrograman Favorit Anda :') # Cetak label dengan tulisan seperti di dalam kurung
        self.javaCheck = QCheckBox() # Membuat checkbox
        self.javaCheck.setText('Java') # Keterangan 'Java' pada checkbox
        self.pythonCheck = QCheckBox() # Membuat checkbox
        self.pythonCheck.setText('Python') # Keterangan 'Python' pada checkbox
        self.rubyCheck = QCheckBox() # Membuat checkbox
        self.rubyCheck.setText('Ruby') # Keterangan 'Ruby' pada checkbox
        self.phpCheck = QCheckBox() # Membuat checkbox
        self.phpCheck.setText('PHP') # Keterangan 'PHP' pada checkbox
        hbox1 = QHBoxLayout() # Layout untuk menampung checkbox dan button
        hbox1.addWidget(self.javaCheck)
        hbox1.addWidget(self.pythonCheck)
        hbox1.addWidget(self.rubyCheck)
        hbox1.addWidget(self.phpCheck)
        self.okButton = QPushButton('&OK') # Button Ok yang bersifat pushbutton
        self.exitButton = QPushButton('Keluar') # Button keluar yang bersifat pushbutton
        hbox2 = QHBoxLayout() # Layout untuk menampung button
        hbox2.addStretch()
        hbox2.addWidget(self.okButton)
        hbox2.addWidget(self.exitButton)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(hbox1)
        horizontalLine = QFrame(); # Membuat garis horizontal di dalam frame
        horizontalLine.setFrameShape(QFrame.HLine)
        horizontalLine.setFrameShadow(QFrame.Sunken)
        layout.addWidget(horizontalLine)
        layout.addLayout(hbox2)
        layout.addStretch()
        self.setLayout(layout)
        self.okButton.clicked.connect(self.okButtonClick) # Jika okButton di click maka menuju function okButtonClick
        self.exitButton.clicked.connect(self.close) # Jika exitButton di click maka menuju function close
        # Function close tidak perlu dibuat kembali karna sudah otomatis 


    # Function okButtonClick
    def okButtonClick(self):
        # variable choices yang menampung array
        choices = []
        # Jika javachecked di ceklist maka variable choices akan menambahkan data 'Java'
        if self.javaCheck.isChecked(): choices.append('Java')
        # Jika pythonCheck di ceklist maka variable choices akan menambahkan data 'Python'
        if self.pythonCheck.isChecked(): choices.append('Python')
        # Jika rubychecked di ceklist maka variable choices akan menambahkan data 'Ruby'
        if self.rubyCheck.isChecked(): choices.append('Ruby')
        # Jika phpchecked di ceklist maka variable choices akan menambahkan data 'PHP'
        if self.phpCheck.isChecked(): choices.append('PHP')
        # Menampilkan pesan dengan judul informasi yang didalamnya menampilkan nilai dari variable choices
        QMessageBox.information(self, 'Informasi', repr(choices))

# bagian utama untuk menjalankan program
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
