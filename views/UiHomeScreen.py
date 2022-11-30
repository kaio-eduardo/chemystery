# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiHomeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralWidget {\n"
                                         "background-color: transparent;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 700, 500))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 500))
        self.frame.setStyleSheet("QFrame#frame {\n"
                                 "    border-style: solid;\n"
                                 "    border-width: 2px;\n"
                                 "    border-color: black;\n"
                                 "    background-color: rgba(255,255,255, 255);    \n"
                                 "}\n"
                                 "\n"
                                 "QToolButton {\n"
                                 "padding: 5px ;\n"
                                 "color: white;\n"
                                 "background-color: rgba(165, 4, 255, 255);\n"
                                 "border: 2px solid white;\n"
                                 "border-radius: 25px;\n"
                                 "font-size: 15pt;\n"
                                 "font-weight: bold;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton:hover {\n"
                                 "    background-color: rgb(255,255,255);\n"
                                 "    color: rgba(165, 4, 255, 255);\n"
                                 "    border: 2px solid rgba(165, 4, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton:pressed {\n"
                                 "    background-color: rgb(150,150,150)\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(2, 2, 320, 496))
        self.label_2.setStyleSheet("#label_2 {\n"
                                   "background-color: rgba(165,4,255,255);\n"
                                   "padding: 2px\n"
                                   "}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(75, 50, 170, 170))
        self.pushButton_4.setStyleSheet("border-radius: 85px;\n"
                                        "image: url(:/images/images/icon 1.png);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lblUser = QtWidgets.QLabel(self.frame)
        self.lblUser.setGeometry(QtCore.QRect(10, 220, 300, 48))
        self.lblUser.setStyleSheet("background-color: transparent;\n"
                                   "font-size: 20pt;\n"
                                   "color: white;\n"
                                   "font-weight: bold")
        self.lblUser.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUser.setObjectName("lblUser")
        self.btnClose = QtWidgets.QPushButton(self.frame)
        self.btnClose.setGeometry(QtCore.QRect(660, 10, 28, 29))
        self.btnClose.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnClose.setStyleSheet("QPushButton#btnClose {\n"
                                    "border: none;\n"
                                    "background-color: transparent;\n"
                                    "color: rgba(150,0,0,120);\n"
                                    "border-radius: 10px;\n"
                                    "font-weight: bold;\n"
                                    "padding: 5px 10px 6px 10px;\n"
                                    "font-size:10pt\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#btnClose:hover {\n"
                                    "    background-color: rgba(255,0,0,100);\n"
                                    "    color: black\n"
                                    "}")
        self.btnClose.setObjectName("btnClose")
        self.startBtn = QtWidgets.QToolButton(self.frame)
        self.startBtn.setGeometry(QtCore.QRect(350, 120, 250, 50))
        self.startBtn.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/images/images/1200px-Circle-icons-rocket.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startBtn.setIcon(icon)
        self.startBtn.setIconSize(QtCore.QSize(45, 45))
        self.startBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.startBtn.setObjectName("startBtn")
        self.rankBtn = QtWidgets.QToolButton(self.frame)
        self.rankBtn.setGeometry(QtCore.QRect(350, 180, 250, 50))
        self.rankBtn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            ":/images/images/1024px-Circle-icons-trophy_(dark).svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rankBtn.setIcon(icon1)
        self.rankBtn.setIconSize(QtCore.QSize(45, 45))
        self.rankBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.rankBtn.setObjectName("rankBtn")
        self.gamesBtn = QtWidgets.QToolButton(self.frame)
        self.gamesBtn.setGeometry(QtCore.QRect(350, 240, 250, 50))
        self.gamesBtn.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            ":/images/images/icon_games.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gamesBtn.setIcon(icon2)
        self.gamesBtn.setIconSize(QtCore.QSize(45, 45))
        self.gamesBtn.setAutoRepeat(False)
        self.gamesBtn.setAutoRepeatDelay(300)
        self.gamesBtn.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.gamesBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.gamesBtn.setAutoRaise(True)
        self.gamesBtn.setArrowType(QtCore.Qt.NoArrow)
        self.gamesBtn.setObjectName("gamesBtn")
        self.aboutBtn = QtWidgets.QToolButton(self.frame)
        self.aboutBtn.setGeometry(QtCore.QRect(350, 300, 250, 50))
        self.aboutBtn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/429880.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutBtn.setIcon(icon3)
        self.aboutBtn.setIconSize(QtCore.QSize(45, 45))
        self.aboutBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.aboutBtn.setObjectName("aboutBtn")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(460, 480, 213, 10))
        self.label_6.setStyleSheet("font-size: 6pt;\n"
                                   "font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 330, 220, 120))
        self.label_3.setStyleSheet("image: url(:/images/images/logo4.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page)
        self.questionPage = QtWidgets.QWidget()
        self.questionPage.setObjectName("questionPage")
        self.label_4 = QtWidgets.QLabel(self.questionPage)
        self.label_4.setGeometry(QtCore.QRect(160, 80, 661, 321))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.questionPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblUser.setText(_translate("MainWindow", "KAIOOFERA"))
        self.btnClose.setText(_translate("MainWindow", "x"))
        self.startBtn.setText(_translate("MainWindow", "    START"))
        self.rankBtn.setText(_translate("MainWindow", "    RANK"))
        self.gamesBtn.setText(_translate("MainWindow", "    GAMES"))
        self.aboutBtn.setText(_translate("MainWindow", "    ABOUT"))
        self.label_6.setText(_translate(
            "MainWindow", "Todos os direitos reservados ao @KaioMalek, por hora"))
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:72pt; color:#ffaaff;\">PAGINA 2</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    import resHome_rc
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())