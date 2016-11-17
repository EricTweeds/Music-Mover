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
        musicGetter(textboxInValue,textboxOutValue,videos)





def musicGetter(inputName,outputName,includeVideos):
    """
    :param inputName:  String
    :param outputName: String
    :param includeVideos Boolean
    :return: Void
    """
    music = os.listdir() #TODO: Make this a user input location
    records = []
    singers = []
    allSongs = []
    count = 0 #TODO: Make this only count ones successfully copied

    for folder in music:
        if os.path.isdir(folder) and folder == inputName:
            artists = os.listdir(folder)
            for artist in artists:
                artist = folder + "/" + artist
                singers.append(artist)

    for artist in singers:
        if os.path.isdir(artist):
            albums = os.listdir(artist)
            for album in albums:
                album = artist + "/" + album
                records.append(album)
        else:
            #checks for music file in improper location
            print("ERROR Unexpected location for file:", artist)
            allSongs.append(artist)

    for album in records:
        if os.path.isdir(album):
            songs = os.listdir(album)
            #print (songs)
            for song in songs:
                song = album + "/" + song
                allSongs.append(song)
        else:
            #checks for music file in improper location
            print("ERROR Unexpected location for file:", album)
            allSongs.append(album)

    for song in allSongs:
        #print (song)
        if ".m4a" in song:
            try:
                shutil.copy(song, outputName) #TODO: Check file type
            except OSError as err:
                #Prevents crash when running the code twice in a row
                print("OS error: {0}".format(err))
            else:
                count += 1

        elif includeVideos and ".m4v" in song:
            try:
                shutil.copy(song, outputName) #TODO: Check file type
            except OSError as err:
                #Prevents crash when running the code twice in a row
                print("OS error: {0}".format(err))
            else:
                count += 1

        else:
            print(song, "is not a valid file type")

    print (count, "songs were moved")
    print ("Complete")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())()