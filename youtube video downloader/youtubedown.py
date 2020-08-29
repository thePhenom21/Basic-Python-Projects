# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtubedown.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
import os, time
from counter import count, downloads


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 200)
        MainWindow.setWindowIcon(QtGui.QIcon("youtube.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.link = QtWidgets.QLabel(self.centralwidget)
        self.link.setGeometry(QtCore.QRect(10, 50, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.link.setFont(font)
        self.link.setObjectName("link")
        self.url_place = QtWidgets.QLineEdit(self.centralwidget)
        self.url_place.setGeometry(QtCore.QRect(185, 50, 301, 21))
        self.url_place.setObjectName("url_place")
        self.url_place.setPlaceholderText("https://www.youtube.com/watch?v=...")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(150, 160, 47, 13))
        self.info.setText("Please insert a youtube url")
        self.info.adjustSize()
        self.info.setObjectName("info")
        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(170, 100, 111, 41))
        self.download.setObjectName("download")
        MainWindow.setCentralWidget(self.centralwidget)
        self.progress = QtWidgets.QProgressBar(self.centralwidget)
        self.progress.setGeometry(300,120,200,20)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.download.clicked.connect(self.get)


    def get(self):
        global directory2, completed
        completed = 0
        os.environ['MOZ_HEADLESS'] = '1'
        address = self.url_place.text()
        fp = webdriver.FirefoxProfile()
        directory = os.getcwd()+"\geckodriver.exe"
        directory2 = os.getcwd() + "\Downloads"
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.dir", directory2)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk","video/mp4")
        browser = webdriver.Firefox(executable_path=directory,firefox_profile=fp)
        browser.get('https://keepvid.pro/en44/youtube-converter-free')
        element = browser.find_element_by_xpath('//*[@id="videourl"]')
        element.send_keys(address)
        button = browser.find_element_by_xpath('//*[@id="downloadbtn"]')
        button.click()
        window_name = browser.window_handles[1]
        browser.switch_to.window(window_name=window_name)
        browser.close()
        window_name = browser.window_handles[0]
        browser.switch_to.window(window_name=window_name)
        time.sleep(10)
        button2 = browser.find_element_by_xpath('//*[@id="best-download-btn"]')
        button2.click()
        while True:
            #global downloaded
            #downloaded = os.listdir(directory2)
            try:
                if len(downloads) > 0:
                    print(downloads)
                    print(count)
                    size = os.path.getsize(f"{directory2}\{downloads[count]}")
                    if size > 10000:
                        size = float(size/1000000)
                        print(count+1)
                        self.info.setText(f"File Size: {'%.1f'%size} MB")
                        self.info.adjustSize()
                        self.downloaded()
                        break
            except:
                pass
        browser.quit()

    def downloaded(self):
        while completed < 100:
            completed += 1
            self.progress.setValue(completed)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YoutubeVideoDownloader"))
        self.link.setText(_translate("MainWindow", "Youtube Video Url:"))
        self.download.setText(_translate("MainWindow", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
