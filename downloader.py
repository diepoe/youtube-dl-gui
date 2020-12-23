from __future__ import unicode_literals
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit, QMessageBox
from PyQt5.QtCore import QSize

import youtube_dl


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set parameter for the window
        self.setMinimumSize(QSize(300, 150))
        self.setWindowTitle('youtube-dl')

        # create grid layout

        # initialize widget
        wid = QWidget(self)
        self.setCentralWidget(wid)
        grid = QGridLayout()
        wid.setLayout(grid)

        # labels
        row = 0
        labels = ['URL: ', '', ]

        for label in labels:
            lbl = QLabel(label)
            lbl.resize(lbl.sizeHint())
            grid.addWidget(lbl, row, 1, QtCore.Qt.AlignRight)

            row += 1

        # url input field
        self.url = QLineEdit(self)
        grid.addWidget(self.url, 0, 2, QtCore.Qt.AlignLeft)

        # saving directory input field
        safebutton = QPushButton('Select saving directory', self)
        safebutton.clicked.connect(self.get_directory)
        grid.addWidget(safebutton, 1, 2)

        # submit button
        submit = QPushButton('Download', self)
        submit.clicked.connect(self.download)
        grid.addWidget(submit, 3, 2)

        # clear button
        cancel = QPushButton('Cancel', self)
        cancel.clicked.connect(self.url.clear)
        grid.addWidget(cancel, 3, 1)

    def get_directory(self):
        safe_path = QFileDialog(self)
        safe_path.setFileMode(QFileDialog.Directory)

        if safe_path.exec_():
            self.directory = safe_path.selectedFiles()

    def download(self):
        try:
            download_url = self.url.text()

            ydl_opts = {
                'outtmpl': self.directory[0] + '/' + '%(title)s.%(ext)s',
                'format': 'best',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([download_url])

        except:
            QMessageBox.about(self, 'Error', 'Something went wrong!')


# start window
app = QtWidgets.QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
