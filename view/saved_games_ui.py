# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saved_games.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SavedGames(object):
    def setupUi(self, SavedGames):
        SavedGames.setObjectName("SavedGames")
        SavedGames.resize(429, 335)
        self.verticalLayout = QtWidgets.QVBoxLayout(SavedGames)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_saved_games = QtWidgets.QListWidget(SavedGames)
        self.list_saved_games.setObjectName("list_saved_games")
        self.verticalLayout.addWidget(self.list_saved_games)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_resume = QtWidgets.QPushButton(SavedGames)
        self.btn_resume.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_resume.setStyleSheet("font-size: 20px")
        self.btn_resume.setObjectName("btn_resume")
        self.horizontalLayout_3.addWidget(self.btn_resume)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btn_back = QtWidgets.QPushButton(SavedGames)
        self.btn_back.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_3.addWidget(self.btn_back)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(3, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(SavedGames)
        QtCore.QMetaObject.connectSlotsByName(SavedGames)

    def retranslateUi(self, SavedGames):
        _translate = QtCore.QCoreApplication.translate
        SavedGames.setWindowTitle(_translate("SavedGames", "Form"))
        self.btn_resume.setText(_translate("SavedGames", "Resume Game"))
        self.btn_back.setText(_translate("SavedGames", "Back to Main Menu"))
