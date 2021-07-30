from PyQt5 import QtCore, QtWidgets, QtGui
from base_class.hand import Hand
# customized button that has index
class IndexedButton(QtWidgets.QPushButton):

    signal_clicked = QtCore.pyqtSignal(Hand)

    def __init__(self, parent_wgt, drop_hand):
        QtWidgets.QPushButton.__init__(self, parent_wgt)
        self.drop_hand = drop_hand

    def mousePressEvent(self, event):
        # super().mousePressEvent(event)
        self.signal_clicked.emit(self.drop_hand)
