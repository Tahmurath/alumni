import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


class HelloWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("Hello world - pythonprogramminglanguage.com")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        mdi = QMdiArea(self)
        sw = QMdiSubWindow(mdi)

        mdi.setActiveSubWindow(sw)


        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        text = QTextEdit("سلام")
        # text.text
        text.setAlignment(QtCore.Qt.AlignCenter)

        def on_button_clicked(self):
            sw2 = QMdiSubWindow(mdi)
            sw2.setVisible(True)

            alert = QMessageBox()
            alert.setText(text.toPlainText())
            alert.exec_()

        button = QPushButton('Click')
        button.clicked.connect(on_button_clicked)

        title = QLabel("Hello World from PyQt", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)
        gridLayout.addWidget(text)
        gridLayout.addWidget(button)
        gridLayout.addWidget(mdi)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('windowsvista')
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec_())
