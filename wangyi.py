# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wangyi.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 450)
        MainWindow.setStyleSheet("QPushButton:pressed {\n"
                                 "    background-color: rgb(0, 0, 0);\n"
                                 "    border-style: inset;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 661, 441))
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
                                     "    alignment: left;\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:hover {\n"
                                     "    background: #98468f;\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:selected {\n"
                                     "    border-color: #3a3a3f;\n"
                                     "    color: red;\n"
                                     "    border-bottom-color: #5c3de4;\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab {\n"
                                     "    background: #006ff000;\n"
                                     "    border: none;\n"
                                     "    border-bottom: 2px solid #3c3e42;\n"
                                     "    min-width: 10px;\n"
                                     "    margin-right: 8px;\n"
                                     "    padding-left: 20px;\n"
                                     "    padding-right: 20px;\n"
                                     "    padding-top: 10px;\n"
                                     "    padding-bottom: 10px;\n"
                                     "    color: #6656e6;\n"
                                     "}")
        self.tabWidget.setObjectName("tabWidget")
        self.wangyitab = QtWidgets.QWidget()
        self.wangyitab.setObjectName("wangyitab")
        self.layoutWidget = QtWidgets.QWidget(self.wangyitab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 651, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.songlabel = QtWidgets.QLabel(self.layoutWidget)
        self.songlabel.setStyleSheet("border-style:none;\n"
                                     "border-radius:6px;\n"
                                     "background:transparent;\n"
                                     "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                     "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                     "border-top:1px solid #3a3a3f;\n"
                                     "border-right:1px solid #3a3a3f;\n"
                                     "border-left:1px solid #3a3a3f;")
        self.songlabel.setObjectName("songlabel")
        self.horizontalLayout.addWidget(self.songlabel)
        self.songedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.songedit.setMinimumSize(QtCore.QSize(158, 31))
        self.songedit.setMaximumSize(QtCore.QSize(480, 31))
        self.songedit.setStyleSheet("border-style:none;\n"
                                    "border-radius:6px;\n"
                                    "background:transparent;\n"
                                    "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                    "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                    "border-top:1px solid #3a3a3f;\n"
                                    "border-right:1px solid #3a3a3f;\n"
                                    "border-left:1px solid #3a3a3f;")
        self.songedit.setObjectName("songedit")
        self.horizontalLayout.addWidget(self.songedit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.songlist = QtWidgets.QListWidget(self.layoutWidget)
        self.songlist.setStyleSheet("border-style:none;\n"
                                    "border-radius:6px;\n"
                                    "background:transparent;\n"
                                    "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                    "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                    "border-top:1px solid #3a3a3f;\n"
                                    "border-right:1px solid #3a3a3f;\n"
                                    "border-left:1px solid #3a3a3f;")
        self.songlist.setObjectName("songlist")
        self.verticalLayout.addWidget(self.songlist)
        self.pathedit = QtWidgets.QLineEdit(self.layoutWidget)
        self.pathedit.setStyleSheet("border-style:none;\n"
                                    "border-radius:6px;\n"
                                    "background:transparent;\n"
                                    "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                    "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                    "border-top:1px solid #3a3a3f;\n"
                                    "border-right:1px solid #3a3a3f;\n"
                                    "border-left:1px solid #3a3a3f;")
        self.pathedit.setObjectName("pathedit")
        self.verticalLayout.addWidget(self.pathedit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnsave = QtWidgets.QPushButton(self.layoutWidget)
        self.btnsave.setMinimumSize(QtCore.QSize(60, 45))
        self.btnsave.setMaximumSize(QtCore.QSize(120, 45))
        self.btnsave.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                   "color: rgb(251, 0, 242);\n"
                                   "border-style:none;\n"
                                   "border-radius:6px;\n"
                                   "background:transparent;\n"
                                   "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                   "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                   "border-top:1px solid #3a3a3f;\n"
                                   "border-right:1px solid #3a3a3f;\n"
                                   "border-left:1px solid #3a3a3f;")
        self.btnsave.setObjectName("btnsave")
        self.horizontalLayout_2.addWidget(self.btnsave)
        self.btnstart = QtWidgets.QPushButton(self.layoutWidget)
        self.btnstart.setMinimumSize(QtCore.QSize(60, 45))
        self.btnstart.setMaximumSize(QtCore.QSize(111, 45))
        self.btnstart.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                    "color: rgb(251, 0, 242);\n"
                                    "border-style:none;\n"
                                    "border-radius:6px;\n"
                                    "background:transparent;\n"
                                    "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                    "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                    "border-top:1px solid #3a3a3f;\n"
                                    "border-right:1px solid #3a3a3f;\n"
                                    "border-left:1px solid #3a3a3f;")
        self.btnstart.setObjectName("btnstart")
        self.horizontalLayout_2.addWidget(self.btnstart)
        self.btnexit = QtWidgets.QPushButton(self.layoutWidget)
        self.btnexit.setMinimumSize(QtCore.QSize(60, 45))
        self.btnexit.setMaximumSize(QtCore.QSize(113, 45))
        self.btnexit.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                   "color: rgb(251, 0, 242);\n"
                                   "border-style:none;\n"
                                   "border-radius:6px;\n"
                                   "background:transparent;\n"
                                   "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                   "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                   "border-top:1px solid #3a3a3f;\n"
                                   "border-right:1px solid #3a3a3f;\n"
                                   "border-left:1px solid #3a3a3f;")
        self.btnexit.setObjectName("btnexit")
        self.horizontalLayout_2.addWidget(self.btnexit)
        self.btnabout = QtWidgets.QPushButton(self.layoutWidget)
        self.btnabout.setMinimumSize(QtCore.QSize(60, 45))
        self.btnabout.setMaximumSize(QtCore.QSize(113, 45))
        self.btnabout.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                    "color: rgb(251, 0, 242);\n"
                                    "border-style:none;\n"
                                    "border-radius:6px;\n"
                                    "background:transparent;\n"
                                    "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                    "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                    "border-top:1px solid #3a3a3f;\n"
                                    "border-right:1px solid #3a3a3f;\n"
                                    "border-left:1px solid #3a3a3f;")
        self.btnabout.setObjectName("btnabout")
        self.horizontalLayout_2.addWidget(self.btnabout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.wangyitab, "")
        self.tabshipin = QtWidgets.QWidget()
        self.tabshipin.setObjectName("tabshipin")
        self.layoutWidget1 = QtWidgets.QWidget(self.tabshipin)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 4, 663, 391))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(2, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.shipinlabel = QtWidgets.QLabel(self.layoutWidget1)
        self.shipinlabel.setMinimumSize(QtCore.QSize(60, 31))
        self.shipinlabel.setMaximumSize(QtCore.QSize(148, 31))
        self.shipinlabel.setStyleSheet("border-style:none;\n"
                                       "border-radius:6px;\n"
                                       "background:transparent;\n"
                                       "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                       "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                       "border-top:1px solid #3a3a3f;\n"
                                       "border-right:1px solid #3a3a3f;\n"
                                       "border-left:1px solid #3a3a3f;")
        self.shipinlabel.setObjectName("shipinlabel")
        self.verticalLayout_6.addWidget(self.shipinlabel)
        self.btnsaveshipin = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnsaveshipin.setMinimumSize(QtCore.QSize(60, 31))
        self.btnsaveshipin.setMaximumSize(QtCore.QSize(148, 31))
        self.btnsaveshipin.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                         "color: rgb(251, 0, 242);\n"
                                         "border-style:none;\n"
                                         "border-radius:6px;\n"
                                         "background:transparent;\n"
                                         "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                         "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                         "border-top:1px solid #3a3a3f;\n"
                                         "border-right:1px solid #3a3a3f;\n"
                                         "border-left:1px solid #3a3a3f;")
        self.btnsaveshipin.setObjectName("btnsaveshipin")
        self.verticalLayout_6.addWidget(self.btnsaveshipin)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.shipinedit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.shipinedit.setMinimumSize(QtCore.QSize(158, 31))
        self.shipinedit.setMaximumSize(QtCore.QSize(480, 31))
        self.shipinedit.setStyleSheet("border-style:none;\n"
                                      "border-radius:6px;\n"
                                      "background:transparent;\n"
                                      "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                      "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                      "border-top:1px solid #3a3a3f;\n"
                                      "border-right:1px solid #3a3a3f;\n"
                                      "border-left:1px solid #3a3a3f;\n"
                                      "")
        self.shipinedit.setObjectName("shipinedit")
        self.verticalLayout_5.addWidget(self.shipinedit)
        self.patheditshipin = QtWidgets.QLineEdit(self.layoutWidget1)
        self.patheditshipin.setMinimumSize(QtCore.QSize(158, 32))
        self.patheditshipin.setMaximumSize(QtCore.QSize(480, 32))
        self.patheditshipin.setStyleSheet("border-style:none;\n"
                                          "border-radius:6px;\n"
                                          "background:transparent;\n"
                                          "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                          "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                          "border-top:1px solid #3a3a3f;\n"
                                          "border-right:1px solid #3a3a3f;\n"
                                          "border-left:1px solid #3a3a3f;")
        self.patheditshipin.setObjectName("patheditshipin")
        self.verticalLayout_5.addWidget(self.patheditshipin)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButtonlist = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButtonlist.setMinimumSize(QtCore.QSize(60, 30))
        self.radioButtonlist.setMaximumSize(QtCore.QSize(300, 30))
        self.radioButtonlist.setStyleSheet("border-style:none;\n"
                                           "border-radius:6px;\n"
                                           "background:transparent;\n"
                                           "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                           "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                           "border-top:1px solid #3a3a3f;\n"
                                           "border-right:1px solid #3a3a3f;\n"
                                           "border-left:1px solid #3a3a3f;")
        self.radioButtonlist.setObjectName("radioButtonlist")
        self.verticalLayout_4.addWidget(self.radioButtonlist)
        self.radioButton1080 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton1080.setMinimumSize(QtCore.QSize(60, 30))
        self.radioButton1080.setMaximumSize(QtCore.QSize(300, 30))
        self.radioButton1080.setStyleSheet("border-style:none;\n"
                                           "border-radius:6px;\n"
                                           "background:transparent;\n"
                                           "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                           "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                           "border-top:1px solid #3a3a3f;\n"
                                           "border-right:1px solid #3a3a3f;\n"
                                           "border-left:1px solid #3a3a3f;")
        self.radioButton1080.setObjectName("radioButton1080")
        self.verticalLayout_4.addWidget(self.radioButton1080)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton360 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton360.setMinimumSize(QtCore.QSize(60, 30))
        self.radioButton360.setMaximumSize(QtCore.QSize(308, 30))
        self.radioButton360.setStyleSheet("border-style:none;\n"
                                          "border-radius:6px;\n"
                                          "background:transparent;\n"
                                          "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                          "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                          "border-top:1px solid #3a3a3f;\n"
                                          "border-right:1px solid #3a3a3f;\n"
                                          "border-left:1px solid #3a3a3f;")
        self.radioButton360.setObjectName("radioButton360")
        self.verticalLayout_3.addWidget(self.radioButton360)
        self.radioButton720 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton720.setMinimumSize(QtCore.QSize(60, 30))
        self.radioButton720.setMaximumSize(QtCore.QSize(308, 30))
        self.radioButton720.setStyleSheet("border-style:none;\n"
                                          "border-radius:6px;\n"
                                          "background:transparent;\n"
                                          "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                          "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                          "border-top:1px solid #3a3a3f;\n"
                                          "border-right:1px solid #3a3a3f;\n"
                                          "border-left:1px solid #3a3a3f;")
        self.radioButton720.setObjectName("radioButton720")
        self.verticalLayout_3.addWidget(self.radioButton720)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.shipinlistshipin = QtWidgets.QListWidget(self.layoutWidget1)
        self.shipinlistshipin.setMinimumSize(QtCore.QSize(158, 148))
        self.shipinlistshipin.setMaximumSize(QtCore.QSize(646, 148))
        self.shipinlistshipin.setStyleSheet("border-style:none;\n"
                                            "border-radius:6px;\n"
                                            "background:transparent;\n"
                                            "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                            "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                            "border-top:1px solid #3a3a3f;\n"
                                            "border-right:1px solid #3a3a3f;\n"
                                            "border-left:1px solid #3a3a3f;")
        self.shipinlistshipin.setObjectName("shipinlistshipin")
        self.verticalLayout_7.addWidget(self.shipinlistshipin)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ptnnchangebackgroud = QtWidgets.QPushButton(self.layoutWidget1)
        self.ptnnchangebackgroud.setMinimumSize(QtCore.QSize(60, 31))
        self.ptnnchangebackgroud.setMaximumSize(QtCore.QSize(104, 31))
        self.ptnnchangebackgroud.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                               "color: rgb(251, 0, 242);\n"
                                               "border-style:none;\n"
                                               "border-radius:6px;\n"
                                               "background:transparent;\n"
                                               "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                               "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                               "border-top:1px solid #3a3a3f;\n"
                                               "border-right:1px solid #3a3a3f;\n"
                                               "border-left:1px solid #3a3a3f;")
        self.ptnnchangebackgroud.setObjectName("ptnnchangebackgroud")
        self.horizontalLayout_6.addWidget(self.ptnnchangebackgroud)
        self.btnstartshipin = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnstartshipin.setMinimumSize(QtCore.QSize(60, 31))
        self.btnstartshipin.setMaximumSize(QtCore.QSize(104, 31))
        self.btnstartshipin.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                          "color: rgb(251, 0, 242);\n"
                                          "border-style:none;\n"
                                          "border-radius:6px;\n"
                                          "background:transparent;\n"
                                          "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                          "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                          "border-top:1px solid #3a3a3f;\n"
                                          "border-right:1px solid #3a3a3f;\n"
                                          "border-left:1px solid #3a3a3f;")
        self.btnstartshipin.setObjectName("btnstartshipin")
        self.horizontalLayout_6.addWidget(self.btnstartshipin)
        self.btnexitshipin = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnexitshipin.setMinimumSize(QtCore.QSize(60, 31))
        self.btnexitshipin.setMaximumSize(QtCore.QSize(104, 31))
        self.btnexitshipin.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                         "color: rgb(251, 0, 242);\n"
                                         "border-style:none;\n"
                                         "border-radius:6px;\n"
                                         "background:transparent;\n"
                                         "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                         "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                         "border-top:1px solid #3a3a3f;\n"
                                         "border-right:1px solid #3a3a3f;\n"
                                         "border-left:1px solid #3a3a3f;")
        self.btnexitshipin.setObjectName("btnexitshipin")
        self.horizontalLayout_6.addWidget(self.btnexitshipin)
        self.btnaboutshipin = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnaboutshipin.setMinimumSize(QtCore.QSize(60, 31))
        self.btnaboutshipin.setMaximumSize(QtCore.QSize(104, 31))
        self.btnaboutshipin.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                          "color: rgb(251, 0, 242);\n"
                                          "border-style:none;\n"
                                          "border-radius:6px;\n"
                                          "background:transparent;\n"
                                          "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                          "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                          "border-top:1px solid #3a3a3f;\n"
                                          "border-right:1px solid #3a3a3f;\n"
                                          "border-left:1px solid #3a3a3f;")
        self.btnaboutshipin.setObjectName("btnaboutshipin")
        self.horizontalLayout_6.addWidget(self.btnaboutshipin)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tabshipin, "")
        self.tabquanwang = QtWidgets.QWidget()
        self.tabquanwang.setObjectName("tabquanwang")
        self.widget = QtWidgets.QWidget(self.tabquanwang)
        self.widget.setGeometry(QtCore.QRect(0, 0, 671, 391))
        self.widget.setObjectName("widget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(158, 32))
        self.label.setMaximumSize(QtCore.QSize(98, 32))
        self.label.setStyleSheet("border-style:none;\n"
                                 "border-radius:6px;\n"
                                 "background:transparent;\n"
                                 "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                 "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                 "border-top:1px solid #3a3a3f;\n"
                                 "border-right:1px solid #3a3a3f;\n"
                                 "border-left:1px solid #3a3a3f;")
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.editurl = QtWidgets.QLineEdit(self.widget)
        self.editurl.setMinimumSize(QtCore.QSize(158, 32))
        self.editurl.setMaximumSize(QtCore.QSize(480, 32))
        self.editurl.setStyleSheet("border-style:none;\n"
                                   "border-radius:6px;\n"
                                   "background:transparent;\n"
                                   "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                   "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                   "border-top:1px solid #3a3a3f;\n"
                                   "border-right:1px solid #3a3a3f;\n"
                                   "border-left:1px solid #3a3a3f;")
        self.editurl.setObjectName("editurl")
        self.horizontalLayout_8.addWidget(self.editurl)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.rbtn4 = QtWidgets.QRadioButton(self.widget)
        self.rbtn4.setMinimumSize(QtCore.QSize(120, 32))
        self.rbtn4.setMaximumSize(QtCore.QSize(108, 32))
        self.rbtn4.setStyleSheet("border-style:none;\n"
                                 "border-radius:6px;\n"
                                 "background:transparent;\n"
                                 "border-bottom: 1px solid #3a3a3f;min-width: 98px;margin-right: 8px;\n"
                                 "padding-left:8px;padding-right:4px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                 "border-top:1px solid #3a3a3f;\n"
                                 "border-right:1px solid #3a3a3f;\n"
                                 "border-left:1px solid #3a3a3f;")
        self.rbtn4.setObjectName("rbtn4")
        self.horizontalLayout_9.addWidget(self.rbtn4)
        self.rbtn5 = QtWidgets.QRadioButton(self.widget)
        self.rbtn5.setMinimumSize(QtCore.QSize(120, 32))
        self.rbtn5.setMaximumSize(QtCore.QSize(108, 32))
        self.rbtn5.setStyleSheet("border-style:none;\n"
                                 "border-radius:6px;\n"
                                 "background:transparent;\n"
                                 "border-bottom: 1px solid #3a3a3f;min-width: 98px;margin-right: 8px;\n"
                                 "padding-left:8px;padding-right:4px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                 "border-top:1px solid #3a3a3f;\n"
                                 "border-right:1px solid #3a3a3f;\n"
                                 "border-left:1px solid #3a3a3f;")
        self.rbtn5.setObjectName("rbtn5")
        self.horizontalLayout_9.addWidget(self.rbtn5)
        self.rbtn1 = QtWidgets.QRadioButton(self.widget)
        self.rbtn1.setMinimumSize(QtCore.QSize(120, 32))
        self.rbtn1.setMaximumSize(QtCore.QSize(108, 32))
        self.rbtn1.setStyleSheet("border-style:none;\n"
                                 "border-radius:6px;\n"
                                 "background:transparent;\n"
                                 "border-bottom: 1px solid #3a3a3f;min-width: 98px;margin-right: 8px;\n"
                                 "padding-left:8px;padding-right:4px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                 "border-top:1px solid #3a3a3f;\n"
                                 "border-right:1px solid #3a3a3f;\n"
                                 "border-left:1px solid #3a3a3f;")
        self.rbtn1.setObjectName("rbtn1")
        self.horizontalLayout_9.addWidget(self.rbtn1)
        self.rbtn2 = QtWidgets.QRadioButton(self.widget)
        self.rbtn2.setMinimumSize(QtCore.QSize(120, 32))
        self.rbtn2.setMaximumSize(QtCore.QSize(108, 32))
        self.rbtn2.setStyleSheet("border-style:none;\n"
                                 "border-radius:6px;\n"
                                 "background:transparent;\n"
                                 "border-bottom: 1px solid #3a3a3f;min-width: 98px;margin-right: 8px;\n"
                                 "padding-left:8px;padding-right:4px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                 "border-top:1px solid #3a3a3f;\n"
                                 "border-right:1px solid #3a3a3f;\n"
                                 "border-left:1px solid #3a3a3f;")
        self.rbtn2.setObjectName("rbtn2")
        self.horizontalLayout_9.addWidget(self.rbtn2)
        self.rbtn3 = QtWidgets.QRadioButton(self.widget)
        self.rbtn3.setMinimumSize(QtCore.QSize(120, 32))
        self.rbtn3.setMaximumSize(QtCore.QSize(108, 32))
        self.rbtn3.setStyleSheet("border-style:none;\n"
                                 "border-radius:6px;\n"
                                 "background:transparent;\n"
                                 "border-bottom: 1px solid #3a3a3f;min-width: 98px;margin-right: 8px;\n"
                                 "padding-left:8px;padding-right:4px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                 "border-top:1px solid #3a3a3f;\n"
                                 "border-right:1px solid #3a3a3f;\n"
                                 "border-left:1px solid #3a3a3f;")
        self.rbtn3.setObjectName("rbtn3")
        self.horizontalLayout_9.addWidget(self.rbtn3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btnbofang = QtWidgets.QPushButton(self.widget)
        self.btnbofang.setMinimumSize(QtCore.QSize(60, 32))
        self.btnbofang.setMaximumSize(QtCore.QSize(108, 32))
        self.btnbofang.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                     "color: rgb(251, 0, 242);\n"
                                     "border-style:none;\n"
                                     "border-radius:6px;\n"
                                     "background:transparent;\n"
                                     "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                     "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                     "border-top:1px solid #3a3a3f;\n"
                                     "border-right:1px solid #3a3a3f;\n"
                                     "border-left:1px solid #3a3a3f;")
        self.btnbofang.setObjectName("btnbofang")
        self.horizontalLayout_10.addWidget(self.btnbofang)
        self.btnqingchu = QtWidgets.QPushButton(self.widget)
        self.btnqingchu.setMinimumSize(QtCore.QSize(60, 32))
        self.btnqingchu.setMaximumSize(QtCore.QSize(108, 32))
        self.btnqingchu.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                      "color: rgb(251, 0, 242);\n"
                                      "border-style:none;\n"
                                      "border-radius:6px;\n"
                                      "background:transparent;\n"
                                      "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                      "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                      "border-top:1px solid #3a3a3f;\n"
                                      "border-right:1px solid #3a3a3f;\n"
                                      "border-left:1px solid #3a3a3f;")
        self.btnqingchu.setObjectName("btnqingchu")
        self.horizontalLayout_10.addWidget(self.btnqingchu)
        self.btnabout_2 = QtWidgets.QPushButton(self.widget)
        self.btnabout_2.setMinimumSize(QtCore.QSize(60, 32))
        self.btnabout_2.setMaximumSize(QtCore.QSize(108, 32))
        self.btnabout_2.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                      "color: rgb(251, 0, 242);\n"
                                      "border-style:none;\n"
                                      "border-radius:6px;\n"
                                      "background:transparent;\n"
                                      "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                      "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                      "border-top:1px solid #3a3a3f;\n"
                                      "border-right:1px solid #3a3a3f;\n"
                                      "border-left:1px solid #3a3a3f;")
        self.btnabout_2.setObjectName("btnabout_2")
        self.horizontalLayout_10.addWidget(self.btnabout_2)
        self.btnexit_2 = QtWidgets.QPushButton(self.widget)
        self.btnexit_2.setMinimumSize(QtCore.QSize(60, 32))
        self.btnexit_2.setMaximumSize(QtCore.QSize(108, 32))
        self.btnexit_2.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                     "color: rgb(251, 0, 242);\n"
                                     "border-style:none;\n"
                                     "border-radius:6px;\n"
                                     "background:transparent;\n"
                                     "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                     "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                     "border-top:1px solid #3a3a3f;\n"
                                     "border-right:1px solid #3a3a3f;\n"
                                     "border-left:1px solid #3a3a3f;")
        self.btnexit_2.setObjectName("btnexit_2")
        self.horizontalLayout_10.addWidget(self.btnexit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setMinimumSize(QtCore.QSize(158, 200))
        self.textBrowser.setMaximumSize(QtCore.QSize(688, 288))
        self.textBrowser.setStyleSheet("border-style:none;\n"
                                       "border-radius:6px;\n"
                                       "background:transparent;\n"
                                       "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                       "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                       "border-top:1px solid #3a3a3f;\n"
                                       "border-right:1px solid #3a3a3f;\n"
                                       "border-left:1px solid #3a3a3f;")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout_13.addLayout(self.verticalLayout_2)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.textBrowser.raise_()
        self.textBrowser.raise_()
        self.tabWidget.addTab(self.tabquanwang, "")
        self.tabqrcode = QtWidgets.QWidget()
        self.tabqrcode.setObjectName("tabqrcode")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tabqrcode)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 651, 391))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(2, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btnpicture = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnpicture.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                      "color:#186a6e;\n"
                                      "border-style:none;\n"
                                      "border-radius:6px;\n"
                                      "background:transparent;\n"
                                      "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                      "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                      "border-top:1px solid #3a3a3f;\n"
                                      "border-right:1px solid #3a3a3f;\n"
                                      "border-left:1px solid #3a3a3f;")
        self.btnpicture.setObjectName("btnpicture")
        self.verticalLayout_9.addWidget(self.btnpicture)
        self.btnpicleixing = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnpicleixing.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                         "color:#186a6e;\n"
                                         "border-style:none;\n"
                                         "border-radius:6px;\n"
                                         "background:transparent;\n"
                                         "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                         "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                         "border-top:1px solid #3a3a3f;\n"
                                         "border-right:1px solid #3a3a3f;\n"
                                         "border-left:1px solid #3a3a3f;")
        self.btnpicleixing.setObjectName("btnpicleixing")
        self.verticalLayout_9.addWidget(self.btnpicleixing)
        self.btnqrcodeurl = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnqrcodeurl.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                        "color: rgb(251, 0, 242);\n"
                                        "border-style:none;\n"
                                        "border-radius:6px;\n"
                                        "background:transparent;\n"
                                        "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                        "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                        "border-top:1px solid #3a3a3f;\n"
                                        "border-right:1px solid #3a3a3f;\n"
                                        "border-left:1px solid #3a3a3f;")
        self.btnqrcodeurl.setObjectName("btnqrcodeurl")
        self.verticalLayout_9.addWidget(self.btnqrcodeurl)
        self.btnqrcode = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnqrcode.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                     "color: rgb(251, 0, 242);\n"
                                     "border-style:none;\n"
                                     "border-radius:6px;\n"
                                     "background:transparent;\n"
                                     "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                     "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                     "border-top:1px solid #3a3a3f;\n"
                                     "border-right:1px solid #3a3a3f;\n"
                                     "border-left:1px solid #3a3a3f;")
        self.btnqrcode.setObjectName("btnqrcode")
        self.verticalLayout_9.addWidget(self.btnqrcode)
        self.horizontalLayout_11.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pictureedit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.pictureedit.setMinimumSize(QtCore.QSize(158, 31))
        self.pictureedit.setMaximumSize(QtCore.QSize(480, 31))
        self.pictureedit.setStyleSheet("border-style:none;\n"
                                       "border-radius:6px;\n"
                                       "background:transparent;\n"
                                       "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                       "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                       "border-top:1px solid #3a3a3f;\n"
                                       "border-right:1px solid #3a3a3f;\n"
                                       "border-left:1px solid #3a3a3f;")
        self.pictureedit.setObjectName("pictureedit")
        self.verticalLayout_10.addWidget(self.pictureedit)
        self.qrcodenameEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.qrcodenameEdit.setStyleSheet("border-style:none;\n"
                                          "border-radius:6px;\n"
                                          "background:transparent;\n"
                                          "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                          "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                          "border-top:1px solid #3a3a3f;\n"
                                          "border-right:1px solid #3a3a3f;\n"
                                          "border-left:1px solid #3a3a3f;")
        self.qrcodenameEdit.setObjectName("qrcodenameEdit")
        self.verticalLayout_10.addWidget(self.qrcodenameEdit)
        self.urllineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.urllineEdit.setStyleSheet("border-style:none;\n"
                                       "border-radius:6px;\n"
                                       "background:transparent;\n"
                                       "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                       "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                       "border-top:1px solid #3a3a3f;\n"
                                       "border-right:1px solid #3a3a3f;\n"
                                       "border-left:1px solid #3a3a3f;")
        self.urllineEdit.setObjectName("urllineEdit")
        self.verticalLayout_10.addWidget(self.urllineEdit)
        self.qrcodeedit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.qrcodeedit.setMinimumSize(QtCore.QSize(158, 32))
        self.qrcodeedit.setMaximumSize(QtCore.QSize(480, 32))
        self.qrcodeedit.setStyleSheet("border-style:none;\n"
                                      "border-radius:6px;\n"
                                      "background:transparent;\n"
                                      "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                      "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                      "border-top:1px solid #3a3a3f;\n"
                                      "border-right:1px solid #3a3a3f;\n"
                                      "border-left:1px solid #3a3a3f;")
        self.qrcodeedit.setObjectName("qrcodeedit")
        self.verticalLayout_10.addWidget(self.qrcodeedit)
        self.horizontalLayout_11.addLayout(self.verticalLayout_10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.rbnheibai = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.rbnheibai.setMinimumSize(QtCore.QSize(60, 30))
        self.rbnheibai.setMaximumSize(QtCore.QSize(300, 30))
        self.rbnheibai.setStyleSheet("border-style:none;\n"
                                     "border-radius:6px;\n"
                                     "background:transparent;\n"
                                     "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                     "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                     "border-top:1px solid #3a3a3f;\n"
                                     "border-right:1px solid #3a3a3f;\n"
                                     "border-left:1px solid #3a3a3f;")
        self.rbnheibai.setObjectName("rbnheibai")
        self.verticalLayout_11.addWidget(self.rbnheibai)
        self.rbngif = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.rbngif.setMinimumSize(QtCore.QSize(60, 30))
        self.rbngif.setMaximumSize(QtCore.QSize(300, 30))
        self.rbngif.setStyleSheet("border-style:none;\n"
                                  "border-radius:6px;\n"
                                  "background:transparent;\n"
                                  "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                  "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                  "border-top:1px solid #3a3a3f;\n"
                                  "border-right:1px solid #3a3a3f;\n"
                                  "border-left:1px solid #3a3a3f;")
        self.rbngif.setObjectName("rbngif")
        self.verticalLayout_11.addWidget(self.rbngif)
        self.horizontalLayout_12.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.rbncaise = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.rbncaise.setMinimumSize(QtCore.QSize(60, 30))
        self.rbncaise.setMaximumSize(QtCore.QSize(308, 30))
        self.rbncaise.setStyleSheet("border-style:none;\n"
                                    "border-radius:6px;\n"
                                    "background:transparent;\n"
                                    "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                    "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                    "border-top:1px solid #3a3a3f;\n"
                                    "border-right:1px solid #3a3a3f;\n"
                                    "border-left:1px solid #3a3a3f;")
        self.rbncaise.setObjectName("rbncaise")
        self.verticalLayout_12.addWidget(self.rbncaise)
        self.rbnputong = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.rbnputong.setMinimumSize(QtCore.QSize(60, 30))
        self.rbnputong.setMaximumSize(QtCore.QSize(308, 30))
        self.rbnputong.setStyleSheet("border-style:none;\n"
                                     "border-radius:6px;\n"
                                     "background:transparent;\n"
                                     "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                     "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                     "border-top:1px solid #3a3a3f;\n"
                                     "border-right:1px solid #3a3a3f;\n"
                                     "border-left:1px solid #3a3a3f;")
        self.rbnputong.setObjectName("rbnputong")
        self.verticalLayout_12.addWidget(self.rbnputong)
        self.horizontalLayout_12.addLayout(self.verticalLayout_12)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.qrcodelist = QtWidgets.QListWidget(self.layoutWidget_2)
        self.qrcodelist.setMinimumSize(QtCore.QSize(158, 108))
        self.qrcodelist.setMaximumSize(QtCore.QSize(646, 108))
        self.qrcodelist.setStyleSheet("border-style:none;\n"
                                      "border-radius:6px;\n"
                                      "background:transparent;\n"
                                      "border-bottom: 1px solid #3a3a3f;min-width: 108px;margin-right: 8px;\n"
                                      "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                      "border-top:1px solid #3a3a3f;\n"
                                      "border-right:1px solid #3a3a3f;\n"
                                      "border-left:1px solid #3a3a3f;")
        self.qrcodelist.setObjectName("qrcodelist")
        self.verticalLayout_8.addWidget(self.qrcodelist)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.btnqrcodechangebackgroud = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnqrcodechangebackgroud.setMinimumSize(QtCore.QSize(60, 31))
        self.btnqrcodechangebackgroud.setMaximumSize(QtCore.QSize(104, 31))
        self.btnqrcodechangebackgroud.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                                    "color: rgb(251, 0, 242);\n"
                                                    "border-style:none;\n"
                                                    "border-radius:6px;\n"
                                                    "background:transparent;\n"
                                                    "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                                    "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                                    "border-top:1px solid #3a3a3f;\n"
                                                    "border-right:1px solid #3a3a3f;\n"
                                                    "border-left:1px solid #3a3a3f;")
        self.btnqrcodechangebackgroud.setObjectName("btnqrcodechangebackgroud")
        self.horizontalLayout_13.addWidget(self.btnqrcodechangebackgroud)
        self.btnzhizuo = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnzhizuo.setMinimumSize(QtCore.QSize(60, 31))
        self.btnzhizuo.setMaximumSize(QtCore.QSize(104, 31))
        self.btnzhizuo.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                     "color: rgb(251, 0, 242);\n"
                                     "border-style:none;\n"
                                     "border-radius:6px;\n"
                                     "background:transparent;\n"
                                     "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                     "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                     "border-top:1px solid #3a3a3f;\n"
                                     "border-right:1px solid #3a3a3f;\n"
                                     "border-left:1px solid #3a3a3f;")
        self.btnzhizuo.setObjectName("btnzhizuo")
        self.horizontalLayout_13.addWidget(self.btnzhizuo)
        self.btnqrcodeexit = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnqrcodeexit.setMinimumSize(QtCore.QSize(60, 31))
        self.btnqrcodeexit.setMaximumSize(QtCore.QSize(104, 31))
        self.btnqrcodeexit.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                         "color: rgb(251, 0, 242);\n"
                                         "border-style:none;\n"
                                         "border-radius:6px;\n"
                                         "background:transparent;\n"
                                         "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                         "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                         "border-top:1px solid #3a3a3f;\n"
                                         "border-right:1px solid #3a3a3f;\n"
                                         "border-left:1px solid #3a3a3f;")
        self.btnqrcodeexit.setObjectName("btnqrcodeexit")
        self.horizontalLayout_13.addWidget(self.btnqrcodeexit)
        self.btnqrcodeabout = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnqrcodeabout.setMinimumSize(QtCore.QSize(60, 31))
        self.btnqrcodeabout.setMaximumSize(QtCore.QSize(104, 31))
        self.btnqrcodeabout.setStyleSheet("font: 13pt \".SF NS Text\";\n"
                                          "color: rgb(251, 0, 242);\n"
                                          "border-style:none;\n"
                                          "border-radius:6px;\n"
                                          "background:transparent;\n"
                                          "border-bottom: 1px solid #3a3a3f;min-width: 10px;margin-right: 8px;\n"
                                          "padding-left:20px;padding-right:20px;padding-top:5px;padding-bottom:5px;color:#186a6e;\n"
                                          "border-top:1px solid #3a3a3f;\n"
                                          "border-right:1px solid #3a3a3f;\n"
                                          "border-left:1px solid #3a3a3f;")
        self.btnqrcodeabout.setObjectName("btnqrcodeabout")
        self.horizontalLayout_13.addWidget(self.btnqrcodeabout)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.tabWidget.addTab(self.tabqrcode, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.songlabel.setText(_translate("MainWindow",
                                          "<html><head/><body><p><span style=\" color:#f200f0;\">请输入下载的歌曲名：</span></p></body></html>"))
        self.songedit.setText(_translate("MainWindow", "如：电灯胆"))
        self.pathedit.setText(_translate("MainWindow", "点击[选择文件夹]选择歌曲保存路径："))
        self.btnsave.setText(_translate("MainWindow", "选择文件夹"))
        self.btnstart.setText(_translate("MainWindow", "开始下载"))
        self.btnexit.setText(_translate("MainWindow", "退出程序"))
        self.btnabout.setText(_translate("MainWindow", "关于作者"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wangyitab), _translate("MainWindow", "网易音乐"))
        self.shipinlabel.setText(_translate("MainWindow",
                                            "<html><head/><body><p align=\"right\"><span style=\" color:#e900ec;\">视频网址列表：</span></p></body></html>"))
        self.btnsaveshipin.setText(_translate("MainWindow", "选择文件夹"))
        self.shipinedit.setText(_translate("MainWindow", "空格隔开网址:"))
        self.patheditshipin.setText(_translate("MainWindow", "视频保存路径："))
        self.radioButtonlist.setText(_translate("MainWindow", "播放列表"))
        self.radioButton1080.setText(_translate("MainWindow", "超高清1080"))
        self.radioButton360.setText(_translate("MainWindow", "流畅360"))
        self.radioButton720.setText(_translate("MainWindow", "高清720"))
        self.ptnnchangebackgroud.setText(_translate("MainWindow", "更换皮肤"))
        self.btnstartshipin.setText(_translate("MainWindow", "开始下载"))
        self.btnexitshipin.setText(_translate("MainWindow", "退出程序"))
        self.btnaboutshipin.setText(_translate("MainWindow", "关于作者"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabshipin), _translate("MainWindow", "视频下载"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" color:#cb002c;\">播放链接：</span></p></body></html>"))
        self.editurl.setText(_translate("MainWindow", "电脑使用CTRL+V粘贴网址-手机长按粘贴网址"))
        self.rbtn4.setText(_translate("MainWindow", "播放接口1"))
        self.rbtn5.setText(_translate("MainWindow", "播放接口2"))
        self.rbtn1.setText(_translate("MainWindow", "播放接口3"))
        self.rbtn2.setText(_translate("MainWindow", "播放接口4"))
        self.rbtn3.setText(_translate("MainWindow", "播放接口5"))
        self.btnbofang.setText(_translate("MainWindow", "播放"))
        self.btnqingchu.setText(_translate("MainWindow", "清除"))
        self.btnabout_2.setText(_translate("MainWindow", "关于作者"))
        self.btnexit_2.setText(_translate("MainWindow", "退出程序"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\"><thead>\n"
                                            "<tr>\n"
                                            "<td>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#d82a0e;\">       </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#d82a0e;\">全网影视VIP及付费视频解析说明</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600; color:#d82a0e;\"><br /></p></td></tr></thead>\n"
                                            "<tr>\n"
                                            "<td>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#570079;\">                                    第一步  进入各大视频网站，找到想要观看的VIP视频或者电视剧！</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#570079;\">                                    第二步  复制浏览器上的视频地址、粘贴到播放链接后的文本框！</span></p>\n"
                                            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#570079;\">                                    第三步 然后选择播放接口，再点击播放即可！ </span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-size:14pt; color:#570079;\"><br /></p></td></tr></table></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabquanwang), _translate("MainWindow", "全网解析"))
        self.btnpicture.setText(_translate("MainWindow", "选择(制作用)图片:"))
        self.btnpicleixing.setText(_translate("MainWindow", "二维码类型及命名："))
        self.btnqrcodeurl.setText(_translate("MainWindow", "二维码指定url:"))
        self.btnqrcode.setText(_translate("MainWindow", "(二维码)保存位置:"))
        self.pictureedit.setText(_translate("MainWindow", "制作二维码的图片路径:"))
        self.qrcodenameEdit.setText(_translate("MainWindow", "命名为*.png,如果图片为gif格式，则命名为*.gif"))
        self.urllineEdit.setText(_translate("MainWindow", "扫描二维码后的链接位置："))
        self.qrcodeedit.setText(_translate("MainWindow", "生成的二维码保存路径："))
        self.rbnheibai.setText(_translate("MainWindow", "黑白二维码"))
        self.rbngif.setText(_translate("MainWindow", "动态GIF二维码"))
        self.rbncaise.setText(_translate("MainWindow", "彩色二维码"))
        self.rbnputong.setText(_translate("MainWindow", "普通二维码"))
        self.btnqrcodechangebackgroud.setText(_translate("MainWindow", "更换皮肤"))
        self.btnzhizuo.setText(_translate("MainWindow", "开始制作"))
        self.btnqrcodeexit.setText(_translate("MainWindow", "退出程序"))
        self.btnqrcodeabout.setText(_translate("MainWindow", "关于作者"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabqrcode), _translate("MainWindow", "二维码制作"))
