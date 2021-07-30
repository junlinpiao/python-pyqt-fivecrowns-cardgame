from PyQt5 import QtCore, QtWidgets
from view.score_board_view_ui import Ui_ScoreBoard

class ScoreBoardWidget(QtWidgets.QWidget):
    
    signal_continue = QtCore.pyqtSignal()

    def __init__(self, model):
        QtWidgets.QWidget.__init__(self)
        self._ui = Ui_ScoreBoard()
        self._ui.setupUi(self)
        self._model = model
        self.setWindowTitle('Scores')
        self._ui.btn_continue.clicked.connect(self.onContinue)
        self.load_scores_from_model()

    def load_scores_from_model(self):
        players = self._model.get_data('players')
        self._ui.table_score.setColumnCount(12);
        self._ui.table_score.setRowCount(len(players));
        for i in range(11):
            self._ui.table_score.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem("Round {}".format(i+1)));
        self._ui.table_score.setHorizontalHeaderItem(11, QtWidgets.QTableWidgetItem("Total"));
        row_index = 0
        for player in players:
            row = player.get_player_score()
            self._ui.table_score.setVerticalHeaderItem(row_index, QtWidgets.QTableWidgetItem(player.get_player_name()));
            for key in row:
                self._ui.table_score.setItem(row_index, int(key)-1, QtWidgets.QTableWidgetItem(str(row[key])));
            self._ui.table_score.setItem(row_index, 11, QtWidgets.QTableWidgetItem(str(player.get_player_total_score())));
            row_index += 1
        self._ui.table_score.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self._ui.table_score.horizontalHeader().setStretchLastSection(True)
        self._ui.table_score.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def onContinue(self):
        self.signal_continue.emit()
