from PyQt5 import QtCore, QtWidgets
from view.setting_view_ui import Ui_Setting

class SettingWidget(QtWidgets.QWidget):
    
    signal_switch_coin_toss = QtCore.pyqtSignal()
    signal_switch_menu = QtCore.pyqtSignal()

    def __init__(self, model):
        QtWidgets.QWidget.__init__(self)
        self._ui = Ui_Setting()
        self._ui.setupUi(self)
        self._model = model

        self.load_default_values()
        self.set_spin_defaults()

        self.setWindowTitle('Settings')

        self._ui.btn_start.clicked.connect(self.switch_coin_toss_widget)
        self._ui.btn_back.clicked.connect(self.switch_menu_widget)

    def load_default_values(self):
        player_count = self._model.get_data('player_count')
        computer_count = player_count["computer"]
        human_count = player_count["human"]
        deck_count = self._model.get_data('deck_count')
        self._ui.spin_deck_count.setValue(deck_count)
        self._ui.spin_computer_count.setValue(computer_count)
        self._ui.spin_human_count.setValue(human_count)
        self._ui.spin_player_count.setValue(computer_count+human_count)

    # initial values for ui elements.
    def set_spin_defaults(self):
        # set min and max values of spinBox
        self._ui.spin_player_count.setMinimum(2)    # minimum 2 players
        self._ui.spin_player_count.setMaximum(4)    # maximum 4 players
        self._ui.spin_deck_count.setMinimum(2)    # minimum 2 decks
        self._ui.spin_deck_count.setMaximum(4)    # maximum 4 decks
        self._ui.spin_computer_count.setMinimum(0)    # minimum 1 computers
        self._ui.spin_computer_count.setMaximum(4)    # maximum 4 computers
        self._ui.spin_human_count.setMinimum(0)    # minimum 1 human
        self._ui.spin_human_count.setMaximum(4)    # maximum 4 human

        # connect when spins changed
        self._ui.spin_player_count.valueChanged.connect(self.onTotalCountChanged)
        self._ui.spin_computer_count.valueChanged.connect(self.onComputerCountChanged)
        self._ui.spin_human_count.valueChanged.connect(self.onHumanCountChanged)

    def getComputerCount(self):
        return self._ui.spin_computer_count.value()

    def getHumanCount(self):
        return self._ui.spin_human_count.value()
    
    def getPlayerCount(self):
        return self._ui.spin_player_count.value()
    
    def getDeckCount(self):
        return self._ui.spin_deck_count.value()
    
    # slot when total player count changed
    def onTotalCountChanged(self):
        total_count = self.getPlayerCount()
        computer_count = self.getComputerCount()
        human_count = total_count - computer_count
        if human_count < 0:
            self._ui.spin_computer_count.setValue(total_count)
        self._ui.spin_human_count.setValue(human_count)

    # slot when computer player count changed
    def onComputerCountChanged(self):
        total_count = self.getPlayerCount()
        computer_count = self.getComputerCount()
        human_count = total_count - computer_count
        if human_count < 0:
            self._ui.spin_computer_count.setValue(total_count)
        self._ui.spin_human_count.setValue(human_count)

    # slot when human player count changed
    def onHumanCountChanged(self):
        total_count = self.getPlayerCount()
        human_count = self.getHumanCount()
        computer_count = total_count - human_count
        if computer_count < 0:
            self._ui.spin_human_count.setValue(total_count)
        self._ui.spin_computer_count.setValue(computer_count)

    def update_model(self):
        self._model.update_data('play_state', 0) # 0: new game
        self._model.update_data('deck_count', self.getDeckCount())
        self._model.update_data('player_count', {"computer": self.getComputerCount(), "human": self.getHumanCount()})

    # switch to settings window
    def switch_menu_widget(self):
        self.update_model()
        self.signal_switch_menu.emit()

    # switch to open-saved-games window
    def switch_coin_toss_widget(self):
        self.update_model()
        self._model.create_players()
        self.signal_switch_coin_toss.emit()