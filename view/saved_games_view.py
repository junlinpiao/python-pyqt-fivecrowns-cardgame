from PyQt5 import QtCore, QtWidgets
from view.saved_games_ui import Ui_SavedGames

class SavedGamesWidget(QtWidgets.QWidget):
    
    signal_switch_game_board = QtCore.pyqtSignal()
    signal_switch_menu = QtCore.pyqtSignal()

    def __init__(self, model):
        QtWidgets.QWidget.__init__(self)
        self._ui = Ui_SavedGames()
        self._ui.setupUi(self)
        self._model = model

        self.load_default_values()

        self.setWindowTitle('Load saved games...')

        self._ui.btn_resume.clicked.connect(self.switch_game_board_widget)
        self._ui.btn_back.clicked.connect(self.switch_menu_widget)

    def load_default_values(self):
        saved_filenames = self._model.saved_game_file_names()
        self._ui.list_saved_games.addItems(saved_filenames)
        self._ui.list_saved_games.setCurrentRow(0)
        if len(saved_filenames) == 0:
            self._ui.btn_resume.setEnabled(False)

    def update_model(self, filename):
        return self._model.load_saved_game_data(filename)

    # get currently selected filename
    def get_cur_sel_filename(self):
        return self._ui.list_saved_games.currentItem().text()

    # switch to Menu window
    def switch_menu_widget(self):
        self.signal_switch_menu.emit()

    # switch to open-saved-games window
    def switch_game_board_widget(self):
        cur_sel_filename = self.get_cur_sel_filename()
        bResult = self.update_model(cur_sel_filename)

        if bResult == "error":
            QtWidgets.QMessageBox.warning(self, "Error", "Could not load game. <br>This file might be invalid.<br>Try again.")
            return

        self.signal_switch_game_board.emit()