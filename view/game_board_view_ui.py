# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_board_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameBoard(object):
    def setupUi(self, GameBoard):
        GameBoard.setObjectName("GameBoard")
        GameBoard.resize(670, 521)
        GameBoard.setStyleSheet("GameBoard.QWidget {border: 1px solid black;}")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(GameBoard)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_round = QtWidgets.QLabel(GameBoard)
        self.lbl_round.setStyleSheet("font-size: 30px")
        self.lbl_round.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_round.setObjectName("lbl_round")
        self.horizontalLayout.addWidget(self.lbl_round)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_save = QtWidgets.QPushButton(GameBoard)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_save.setStyleSheet("font-size:15px")
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_view_scores = QtWidgets.QPushButton(GameBoard)
        self.btn_view_scores.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_view_scores.setStyleSheet("font-size:15px")
        self.btn_view_scores.setObjectName("btn_view_scores")
        self.horizontalLayout.addWidget(self.btn_view_scores)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(0, 30)
        self.horizontalLayout.setStretch(1, 40)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 14)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 13)
        self.horizontalLayout.setStretch(6, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(GameBoard)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 449, 233))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_cur_turn = QtWidgets.QLabel(GameBoard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_cur_turn.sizePolicy().hasHeightForWidth())
        self.lbl_cur_turn.setSizePolicy(sizePolicy)
        self.lbl_cur_turn.setStyleSheet("font-size: 15px")
        self.lbl_cur_turn.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_cur_turn.setWordWrap(True)
        self.lbl_cur_turn.setObjectName("lbl_cur_turn")
        self.verticalLayout_3.addWidget(self.lbl_cur_turn)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wgt_draw_pile = QtWidgets.QWidget(GameBoard)
        self.wgt_draw_pile.setObjectName("wgt_draw_pile")
        self.verticalLayout_2.addWidget(self.wgt_draw_pile)
        self.lbl_draw_pile = QtWidgets.QLabel(GameBoard)
        self.lbl_draw_pile.setStyleSheet("font-size:15px\n"
"")
        self.lbl_draw_pile.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_draw_pile.setObjectName("lbl_draw_pile")
        self.verticalLayout_2.addWidget(self.lbl_draw_pile)
        self.verticalLayout_2.setStretch(0, 1)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.wgt_discard_pile = QtWidgets.QWidget(GameBoard)
        self.wgt_discard_pile.setObjectName("wgt_discard_pile")
        self.verticalLayout.addWidget(self.wgt_discard_pile)
        self.lbl_discard_pile = QtWidgets.QLabel(GameBoard)
        self.lbl_discard_pile.setStyleSheet("font-size:15px")
        self.lbl_discard_pile.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_discard_pile.setObjectName("lbl_discard_pile")
        self.verticalLayout.addWidget(self.lbl_discard_pile)
        self.verticalLayout.setStretch(0, 1)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.setStretch(0, 7)
        self.horizontalLayout_4.setStretch(1, 3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.wgt_hand = QtWidgets.QWidget(GameBoard)
        self.wgt_hand.setObjectName("wgt_hand")
        self.horizontalLayout_2.addWidget(self.wgt_hand)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 50)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.lbl_wild_card = QtWidgets.QLabel(GameBoard)
        self.lbl_wild_card.setStyleSheet("font-size: 15px")
        self.lbl_wild_card.setObjectName("lbl_wild_card")
        self.horizontalLayout_3.addWidget(self.lbl_wild_card)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.btn_drop = QtWidgets.QPushButton(GameBoard)
        self.btn_drop.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_drop.setStyleSheet("font-size: 20px;")
        self.btn_drop.setObjectName("btn_drop")
        self.horizontalLayout_3.addWidget(self.btn_drop)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.btn_discard = QtWidgets.QPushButton(GameBoard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_discard.sizePolicy().hasHeightForWidth())
        self.btn_discard.setSizePolicy(sizePolicy)
        self.btn_discard.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_discard.setStyleSheet("font-size: 20px;")
        self.btn_discard.setObjectName("btn_discard")
        self.horizontalLayout_3.addWidget(self.btn_discard)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.btn_quit = QtWidgets.QPushButton(GameBoard)
        self.btn_quit.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_quit.setStyleSheet("font-size: 15px")
        self.btn_quit.setObjectName("btn_quit")
        self.horizontalLayout_3.addWidget(self.btn_quit)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.horizontalLayout_3.setStretch(0, 20)
        self.horizontalLayout_3.setStretch(2, 10)
        self.horizontalLayout_3.setStretch(3, 40)
        self.horizontalLayout_3.setStretch(4, 10)
        self.horizontalLayout_3.setStretch(5, 40)
        self.horizontalLayout_3.setStretch(6, 19)
        self.horizontalLayout_3.setStretch(7, 10)
        self.horizontalLayout_3.setStretch(8, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.setStretch(1, 3)
        self.verticalLayout_5.setStretch(2, 2)

        self.retranslateUi(GameBoard)
        QtCore.QMetaObject.connectSlotsByName(GameBoard)

    def retranslateUi(self, GameBoard):
        _translate = QtCore.QCoreApplication.translate
        GameBoard.setWindowTitle(_translate("GameBoard", "Form"))
        self.lbl_round.setText(_translate("GameBoard", "Round 1"))
        self.btn_save.setText(_translate("GameBoard", "Save game"))
        self.btn_view_scores.setText(_translate("GameBoard", "View Scores"))
        self.lbl_cur_turn.setText(_translate("GameBoard", "Computer 2 \'s turn"))
        self.lbl_draw_pile.setText(_translate("GameBoard", "Draw pile"))
        self.lbl_discard_pile.setText(_translate("GameBoard", "Discard pile"))
        self.lbl_wild_card.setText(_translate("GameBoard", "<span style=\"font-size: 30px; color: red; font-weight: bold\">[3]</span> is wild card"))
        self.btn_drop.setText(_translate("GameBoard", "Drop"))
        self.btn_discard.setText(_translate("GameBoard", "Discard"))
        self.btn_quit.setText(_translate("GameBoard", "Quit"))
