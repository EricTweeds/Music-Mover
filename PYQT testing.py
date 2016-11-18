import os
import shutil
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QCheckBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Music Mover'
        self.left = 500
        self.top = 500
        self.width = 400
        self.height = 240
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textboxIn = QLineEdit(self)
        self.textboxIn.move(60, 20)
        self.textboxIn.resize(280,40)

        self.textboxOut = QLineEdit(self)
        self.textboxOut.move(60, 80)
        self.textboxOut.resize(280,40)

        self.vidButton = QCheckBox(self)
        self.vidButton.move(20, 140)

        self.inputLabel = QLabel(self)
        self.inputLabel.setText("Input:")
        self.inputLabel.move(10,25)

        self.outputLabel = QLabel(self)
        self.outputLabel.setText("Output:")
        self.outputLabel.move(10,85)

        self.vidLabel = QLabel(self)
        self.vidLabel.setText("Include Videos")
        self.vidLabel.move(50,140)


        # Create a button in the window
        self.button = QPushButton('Move Files', self)
        self.button.move(150,180)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        videos = self.vidButton.isChecked()
        textboxInValue = self.textboxIn.text()
        textboxOutValue = self.textboxOut.text()
        array = []
        print(fileGetter(textboxInValue,array))



def fileGetter(cfolder, files):
    """
    :param cfolder: directory
    :param files: array[string]
    :return: array[string]
    """
    directory = os.listdir(cfolder)
    for item in directory:
        item = cfolder+"/"+item
        if os.path.isdir(item):
            fileGetter(item, files)
        else:
            files.append(item)
    return files


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())()