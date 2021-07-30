from PyQt5 import QtCore, QtWidgets
from view.coin_toss_view_ui import Ui_CoinToss
from time import sleep
import random

class CoinTossWidget(QtWidgets.QWidget):
    
    signal_switch_game_board = QtCore.pyqtSignal()
    signal_switch_menu = QtCore.pyqtSignal()

    def __init__(self, model):
        QtWidgets.QWidget.__init__(self)
        self._ui = Ui_CoinToss()
        self._ui.setupUi(self)
        self._model = model

        self.setWindowTitle('Coin Toss')

        self._ui.btn_back.clicked.connect(self.switch_menu_widget)
        self._ui.btn_start.clicked.connect(self.switch_game_board_widget)
        self._ui.btn_coin_toss.clicked.connect(self.coin_toss)
        self._ui.btn_start.setEnabled(False)

    def update_model(self):
        pass

    # switch to Menu window
    def switch_menu_widget(self):
        self.signal_switch_menu.emit()

    # switch to open-saved-games window
    def switch_game_board_widget(self):
        self.update_model()
        self.signal_switch_game_board.emit()

    # coin toss
    def coin_toss(self):
        sleep(0.5)
        players = self._model.get_data('players')
        first_player = random.choice(players)
        first_player_id = first_player.get_player_id()
        first_player_type = first_player.get_player_type()
        first_player_name = first_player.get_player_name()
        self._model.update_data('cur_turn', first_player)
        display_text = ""
        if first_player_type == 'human':
            display_text += "Congratulations! \n"
        display_text += "{} start first.".format(first_player_name)
        self._ui.lbl_toss_result.setText(display_text)
        self._ui.btn_coin_toss.setEnabled(False)
        self._ui.btn_start.setEnabled(True)
        