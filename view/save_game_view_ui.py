# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_game_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SaveGame(object):
    def setupUi(self, SaveGame):
        SaveGame.setObjectName("SaveGame")
        SaveGame.resize(449, 150)
        self.verticalLayout = QtWidgets.QVBoxLayout(SaveGame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(SaveGame)
        self.label.setStyleSheet("font-size:15px")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_save_name = QtWidgets.QLineEdit(SaveGame)
        self.line_save_name.setMinimumSize(QtCore.QSize(0, 40))
        self.line_save_name.setStyleSheet("font-size: 15px")
        self.line_save_name.setObjectName("line_save_name")
        self.verticalLayout.addWidget(self.line_save_name)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_save = QtWidgets.QPushButton(SaveGame)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_save.setStyleSheet("font-size: 15px")
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_cancel = QtWidgets.QPushButton(SaveGame)
        self.btn_cancel.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_cancel.setStyleSheet("font-size: 15px")
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SaveGame)
        QtCore.QMetaObject.connectSlotsByName(SaveGame)

    def retranslateUi(self, SaveGame):
        _translate = QtCore.QCoreApplication.translate
        SaveGame.setWindowTitle(_translate("SaveGame", "Form"))
        self.label.setText(_translate("SaveGame", "Enter save file name:"))
        self.btn_save.setText(_translate("SaveGame", "Save"))
        self.btn_cancel.setText(_translate("SaveGame", "Cancel"))
