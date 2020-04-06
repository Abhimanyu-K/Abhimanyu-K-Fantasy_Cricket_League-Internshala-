# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FProject.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from name_team import Ui_MainWindow as newTeam
from open_team import Ui_MainWindow as openTeam
from evaluate import Ui_MainWindow as evaluateTeam
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import math

Data=sqlite3.connect('players.db')
curData=Data.cursor()

bat_counter=0
bow_counter=0
ar_counter=0
wk_counter=0

points_used=0

class Ui_MainWindow(object):

    def __init__(self):
        self.new_team = QtWidgets.QMainWindow()
        self.new_screen = newTeam()
        self.new_screen.setupUi(self.new_team)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 612)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.yourselection = QtWidgets.QLabel(self.centralwidget)
        self.yourselection.setEnabled(True)
        self.yourselection.setGeometry(QtCore.QRect(20, 0, 759, 46))
        self.yourselection.setMinimumSize(QtCore.QSize(759, 46))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.yourselection.setFont(font)
        self.yourselection.setLineWidth(1)
        self.yourselection.setMidLineWidth(0)
        self.yourselection.setObjectName("yourselection")
        self.rBat = QtWidgets.QRadioButton(self.centralwidget)
        self.rBat.setGeometry(QtCore.QRect(50, 150, 61, 20))
        self.rBat.setObjectName("rBat")
        self.rBat.setEnabled(False)
        self.rBat.toggled.connect(self.checkstate)
        self.rAr = QtWidgets.QRadioButton(self.centralwidget)
        self.rAr.setGeometry(QtCore.QRect(210, 150, 61, 20))
        self.rAr.setObjectName("rAr")
        self.rAr.setEnabled(False)
        self.rAr.toggled.connect(self.checkstate)
        self.rWk = QtWidgets.QRadioButton(self.centralwidget)
        self.rWk.setGeometry(QtCore.QRect(290, 150, 51, 20))
        self.rWk.setObjectName("rWk")
        self.rWk.setEnabled(False)
        self.rWk.toggled.connect(self.checkstate)
        self.rBow = QtWidgets.QRadioButton(self.centralwidget)
        self.rBow.setGeometry(QtCore.QRect(120, 150, 61, 20))
        self.rBow.setObjectName("rBow")
        self.rBow.setEnabled(False)
        self.rBow.toggled.connect(self.checkstate)
        self.BAT = QtWidgets.QLabel(self.centralwidget)
        self.BAT.setGeometry(QtCore.QRect(20, 50, 93, 31))
        self.BAT.setObjectName("BAT")
        self.BOW = QtWidgets.QLabel(self.centralwidget)
        self.BOW.setGeometry(QtCore.QRect(190, 50, 111, 31))
        self.BOW.setObjectName("BOW")
        self.AR = QtWidgets.QLabel(self.centralwidget)
        self.AR.setGeometry(QtCore.QRect(380, 50, 111, 31))
        self.AR.setObjectName("AR")
        self.WK = QtWidgets.QLabel(self.centralwidget)
        self.WK.setGeometry(QtCore.QRect(580, 50, 131, 31))
        self.WK.setObjectName("WK")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(120, 50, 31, 31))
        self.l1.setObjectName("l1")
        self.l4 = QtWidgets.QLabel(self.centralwidget)
        self.l4.setGeometry(QtCore.QRect(720, 50, 31, 31))
        self.l4.setObjectName("l4")
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(500, 50, 31, 31))
        self.l3.setObjectName("l3")
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(310, 50, 31, 31))
        self.l2.setObjectName("l2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.l5 = QtWidgets.QLabel(self.centralwidget)
        self.l5.setGeometry(QtCore.QRect(170, 100, 31, 31))
        self.l5.setObjectName("l5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.l6 = QtWidgets.QLabel(self.centralwidget)
        self.l6.setGeometry(QtCore.QRect(560, 100, 31, 31))
        self.l6.setObjectName("l6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 150, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.l7 = QtWidgets.QLabel(self.centralwidget)
        self.l7.setGeometry(QtCore.QRect(560, 150, 141, 22))
        self.l7.setObjectName("l7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 80, 781, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 330, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 530, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.exit)
        self.lw2 = QtWidgets.QListWidget(self.centralwidget)
        self.lw2.setGeometry(QtCore.QRect(440, 180, 311, 341))
        self.lw2.setObjectName("lw2")
        self.lw1 = QtWidgets.QListWidget(self.centralwidget)
        self.lw1.setGeometry(QtCore.QRect(40, 180, 321, 341))
        self.lw1.setObjectName("lw1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)
        self.lw1.itemDoubleClicked.connect(self.list1_update)
        self.lw2.itemDoubleClicked.connect(self.list2_update)
        self.new_screen.save.clicked.connect(self.name_teams)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.yourselection.setText(_translate("MainWindow", "Your Selections"))
        self.rBat.setText(_translate("MainWindow", "BAT"))
        self.rAr.setText(_translate("MainWindow", "AR"))
        self.rWk.setText(_translate("MainWindow", "WK"))
        self.rBow.setText(_translate("MainWindow", "BOW"))
        self.BAT.setText(_translate("MainWindow", "Batsman(BAT)"))
        self.BOW.setText(_translate("MainWindow", "Bowler(BOW)"))
        self.AR.setText(_translate("MainWindow", "All-Rounder(AR)"))
        self.WK.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.label.setText(_translate("MainWindow", "Points Available"))
        self.label_2.setText(_translate("MainWindow", "Points Used"))
        self.label_3.setText(_translate("MainWindow", "Team Name"))
        self.label_4.setText(_translate("MainWindow", ">"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    #method to display names of players in listwidget by accessing it from database
    def display_names(self, var):
        sql="SELECT Player from stats WHERE ctg='"+var+"';"
        curData.execute(sql)
        var1=curData.fetchall()
        for data in var1:
            self.lw1.addItem(data[0])
        self.l1.setText(str(bat_counter))
        self.l2.setText(str(bow_counter))
        self.l3.setText(str(ar_counter))
        self.l4.setText(str(wk_counter))
        
    #method to give number of bats,bow,ar,wk and
    #also call the method which will ondoubleclick(item) remove item from list1 and add to list 2    
    def list1_update(self,item):
        if self.rBat.isChecked() and globals()['bat_counter']<5:
            globals()['bat_counter']=globals()['bat_counter']+1
            self.l1.setText(str(bat_counter))
            self.new1(item)
        if self.rBow.isChecked():
            globals()['bow_counter']=globals()['bow_counter']+1           
            self.l2.setText(str(bow_counter))
            self.new1(item)
        if self.rAr.isChecked():
            globals()['ar_counter']=globals()['ar_counter']+1
            self.l3.setText(str(ar_counter))
            self.new1(item)
        if self.rWk.isChecked():
            if globals()['wk_counter']>0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("You cannot select more than one Wicket-Keeper")
                msg.exec_()
            #msg box if more than one wicket keeper is selected
            else:
                globals()['wk_counter']=globals()['wk_counter']+1            
                self.l4.setText(str(wk_counter))
                self.new1(item)
        
    #method to give/update number of bats,bow,ar,wk and
    #also call the method which will ondoubleclick(item) remove item from list2    
    
    def list2_update(self, item):
        if self.rBat.isChecked() and globals()['bat_counter']>0:
            globals()['bat_counter']=globals()['bat_counter']-1
            self.l1.setText(str(bat_counter))
            self.new2(item)
        elif self.rBow.isChecked() and globals()['bow_counter']>0:
            globals()['bow_counter']=globals()['bow_counter']-1
            self.l2.setText(str(bow_counter))
            self.new2(item)
        elif self.rAr.isChecked() and globals()['ar_counter']>0:
            globals()['ar_counter']=globals()['ar_counter']-1
            self.l3.setText(str(ar_counter))
            self.new2(item)
        elif self.rWk.isChecked() and globals()['wk_counter']>0:
            globals()['wk_counter']=globals()['wk_counter']-1
            self.l4.setText(str(wk_counter))
            self.new2(item)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Remove the player where player count is greater than 0")
            msg.exec_()

    #method to perform list widget actions and give point used and point avaialble
    def new1(self,item):
        self.lw1.takeItem(self.lw1.row(item))
        self.lw2.addItem(item.text())
        item=item.text()
        curData.execute("SELECT Points FROM match WHERE Player = '" + item + "';")
        player_pt=curData.fetchall()
        current_pt=self.l5.text()
        current_pt=int(current_pt)-int(player_pt[0][0])
        self.l5.setText(str(current_pt))
        used_pt=self.l6.text()
        add_pt=int(used_pt)+int(player_pt[0][0])
        self.l6.setText(str(add_pt))
    #method to remove list2 items from list
    def new2(self,item):
        self.lw2.takeItem(self.lw2.row(item))
    
    #when Bat radiobutton is clicked.. displays the player list from database   
    def bat(self):
        var="BAT"
        self.lw1.clear()
        self.display_names(var)

    #when Bow radiobutton is clicked.. displays the player list from database   
    def bow(self):
        var="BWL"
        self.lw1.clear()
        self.display_names(var)

    #when ar radiobutton is clicked.. displays the player list from database   
    def ar(self):
        var="AR"
        self.lw1.clear()
        self.display_names(var)

    #when wk radiobutton is clicked.. displays the player list from database   
    def wk(self):
        var="WK"
        self.lw1.clear()
        self.display_names(var)

    #checks which radiobutton is enabled and perform actions accordingly
    def checkstate(self):
        self.rBat.setEnabled(True)
        self.rBow.setEnabled(True)
        self.rAr.setEnabled(True)
        self.rWk.setEnabled(True)
        if self.rBat.isChecked()==True:
            self.bat()
        elif self.rBow.isChecked()==True:
            self.bow()
        elif self.rAr.isChecked()==True:
            self.ar()
        elif self.rWk.isChecked()==True:
            self.wk()

    #to Close the gui
    def exit(self):
        import sys
        self.showdlg("Are you sure,Press OK to exit")
        sys.exit()

    #in continuation to exit method
    def showdlg(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Fantasy cricket team")
        ret=Dialog.exec()

    #which action or method to perform on menufunction
    def menufunction(self, action):
        txt=(action.text())
        if txt=='NEW team':
            self.name_teams()
            self.show_points()
            self.checkstate()
        if txt=='OPEN Team':
            self.open_teams()
        if txt=='SAVE Team':
            self.save()
        if txt=='EVALUATE Team':
            self.evaluate()

    #to display point used as well as available points        
    def show_points(self):
        curData.execute('SELECT SUM(Points) from match')
        points = curData.fetchall()
        self.l5.setText(str(points[0][0]))
        self.l6.setText(str(points_used))

    #method to open team on search from database
    def open_teams(self):
        self.open_team = QtWidgets.QMainWindow()
        self.open_screen = openTeam()
        self.open_screen.setupUi(self.open_team)
        self.open_team.show()

    #To enter the team name and save
    def name_teams(self):
        self.new_team.show()
        teamName = self.new_screen.linetname.text()
        if teamName=='':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Team Name cannot be empty")
            msg.exec_()
        self.l7.setText(str(teamName))

    #to evaluate scores 
    def evaluate(self):
        self.evaluate_team = QtWidgets.QMainWindow()
        self.evaluate_screen = evaluateTeam()
        self.evaluate_screen.setupUi(self.evaluate_team)
        self.evaluate_team.show()

    #to save a team selected
    def save(self):
        team_list = []
        team_name = self.l7.text()
        curData.execute("SELECT match FROM Team WHERE team_name='"+team_name+"';")
        data = curData.fetchall()
        if len(data) is not 0:
            match = data[len(data)-1][0]
            a = match.split(match[len(match)-1])
            b = match.split('match')
            b[1] = int(b[1])+1
            matches = a[0]+str(b[1])
        else:
            matches = 'Match_1'
        for item in range(self.lw2.count()):
            team_list.append(self.lw2.item(item).text())
        for item in team_list:
            curData.execute("SELECT Points FROM match WHERE Player = '" + item + "';")
            Scored = curData.fetchall()
            curData.execute('INSERT INTO Team VALUES (?,?,?,?)', (team_name, item, Scored[0][0], matches))
            Data.commit()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
