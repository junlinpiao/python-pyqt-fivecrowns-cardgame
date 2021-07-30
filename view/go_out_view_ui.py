# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'go_out_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GoOut(object):
    def setupUi(self, GoOut):
        GoOut.setObjectName("GoOut")
        GoOut.resize(500, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(GoOut)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_heading = QtWidgets.QLabel(GoOut)
        self.lbl_heading.setStyleSheet("font-size: 20px\n"
"")
        self.lbl_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_heading.setObjectName("lbl_heading")
        self.verticalLayout.addWidget(self.lbl_heading)
        self.scrollArea = QtWidgets.QScrollArea(GoOut)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 480, 378))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_ok = QtWidgets.QPushButton(GoOut)
        self.btn_ok.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_ok.setStyleSheet("font-size: 20px")
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(GoOut)
        QtCore.QMetaObject.connectSlotsByName(GoOut)

    def retranslateUi(self, GoOut):
        _translate = QtCore.QCoreApplication.translate
        GoOut.setWindowTitle(_translate("GoOut", "Form"))
        self.lbl_heading.setText(_translate("GoOut", "<span style=\"color: red\">\"Human\"</span> goes out!<br>Other players have only 1 chance."))
        self.btn_ok.setText(_translate("GoOut", "Got it"))
