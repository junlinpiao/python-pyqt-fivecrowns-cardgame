from PyQt5 import QtCore, QtWidgets
from view.menu_view_ui import Ui_Menu

class MenuWidget(QtWidgets.QWidget):
    
    signal_switch_setting = QtCore.pyqtSignal()
    signal_switch_saved_games = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self._ui = Ui_Menu()
        self._ui.setupUi(self)

        self.setWindowTitle('Main Menu')

        self._ui.btn_load_saved.clicked.connect(self.switch_saved_widget)
        self._ui.btn_new_game.clicked.connect(self.switch_setting_widget)
        self._ui.btn_quit.clicked.connect(self.close)

    # switch to settings window
    def switch_setting_widget(self):
        self.signal_switch_setting.emit()

    # switch to open-saved-games window
    def switch_saved_widget(self):
        self.signal_switch_saved_games.emit()