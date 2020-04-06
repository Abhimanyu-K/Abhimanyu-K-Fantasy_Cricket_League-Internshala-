# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm6.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import math

Books=sqlite3.connect('books.db')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 711, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.Book_Title_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Book_Title_2.setFont(font)
        self.Book_Title_2.setObjectName("Book_Title_2")
        self.horizontalLayout_3.addWidget(self.Book_Title_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.l1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.l1.setText("")
        self.l1.setObjectName("l1")
        self.horizontalLayout_3.addWidget(self.l1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.b1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.findPrice)
        self.horizontalLayout_3.addWidget(self.b1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.Book_Title_4 = QtWidgets.QLabel(self.centralwidget)
        self.Book_Title_4.setGeometry(QtCore.QRect(150, 150, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Book_Title_4.setFont(font)
        self.Book_Title_4.setObjectName("Book_Title_4")
        self.Book_Title_5 = QtWidgets.QLabel(self.centralwidget)
        self.Book_Title_5.setGeometry(QtCore.QRect(150, 360, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Book_Title_5.setFont(font)
        self.Book_Title_5.setObjectName("Book_Title_5")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 240, 711, 121))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.Book_Title_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Book_Title_6.setFont(font)
        self.Book_Title_6.setObjectName("Book_Title_6")
        self.horizontalLayout_4.addWidget(self.Book_Title_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.l2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.l2.setInputMask("")
        self.l2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.l2.setObjectName("l2")
        self.horizontalLayout_4.addWidget(self.l2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.b2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.findTotal)
        self.horizontalLayout_4.addWidget(self.b2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.l3 = QtWidgets.QLineEdit(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(220, 161, 221, 31))
        self.l3.setObjectName("l3")
        self.l4 = QtWidgets.QLineEdit(self.centralwidget)
        self.l4.setGeometry(QtCore.QRect(220, 370, 221, 31))
        self.l4.setObjectName("l4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Book_Title_2.setText(_translate("MainWindow", "Book Title :"))
        self.b1.setText(_translate("MainWindow", "Find Price"))
        self.Book_Title_4.setText(_translate("MainWindow", "Price : "))
        self.Book_Title_5.setText(_translate("MainWindow", "Total :"))
        self.Book_Title_6.setText(_translate("MainWindow", "Quantity :"))
        self.b2.setText(_translate("MainWindow", "Find Total"))

    def findPrice(self):
        title=self.l1.text()
        sql="SELECT Price from books WHERE Title='"+title+"';"
        curBooks=Books.cursor()
        curBooks.execute(sql)
        price=curBooks.fetchone()
        self.l3.setText(str(price[0]))

    def findTotal(self, action):
        no=int(self.l2.text())
        title=self.l1.text()
        sql="SELECT Price from books WHERE Title='"+title+"';"
        curBooks=Books.cursor()
        curBooks.execute(sql)
        price=curBooks.fetchone()
        self.l4.setText(str(no*price[0]))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
