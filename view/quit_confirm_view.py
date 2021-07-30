from PyQt5 import QtCore, QtWidgets
from view.quit_confirm_view_ui import Ui_QuitConfirm

class QuitConfirmWidget(QtWidgets.QWidget):
    
    signal_switch_save_game = QtCore.pyqtSignal()
    signal_quit_game = QtCore.pyqtSignal()
    signal_switch_game_board = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self._ui = Ui_QuitConfirm()
        self._ui.setupUi(self)

        self.setWindowTitle('Confirmation')

        self._ui.btn_save.clicked.connect(self.onSave)
        self._ui.btn_not_save.clicked.connect(self.onNotSave)
        self._ui.btn_cancel.clicked.connect(self.onCancel)

    # switch to save window
    def onSave(self):
        self.signal_switch_save_game.emit()

    # switch to game board window
    def onCancel(self):
        self.signal_switch_game_board.emit()

    def onNotSave(self):
        self.signal_quit_game.emit()