from PyQt5 import QtCore, QtWidgets, QtGui
from view.card_view import CardWidget

class PileWidget(CardWidget):

    signal_pile_clicked = QtCore.pyqtSignal(QtWidgets.QWidget)

    def __init__(self, model, card, width, height, parent=None, show_backface=False, no_actions=False):
        super().__init__(card, width, height, parent, show_backface)
        self._model = model
        self._is_available = not no_actions
        self.setFixedSize(width, height)

    def mousePressEvent(self, event):
        if self._is_available:
            self.signal_pile_clicked.emit(self)

    def enterEvent(self, event):
        if self._is_available:
            super().enterEvent(event)
        
    def leaveEvent(self, event):
        if self._is_available:
            super().leaveEvent(event)

    def causeEnterEvent(self):
        self._back_color = QtGui.QColor(180,180,180)
        self.update()

    def causeLeaveEvent(self):
        self._back_color = QtGui.QColor(255,255,255)
        self.update()

    def causeMousePressEvent(self):
        self.signal_pile_clicked.emit(self)

