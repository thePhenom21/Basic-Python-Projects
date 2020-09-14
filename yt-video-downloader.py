# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtubedown2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkgraystyle
from pytube import YouTube
import time
from threading import Thread



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/youtube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.link = QtWidgets.QLabel(self.centralwidget)
        self.link.setGeometry(QtCore.QRect(10, 50, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.link.setFont(font)
        self.link.setObjectName("link")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 50, 301, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("type in a url like: https://www.youtube.com/watch?v=... ")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100,150,250,20))
        self.msg = QtWidgets.QMessageBox(self.centralwidget)
        self.progress = QtWidgets.QProgressBar(self.centralwidget)
        self.progress.setGeometry(100, 170, 250, 20)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 100, 111, 41))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.download)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YoutubeVideoDownloader"))
        self.link.setText(_translate("MainWindow", "Youtube Video Link:"))
        self.pushButton.setText(_translate("MainWindow", "Download"))


    def download(self):
        self.progress.setValue(0)
        url = self.lineEdit.text()
        yt = YouTube(url)
        time.sleep(5)
        stream = yt.streams.first()
        self.label.setText(stream.title)
        self.label.adjustSize()
        stream.download('downloads')
        Thread(target=self.bar).start()
        time.sleep(2)
        self.label.setText("")

    def bar(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.00009
            self.progress.setValue(self.completed)

        self.msg.setText("Download Finished.")
        self.msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet((qdarkgraystyle).load_stylesheet())
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
