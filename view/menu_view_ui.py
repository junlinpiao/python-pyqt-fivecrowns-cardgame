# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(311, 328)
        self.verticalLayout = QtWidgets.QVBoxLayout(Menu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_load_saved = QtWidgets.QPushButton(Menu)
        self.btn_load_saved.setMinimumSize(QtCore.QSize(0, 70))
        self.btn_load_saved.setStyleSheet("font-size:20px")
        self.btn_load_saved.setObjectName("btn_load_saved")
        self.horizontalLayout.addWidget(self.btn_load_saved)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_new_game = QtWidgets.QPushButton(Menu)
        self.btn_new_game.setMinimumSize(QtCore.QSize(0, 70))
        self.btn_new_game.setStyleSheet("font-size: 20px\n"
"")
        self.btn_new_game.setObjectName("btn_new_game")
        self.horizontalLayout_2.addWidget(self.btn_new_game)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.btn_quit = QtWidgets.QPushButton(Menu)
        self.btn_quit.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_quit.setStyleSheet("font-size: 20px")
        self.btn_quit.setObjectName("btn_quit")
        self.horizontalLayout_3.addWidget(self.btn_quit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 6)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Form"))
        self.btn_load_saved.setText(_translate("Menu", "Load Saved Game"))
        self.btn_new_game.setText(_translate("Menu", "New Game"))
        self.btn_quit.setText(_translate("Menu", "Quit"))
