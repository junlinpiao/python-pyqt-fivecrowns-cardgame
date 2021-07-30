from PyQt5 import QtCore, QtWidgets
from view.game_over_view_ui import Ui_GameOver

class GameOverWidget(QtWidgets.QWidget):
    
    signal_switch_scores = QtCore.pyqtSignal()
    signal_quit_game = QtCore.pyqtSignal()

    def __init__(self, model):
        QtWidgets.QWidget.__init__(self)
        self._ui = Ui_GameOver()
        self._ui.setupUi(self)
        self._model = model
        self.setWindowTitle('Game Over!')

        self._ui.btn_scores.clicked.connect(self.switch_scores_widget)
        self._ui.btn_quit.clicked.connect(self.quit_game)

        self.setup_gui()

    def setup_gui(self):
        winners_data = self._model.get_winner_data()
        display_name_text = ""
        display_score_text = ""
        for winner_data in winners_data:
            display_name_text += '<span style="color: red">"'+winner_data['name']+'"</span>, '
            display_score_text = "Score: {}".format(winner_data['total_score'])
        display_name_text = display_name_text[:-2] + " Won the Game!"
        self._ui.lbl_heading.setText(display_name_text)
        self._ui.lbl_score.setText(display_score_text)

    # switch to Scores View window
    def switch_scores_widget(self):
        self.signal_switch_scores.emit()

    # switch to Main Menu window
    def quit_game(self):
        self.signal_quit_game.emit()