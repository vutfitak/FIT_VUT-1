# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_Calculator(object):
    def setupUi(self, MainWindow_Calculator):
        MainWindow_Calculator.setObjectName("MainWindow_Calculator")
        MainWindow_Calculator.resize(282, 545)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow_Calculator.sizePolicy().hasHeightForWidth())
        MainWindow_Calculator.setSizePolicy(sizePolicy)
        MainWindow_Calculator.setMinimumSize(QtCore.QSize(282, 545))
        MainWindow_Calculator.setMaximumSize(QtCore.QSize(282, 545))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.xpm"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow_Calculator.setWindowIcon(icon)
        MainWindow_Calculator.setStyleSheet("background-color: rgb(0, 4, 40);\n"
"color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow_Calculator)
        self.centralwidget.setStyleSheet("QPushButton {\n"
"background-color: transparent;\n"
"border-color: rgb(34, 14, 71);\n"
"color:white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 0.6);\n"
"border-style:dotted;\n"
"border-color:black;\n"
" }")
        self.centralwidget.setObjectName("centralwidget")
        self.btnOne = QtWidgets.QPushButton(self.centralwidget)
        self.btnOne.setGeometry(QtCore.QRect(0, 360, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnOne.setFont(font)
        self.btnOne.setStyleSheet("")
        self.btnOne.setObjectName("btnOne")
        self.btnTwo = QtWidgets.QPushButton(self.centralwidget)
        self.btnTwo.setGeometry(QtCore.QRect(70, 360, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnTwo.setFont(font)
        self.btnTwo.setStyleSheet("")
        self.btnTwo.setObjectName("btnTwo")
        self.btnThree = QtWidgets.QPushButton(self.centralwidget)
        self.btnThree.setGeometry(QtCore.QRect(140, 360, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnThree.setFont(font)
        self.btnThree.setStyleSheet("")
        self.btnThree.setObjectName("btnThree")
        self.btnFour = QtWidgets.QPushButton(self.centralwidget)
        self.btnFour.setGeometry(QtCore.QRect(0, 290, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnFour.setFont(font)
        self.btnFour.setStyleSheet("")
        self.btnFour.setObjectName("btnFour")
        self.btnFive = QtWidgets.QPushButton(self.centralwidget)
        self.btnFive.setGeometry(QtCore.QRect(70, 290, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnFive.setFont(font)
        self.btnFive.setStyleSheet("")
        self.btnFive.setObjectName("btnFive")
        self.btnSix = QtWidgets.QPushButton(self.centralwidget)
        self.btnSix.setGeometry(QtCore.QRect(140, 290, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnSix.setFont(font)
        self.btnSix.setStyleSheet("")
        self.btnSix.setObjectName("btnSix")
        self.btnSeven = QtWidgets.QPushButton(self.centralwidget)
        self.btnSeven.setGeometry(QtCore.QRect(0, 220, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnSeven.setFont(font)
        self.btnSeven.setStyleSheet("")
        self.btnSeven.setObjectName("btnSeven")
        self.btnEight = QtWidgets.QPushButton(self.centralwidget)
        self.btnEight.setGeometry(QtCore.QRect(70, 220, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnEight.setFont(font)
        self.btnEight.setStyleSheet("")
        self.btnEight.setObjectName("btnEight")
        self.btnNine = QtWidgets.QPushButton(self.centralwidget)
        self.btnNine.setGeometry(QtCore.QRect(140, 220, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnNine.setFont(font)
        self.btnNine.setStyleSheet("")
        self.btnNine.setObjectName("btnNine")
        self.btnZero = QtWidgets.QPushButton(self.centralwidget)
        self.btnZero.setGeometry(QtCore.QRect(0, 430, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnZero.setFont(font)
        self.btnZero.setStyleSheet("")
        self.btnZero.setObjectName("btnZero")
        self.btnEqual = QtWidgets.QPushButton(self.centralwidget)
        self.btnEqual.setGeometry(QtCore.QRect(210, 430, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnEqual.setFont(font)
        self.btnEqual.setStyleSheet("")
        self.btnEqual.setObjectName("btnEqual")
        self.btnDot = QtWidgets.QPushButton(self.centralwidget)
        self.btnDot.setGeometry(QtCore.QRect(140, 430, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnDot.setFont(font)
        self.btnDot.setStyleSheet("")
        self.btnDot.setObjectName("btnDot")
        self.btnPlus = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlus.setGeometry(QtCore.QRect(210, 360, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnPlus.setFont(font)
        self.btnPlus.setStyleSheet("")
        self.btnPlus.setObjectName("btnPlus")
        self.btnMinus = QtWidgets.QPushButton(self.centralwidget)
        self.btnMinus.setGeometry(QtCore.QRect(210, 290, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnMinus.setFont(font)
        self.btnMinus.setStyleSheet("")
        self.btnMinus.setObjectName("btnMinus")
        self.btnMul = QtWidgets.QPushButton(self.centralwidget)
        self.btnMul.setGeometry(QtCore.QRect(210, 220, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnMul.setFont(font)
        self.btnMul.setStyleSheet("")
        self.btnMul.setObjectName("btnMul")
        self.btnDiv = QtWidgets.QPushButton(self.centralwidget)
        self.btnDiv.setGeometry(QtCore.QRect(210, 150, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnDiv.setFont(font)
        self.btnDiv.setStyleSheet("")
        self.btnDiv.setObjectName("btnDiv")
        self.btnNeg = QtWidgets.QPushButton(self.centralwidget)
        self.btnNeg.setGeometry(QtCore.QRect(70, 150, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnNeg.setFont(font)
        self.btnNeg.setStyleSheet("")
        self.btnNeg.setObjectName("btnNeg")
        self.btnPower = QtWidgets.QPushButton(self.centralwidget)
        self.btnPower.setGeometry(QtCore.QRect(140, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnPower.setFont(font)
        self.btnPower.setStyleSheet("")
        self.btnPower.setObjectName("btnPower")
        self.btnSquareRoot = QtWidgets.QPushButton(self.centralwidget)
        self.btnSquareRoot.setGeometry(QtCore.QRect(210, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnSquareRoot.setFont(font)
        self.btnSquareRoot.setStyleSheet("")
        self.btnSquareRoot.setObjectName("btnSquareRoot")
        self.btnMod = QtWidgets.QPushButton(self.centralwidget)
        self.btnMod.setGeometry(QtCore.QRect(140, 150, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnMod.setFont(font)
        self.btnMod.setStyleSheet("")
        self.btnMod.setObjectName("btnMod")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(0, 150, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnClear.setFont(font)
        self.btnClear.setStyleSheet("")
        self.btnClear.setObjectName("btnClear")
        self.btnAbsolute = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbsolute.setGeometry(QtCore.QRect(70, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnAbsolute.setFont(font)
        self.btnAbsolute.setStyleSheet("")
        self.btnAbsolute.setObjectName("btnAbsolute")
        self.btnFactorial = QtWidgets.QPushButton(self.centralwidget)
        self.btnFactorial.setGeometry(QtCore.QRect(0, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setItalic(False)
        self.btnFactorial.setFont(font)
        self.btnFactorial.setStyleSheet("")
        self.btnFactorial.setObjectName("btnFactorial")
        self.textBoxDisplayyasd = QtWidgets.QLineEdit(self.centralwidget)
        self.textBoxDisplayyasd.setGeometry(QtCore.QRect(0, 0, 281, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.textBoxDisplayyasd.setFont(font)
        self.textBoxDisplayyasd.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(54, 22, 113, 255), stop:1 rgba(167, 134, 255, 255));\n"
"color: rgb(243, 243, 243);\n"
"border:none;")
        self.textBoxDisplayyasd.setText("")
        self.textBoxDisplayyasd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.textBoxDisplayyasd.setReadOnly(True)
        self.textBoxDisplayyasd.setObjectName("textBoxDisplayyasd")
        self.labelBackgroundColor = QtWidgets.QLabel(self.centralwidget)
        self.labelBackgroundColor.setGeometry(QtCore.QRect(0, 0, 281, 501))
        self.labelBackgroundColor.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(54, 22, 113, 255), stop:1 rgba(0, 4, 40, 255));")
        self.labelBackgroundColor.setText("")
        self.labelBackgroundColor.setObjectName("labelBackgroundColor")
        self.textBoxDisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBoxDisplay.setGeometry(QtCore.QRect(0, 40, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.textBoxDisplay.setFont(font)
        self.textBoxDisplay.setStyleSheet("background-color: transparent;\n"
"color: rgb(243, 243, 243);\n"
"border:none;")
        self.textBoxDisplay.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textBoxDisplay.setObjectName("textBoxDisplay")
        self.labelBackgroundColor.raise_()
        self.btnOne.raise_()
        self.btnTwo.raise_()
        self.btnThree.raise_()
        self.btnFour.raise_()
        self.btnFive.raise_()
        self.btnSix.raise_()
        self.btnSeven.raise_()
        self.btnEight.raise_()
        self.btnNine.raise_()
        self.btnZero.raise_()
        self.btnEqual.raise_()
        self.btnDot.raise_()
        self.btnPlus.raise_()
        self.btnMinus.raise_()
        self.btnMul.raise_()
        self.btnDiv.raise_()
        self.btnNeg.raise_()
        self.btnPower.raise_()
        self.btnSquareRoot.raise_()
        self.btnMod.raise_()
        self.btnClear.raise_()
        self.btnAbsolute.raise_()
        self.btnFactorial.raise_()
        self.textBoxDisplayyasd.raise_()
        self.textBoxDisplay.raise_()
        MainWindow_Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 282, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow_Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_Calculator)
        self.statusbar.setObjectName("statusbar")
        MainWindow_Calculator.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow_Calculator)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow_Calculator)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionHelp)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow_Calculator)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Calculator)
        MainWindow_Calculator.setTabOrder(self.btnZero, self.btnDot)
        MainWindow_Calculator.setTabOrder(self.btnDot, self.btnOne)
        MainWindow_Calculator.setTabOrder(self.btnOne, self.btnTwo)
        MainWindow_Calculator.setTabOrder(self.btnTwo, self.btnThree)
        MainWindow_Calculator.setTabOrder(self.btnThree, self.btnFour)
        MainWindow_Calculator.setTabOrder(self.btnFour, self.btnFive)
        MainWindow_Calculator.setTabOrder(self.btnFive, self.btnSix)
        MainWindow_Calculator.setTabOrder(self.btnSix, self.btnSeven)
        MainWindow_Calculator.setTabOrder(self.btnSeven, self.btnEight)
        MainWindow_Calculator.setTabOrder(self.btnEight, self.btnNine)
        MainWindow_Calculator.setTabOrder(self.btnNine, self.btnDiv)
        MainWindow_Calculator.setTabOrder(self.btnDiv, self.btnMul)
        MainWindow_Calculator.setTabOrder(self.btnMul, self.btnMinus)
        MainWindow_Calculator.setTabOrder(self.btnMinus, self.btnPlus)
        MainWindow_Calculator.setTabOrder(self.btnPlus, self.btnEqual)
        MainWindow_Calculator.setTabOrder(self.btnEqual, self.btnClear)
        MainWindow_Calculator.setTabOrder(self.btnClear, self.btnNeg)
        MainWindow_Calculator.setTabOrder(self.btnNeg, self.btnMod)
        MainWindow_Calculator.setTabOrder(self.btnMod, self.btnFactorial)
        MainWindow_Calculator.setTabOrder(self.btnFactorial, self.btnAbsolute)
        MainWindow_Calculator.setTabOrder(self.btnAbsolute, self.btnPower)
        MainWindow_Calculator.setTabOrder(self.btnPower, self.btnSquareRoot)
        MainWindow_Calculator.setTabOrder(self.btnSquareRoot, self.textBoxDisplayyasd)
        MainWindow_Calculator.setTabOrder(self.textBoxDisplayyasd, self.textBoxDisplay)

    def retranslateUi(self, MainWindow_Calculator):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Calculator.setWindowTitle(_translate("MainWindow_Calculator", "Calculator"))
        self.btnOne.setText(_translate("MainWindow_Calculator", "1"))
        self.btnTwo.setText(_translate("MainWindow_Calculator", "2"))
        self.btnThree.setText(_translate("MainWindow_Calculator", "3"))
        self.btnFour.setText(_translate("MainWindow_Calculator", "4"))
        self.btnFive.setText(_translate("MainWindow_Calculator", "5"))
        self.btnSix.setText(_translate("MainWindow_Calculator", "6"))
        self.btnSeven.setText(_translate("MainWindow_Calculator", "7"))
        self.btnEight.setText(_translate("MainWindow_Calculator", "8"))
        self.btnNine.setText(_translate("MainWindow_Calculator", "9"))
        self.btnZero.setText(_translate("MainWindow_Calculator", "0"))
        self.btnEqual.setText(_translate("MainWindow_Calculator", "="))
        self.btnDot.setText(_translate("MainWindow_Calculator", "."))
        self.btnPlus.setText(_translate("MainWindow_Calculator", "+"))
        self.btnMinus.setText(_translate("MainWindow_Calculator", "-"))
        self.btnMul.setText(_translate("MainWindow_Calculator", "*"))
        self.btnDiv.setText(_translate("MainWindow_Calculator", "/"))
        self.btnNeg.setText(_translate("MainWindow_Calculator", "+/-"))
        self.btnPower.setText(_translate("MainWindow_Calculator", "xʸ"))
        self.btnSquareRoot.setText(_translate("MainWindow_Calculator", "ʸ√x"))
        self.btnMod.setText(_translate("MainWindow_Calculator", "%"))
        self.btnClear.setText(_translate("MainWindow_Calculator", "C"))
        self.btnAbsolute.setText(_translate("MainWindow_Calculator", "|x|"))
        self.btnFactorial.setText(_translate("MainWindow_Calculator", "n!"))
        self.textBoxDisplay.setHtml(_translate("MainWindow_Calculator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">0</span></p></body></html>"))
        self.menuMenu.setTitle(_translate("MainWindow_Calculator", "Menu"))
        self.actionHelp.setText(_translate("MainWindow_Calculator", "Help"))
        self.actionAbout.setText(_translate("MainWindow_Calculator", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Calculator = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Calculator()
    ui.setupUi(MainWindow_Calculator)
    MainWindow_Calculator.show()
    sys.exit(app.exec_())
