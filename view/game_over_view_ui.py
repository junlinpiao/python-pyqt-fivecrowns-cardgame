# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_over_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameOver(object):
    def setupUi(self, GameOver):
        GameOver.setObjectName("GameOver")
        GameOver.resize(391, 301)
        self.verticalLayout = QtWidgets.QVBoxLayout(GameOver)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_heading = QtWidgets.QLabel(GameOver)
        self.lbl_heading.setStyleSheet("font-size: 25px")
        self.lbl_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_heading.setWordWrap(True)
        self.lbl_heading.setObjectName("lbl_heading")
        self.verticalLayout.addWidget(self.lbl_heading)
        self.lbl_score = QtWidgets.QLabel(GameOver)
        self.lbl_score.setStyleSheet("font-size:50px;\n"
"color: red;")
        self.lbl_score.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_score.setObjectName("lbl_score")
        self.verticalLayout.addWidget(self.lbl_score)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_scores = QtWidgets.QPushButton(GameOver)
        self.btn_scores.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_scores.setStyleSheet("font-size:15px")
        self.btn_scores.setObjectName("btn_scores")
        self.horizontalLayout.addWidget(self.btn_scores)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_quit = QtWidgets.QPushButton(GameOver)
        self.btn_quit.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_quit.setStyleSheet("font-size:15px")
        self.btn_quit.setObjectName("btn_quit")
        self.horizontalLayout.addWidget(self.btn_quit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(3, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(GameOver)
        QtCore.QMetaObject.connectSlotsByName(GameOver)

    def retranslateUi(self, GameOver):
        _translate = QtCore.QCoreApplication.translate
        GameOver.setWindowTitle(_translate("GameOver", "Form"))
        self.lbl_heading.setText(_translate("GameOver", "<span style=\"color: red\">\"Player 2\"</span>  Won the Game!"))
        self.lbl_score.setText(_translate("GameOver", "Score: 25"))
        self.btn_scores.setText(_translate("GameOver", "View Scores"))
        self.btn_quit.setText(_translate("GameOver", "Quit"))
