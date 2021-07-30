# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quit_confirm_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuitConfirm(object):
    def setupUi(self, QuitConfirm):
        QuitConfirm.setObjectName("QuitConfirm")
        QuitConfirm.resize(388, 150)
        self.verticalLayout = QtWidgets.QVBoxLayout(QuitConfirm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(QuitConfirm)
        self.label.setStyleSheet("font-size: 18px")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_save = QtWidgets.QPushButton(QuitConfirm)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_save.setStyleSheet("font-size: 15px\n"
"")
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_not_save = QtWidgets.QPushButton(QuitConfirm)
        self.btn_not_save.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_not_save.setStyleSheet("font-size:15px\n"
"")
        self.btn_not_save.setObjectName("btn_not_save")
        self.horizontalLayout.addWidget(self.btn_not_save)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_cancel = QtWidgets.QPushButton(QuitConfirm)
        self.btn_cancel.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_cancel.setStyleSheet("font-size: 15px")
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 5)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 5)
        self.horizontalLayout.setStretch(6, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(QuitConfirm)
        QtCore.QMetaObject.connectSlotsByName(QuitConfirm)

    def retranslateUi(self, QuitConfirm):
        _translate = QtCore.QCoreApplication.translate
        QuitConfirm.setWindowTitle(_translate("QuitConfirm", "Form"))
        self.label.setText(_translate("QuitConfirm", "Do you want to save game before quit?"))
        self.btn_save.setText(_translate("QuitConfirm", "Save"))
        self.btn_not_save.setText(_translate("QuitConfirm", "Don\'t save"))
        self.btn_cancel.setText(_translate("QuitConfirm", "Cancel"))
