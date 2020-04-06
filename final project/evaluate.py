# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Score import Ui_MainWindow as ScoreTeam
import sqlite3
conn = sqlite3.connect('players.db')
cur = conn.cursor()


class Ui_MainWindow(object):
    def __init__(self):
        self.score_team = QtWidgets.QMainWindow()
        self.score_screen = ScoreTeam()
        self.score_screen.setupUi(self.score_team)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.teams = QtWidgets.QComboBox(self.centralwidget)
        self.teams.setGeometry(QtCore.QRect(130, 60, 151, 31))
        self.teams.setObjectName("teams")
        self.matches = QtWidgets.QComboBox(self.centralwidget)
        self.matches.setGeometry(QtCore.QRect(480, 60, 151, 31))
        self.matches.setObjectName("matches")
        self.matches.addItem("")
        self.matches.addItem("")
        self.matches.addItem("")
        self.matches.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 100, 721, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 130, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 130, 61, 31))
        self.label_3.setObjectName("label_3")
        self.listPlayers = QtWidgets.QListWidget(self.centralwidget)
        self.listPlayers.setGeometry(QtCore.QRect(80, 170, 291, 331))
        self.listPlayers.setObjectName("listPlayers")
        self.listPoints = QtWidgets.QListWidget(self.centralwidget)
        self.listPoints.setGeometry(QtCore.QRect(430, 170, 291, 331))
        self.listPoints.setObjectName("listPoints")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 510, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.e_points = QtWidgets.QLabel(self.centralwidget)
        self.e_points.setGeometry(QtCore.QRect(510, 140, 55, 16))
        self.e_points.setText("")
        self.e_points.setObjectName("e_points")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.teams.activated.connect(self.matchesShow)
        self.matches.activated.connect(self.dataShow)
        self.pushButton.clicked.connect(self.calculateWindow)

        cur.execute("SELECT team_name FROM Team")
        team_data = cur.fetchall()
        team_data = list(set(team_data))
        for data in team_data:
            self.teams.addItem(data[0])

    def matchesShow(self):
        value = self.teams.currentText()
        cur.execute("SELECT match FROM Team WHERE team_name = '" + value + "'")
        play_match = cur.fetchall()
        play_match = list(set(play_match))
        play_match.sort()
        self.matches.clear()
        for match in play_match:            
            self.matches.addItem(match[0])

    def dataShow(self):
        value = self.matches.currentText()
        cur.execute("SELECT Players , Scored FROM Team WHERE match = '"+ value +"'")
        play_data = cur.fetchall()
        self.listPlayers.clear()
        self.listPoints.clear()
        for data in play_data:
            self.listPlayers.addItem(data[0])
            self.listPoints.addItem(str(data[1]))

    def calculateWindow(self):
        items = []
        for index in range(self.listPoints.count()):
            item = self.listPoints.item(index)
            items.append(int(item.text()))
        print(sum(items))
        self.score_screen.final_score.setText(str(sum(items)))
        self.score_team.show()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.teams.setItemText(0, _translate("MainWindow", "Team1"))
        self.teams.setItemText(1, _translate("MainWindow", "Team2"))
        self.teams.setItemText(2, _translate("MainWindow", "Team3"))
        self.matches.setItemText(0, _translate("MainWindow", "Match_1"))
        self.matches.setItemText(1, _translate("MainWindow", "Match_2"))
        self.matches.setItemText(2, _translate("MainWindow", "Match_3"))
        self.matches.setItemText(3, _translate("MainWindow", "Match_4"))
        self.label.setText(_translate("MainWindow", "Evaluate the performance of your Fantasy Team"))
        self.label_2.setText(_translate("MainWindow", "Players"))
        self.label_3.setText(_translate("MainWindow", "Points"))
        self.pushButton.setText(_translate("MainWindow", "Calculate Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
