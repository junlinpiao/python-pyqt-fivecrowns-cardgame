from PyQt5 import QtCore, QtWidgets
from view.hand_view import HandWidget
from view.round_result_view_ui import Ui_RoundResult

class RoundResultWidget(QtWidgets.QWidget):
    
    signal_continue = QtCore.pyqtSignal()

    def __init__(self, model):
        QtWidgets.QWidget.__init__(self)
        self._ui = Ui_RoundResult()
        self._ui.setupUi(self)
        self._model = model

        self._ui.btn_continue.clicked.connect(self.onContinue)
        self.setup_gui()

    def setup_gui(self):
        cur_round = self._model.get_data('cur_round')
        self.setWindowTitle('Result of Round {}'.format(cur_round))
        self._ui.lbl_heading.setText("Round {} Ended".format(cur_round))

        players = self._model.get_data('players')
        self.hand_wgts = []
        self.lbl_player_info_wgts = []
        scroll_wgt = self._ui.scrollAreaWidgetContents
        self.scroll_vLayout = QtWidgets.QVBoxLayout(scroll_wgt)
        first_gone_out_player = self._model.get_data('first_gone_out')
        for player in players:
            hand = player.get_hand()
            hand.arrange_order()
            player_info_label = QtWidgets.QLabel(scroll_wgt)
            player_scores = player.get_player_score()
            player_score = player_scores[str(cur_round)]
            player_info_str = '<br>"{}": {}'.format(player.get_player_name(), player_score)
            if player is first_gone_out_player:
                player_info_str += " ( First Gone Out )"
            player_info_label.setText(player_info_str)
            player_info_label.setStyleSheet("font-size: 15px")
            player_info_label.setAlignment(QtCore.Qt.AlignCenter)
            self.scroll_vLayout.addWidget(player_info_label)
            self.lbl_player_info_wgts.append(player_info_label)
            if player_score > 0:
                player_hand_wgt = HandWidget(hand, scroll_wgt.width() - 20, 160, scroll_wgt, True)
                player_hand_wgt.show()
                self.hand_wgts.append(player_hand_wgt)
                self.scroll_vLayout.addWidget(player_hand_wgt)
            
            
        

    def onContinue(self):
        self.signal_continue.emit()
