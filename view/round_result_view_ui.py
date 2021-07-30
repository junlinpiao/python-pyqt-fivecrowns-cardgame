# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'round_result_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RoundResult(object):
    def setupUi(self, RoundResult):
        RoundResult.setObjectName("RoundResult")
        RoundResult.resize(600, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(RoundResult)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_heading = QtWidgets.QLabel(RoundResult)
        self.lbl_heading.setStyleSheet("font-size: 25px")
        self.lbl_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_heading.setObjectName("lbl_heading")
        self.verticalLayout.addWidget(self.lbl_heading)
        self.label = QtWidgets.QLabel(RoundResult)
        self.label.setStyleSheet("font-size: 15px")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(RoundResult)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 445, 247))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_continue = QtWidgets.QPushButton(RoundResult)
        self.btn_continue.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_continue.setStyleSheet("font-size: 15px")
        self.btn_continue.setObjectName("btn_continue")
        self.horizontalLayout.addWidget(self.btn_continue)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(RoundResult)
        QtCore.QMetaObject.connectSlotsByName(RoundResult)

    def retranslateUi(self, RoundResult):
        _translate = QtCore.QCoreApplication.translate
        RoundResult.setWindowTitle(_translate("RoundResult", "Form"))
        self.lbl_heading.setText(_translate("RoundResult", "Round 1 Ended"))
        self.label.setText(_translate("RoundResult", "Remaining Cards"))
        self.btn_continue.setText(_translate("RoundResult", "Got it"))
