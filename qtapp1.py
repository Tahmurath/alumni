#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import *


app = QApplication([])


button = QPushButton('Click')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()


button.clicked.connect(on_button_clicked)
#button.show()


app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()