# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        font = QtGui.QFont()
        font.setPointSize(70)
        MainWindow.setFont(font)
        MainWindow.setWindowIcon(QtGui.QIcon('calculator.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(80, 260, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.five.setFont(font)
        self.five.setObjectName("five")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(0, 260, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.four.setFont(font)
        self.four.setObjectName("four")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(160, 260, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.six.setFont(font)
        self.six.setObjectName("six")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(160, 340, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(80, 340, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(80, 420, 80, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(0, 340, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(0, 180, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
        #self.comma = QtWidgets.QPushButton(self.centralwidget)
        #self.comma.setGeometry(QtCore.QRect(160, 420, 80, 80))
        #font = QtGui.QFont()
        #font.setPointSize(40)
        #self.comma.setFont(font)
        #self.comma.setObjectName("comma")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(80, 180, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(160, 180, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.nine.setFont(font)
        self.nine.setObjectName("nine")
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(240, 420, 161, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.equal.setFont(font)
        self.equal.setObjectName("equal")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(320, 180, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.multiply.setFont(font)
        self.multiply.setObjectName("multiply")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(0, 420, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(240, 340, 161, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.plus.setFont(font)
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(240, 260, 161, 80))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.minus.setFont(font)
        self.minus.setObjectName("minus")
        self.division = QtWidgets.QPushButton(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(240, 180, 81, 80))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.division.setFont(font)
        self.division.setObjectName("division")
        self.answer = QtWidgets.QLineEdit(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(0, 0, 401, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer.sizePolicy().hasHeightForWidth())
        self.answer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(70)
        self.answer.setFont(font)
        self.answer.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.answer.setAutoFillBackground(False)
        self.answer.setStyleSheet("background:rgb(248, 249, 248)")
        self.answer.setText("")
        self.answer.setFrame(False)
        self.answer.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.answer.setReadOnly(True)
        self.answer.setPlaceholderText("")
        self.answer.setObjectName("answer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.zero.clicked.connect(lambda: self.show(0))
        self.one.clicked.connect(lambda: self.show(1))
        self.two.clicked.connect(lambda: self.show(2))
        self.three.clicked.connect(lambda: self.show(3))
        self.four.clicked.connect(lambda: self.show(4))
        self.five.clicked.connect(lambda: self.show(5))
        self.six.clicked.connect(lambda: self.show(6))
        self.seven.clicked.connect(lambda: self.show(7))
        self.eight.clicked.connect(lambda: self.show(8))
        self.nine.clicked.connect(lambda: self.show(9))
        self.plus.clicked.connect(lambda: self.operation("+"))
        self.minus.clicked.connect(lambda: self.operation("-"))
        self.multiply.clicked.connect(lambda: self.operation("x"))
        self.division.clicked.connect(lambda: self.operation("/"))
        self.equal.clicked.connect(self.solve)
        self.clear.clicked.connect(self.clearer)
        #self.comma.clicked.connect(lambda: self.show(","))

        global numbers1, numbers2, ends, signs, numbers3, fin
        numbers1 = []
        numbers2 = []
        numbers3 = []
        ends = []
        signs = []
        fin = 0


    def show(self,number):
        if "end" in ends or fin in numbers3:
            self.answer.insert(str(number))
            numbers2.append(str(number))
        else:
            self.answer.insert(str(number))
            numbers1.append(str(number))
            #print(numbers1)

    def operation(self,sign):
        try:
            signs.pop([0])
        except:
            ends.append("end")
            signs.append(sign)
            self.answer.insert(str(sign))

    def solve(self):
        global fin1, fin2, fin,fin_sum,fin_sub,fin_mul,fin_div
        fin1 = int("".join(numbers1))
        fin2 = int("".join(numbers2))
        print(numbers2)
        fin_sum = fin1 + fin2
        fin_sub = fin1 - fin2
        fin_mul = fin1 * fin2
        fin_div = fin1 / fin2
            #print(fin1,"\n")
            #print(fin2)
        if "+" in signs:
            self.answer.clear()
            self.answer.insert(str(fin_sum))
            fin = fin_sum
        elif "-" in signs:
            self.answer.clear()
            self.answer.insert(str(fin_sub))
            fin = fin_sub
        elif "x" in signs:
            self.answer.clear()
            self.answer.insert(str(fin_mul))
            fin = fin_mul
        elif "/" in signs:
            self.answer.clear()
            self.answer.insert("%.2f"%(fin_div))
            fin = int(fin_div)
        numbers1.clear()
        numbers2.clear()
        signs.clear()
        numbers3.append(fin)
        fin = str(fin)
        for i in str(fin):
            numbers1.append(i)
        #numbers1.append(fin.split())
        print(numbers1)

    def clearer(self):
        numbers1.clear()
        numbers2.clear()
        signs.clear()
        ends.clear()
        self.answer.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.five.setText(_translate("MainWindow", "5"))
        self.four.setText(_translate("MainWindow", "4"))
        self.six.setText(_translate("MainWindow", "6"))
        self.three.setText(_translate("MainWindow", "3"))
        self.two.setText(_translate("MainWindow", "2"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.one.setText(_translate("MainWindow", "1"))
        self.seven.setText(_translate("MainWindow", "7"))
        #self.comma.setText(_translate("MainWindow", ","))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.equal.setText(_translate("MainWindow", "="))
        self.multiply.setText(_translate("MainWindow", "X"))
        self.clear.setText(_translate("MainWindow", "C"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.division.setText(_translate("MainWindow", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
