# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score_board_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScoreBoard(object):
    def setupUi(self, ScoreBoard):
        ScoreBoard.setObjectName("ScoreBoard")
        ScoreBoard.resize(806, 258)
        self.verticalLayout = QtWidgets.QVBoxLayout(ScoreBoard)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_score = QtWidgets.QTableWidget(ScoreBoard)
        self.table_score.setObjectName("table_score")
        self.table_score.setColumnCount(0)
        self.table_score.setRowCount(0)
        self.verticalLayout.addWidget(self.table_score)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_continue = QtWidgets.QPushButton(ScoreBoard)
        self.btn_continue.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_continue.setStyleSheet("font-size: 20px")
        self.btn_continue.setObjectName("btn_continue")
        self.horizontalLayout.addWidget(self.btn_continue)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(ScoreBoard)
        QtCore.QMetaObject.connectSlotsByName(ScoreBoard)

    def retranslateUi(self, ScoreBoard):
        _translate = QtCore.QCoreApplication.translate
        ScoreBoard.setWindowTitle(_translate("ScoreBoard", "Scores"))
        self.btn_continue.setText(_translate("ScoreBoard", "Back"))
