from PyQt5 import QtCore, QtWidgets
from view.save_game_view_ui import Ui_SaveGame
from datetime import datetime as DateTime

class SaveGameWidget(QtWidgets.QWidget):
    
    signal_switch_game_board = QtCore.pyqtSignal()
    signal_quit_game = QtCore.pyqtSignal()

    def __init__(self, model, save_and_exit=False):
        QtWidgets.QWidget.__init__(self)
        self._ui = Ui_SaveGame()
        self._ui.setupUi(self)
        self._model = model
        self._exit = save_and_exit
        self.setWindowTitle('Save game...')

        self._ui.btn_save.clicked.connect(self.onSave)
        self._ui.btn_cancel.clicked.connect(self.onCancel)

        self._ui.line_save_name.setText(self.get_cur_time_str()+".txt")
        self._ui.line_save_name.selectAll()

    def get_cur_time_str(self):
        today = DateTime.now()
        return today.strftime("%Y_%m_%d_%H_%M_%S")

    def onSave(self):
        save_name = self._ui.line_save_name.text()
        if not save_name.endswith(".txt"):
            save_name = save_name + ".txt"
        bResult = self._model.save_game(save_name)
        if bResult == "duplicate":
            QtWidgets.QMessageBox.warning(self, "Notice", "This file name already exists. <br>Try another.")
            return
        elif bResult == "error":
            QtWidgets.QMessageBox.warning(self, "Error", "Could not save game. <br>Try again later.")
        elif bResult == "success":
            QtWidgets.QMessageBox.warning(self, "Success", "Game saved successfully!")
        if self._exit:
            self.quit_game()
        else:
            self.switch_game_board_widget()

    def onCancel(self):
        self.switch_game_board_widget()

    # switch to open-saved-games window
    def switch_game_board_widget(self):
        self.signal_switch_game_board.emit()

    def quit_game(self):
        self.signal_quit_game.emit()