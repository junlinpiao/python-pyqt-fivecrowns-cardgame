from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5 import QtWidgets
from controller.game_controller import GameController
from view.menu_view import MenuWidget
from view.setting_view import SettingWidget
from view.saved_games_view import SavedGamesWidget
from view.coin_toss_view import CoinTossWidget
from view.game_board_view import GameBoardWidget
from view.score_board_view import ScoreBoardWidget
from view.game_over_view import GameOverWidget
from view.round_result_view import RoundResultWidget
from view.save_game_view import SaveGameWidget
from view.quit_confirm_view import QuitConfirmWidget
from view.go_out_view import GoOutWidget

class MainController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
        # shows Menu window at first.
        self.cur_opened_widget = None
        self.game_board_wgt = None
        self.show_menu()

    # close currently opened window
    def close_current_widget(self):
        if self.cur_opened_widget != None:
            self.cur_opened_widget.close()

    # set current widget as "widget"
    def set_current_widget(self, widget):
        self.close_current_widget()
        self.cur_opened_widget = widget
        self.cur_opened_widget.show()

    def show_menu(self):
        # create menu window and connect signals
        self.menu_wgt = MenuWidget()
        self.menu_wgt.signal_switch_setting.connect(self.show_setting)
        self.menu_wgt.signal_switch_saved_games.connect(self.show_saved_games)
        # set menu as current widget
        self.set_current_widget(self.menu_wgt)

    def show_setting(self):
        # create setting window and connect signals
        self.setting_wgt = SettingWidget(self._model)
        self.setting_wgt.signal_switch_menu.connect(self.show_menu)
        self.setting_wgt.signal_switch_coin_toss.connect(self.show_coin_toss)
        # set setting as current widget
        self.set_current_widget(self.setting_wgt)

    def show_saved_games(self):
        # create saved games window and connect signals
        self.saved_game_wgt = SavedGamesWidget(self._model)
        self.saved_game_wgt.signal_switch_menu.connect(self.show_menu)
        self.saved_game_wgt.signal_switch_game_board.connect(self.show_game_board)
        # set saged games as current widget
        self.set_current_widget(self.saved_game_wgt)

    def show_coin_toss(self):
        # create coin toss window and connect signals
        self.coin_toss_wgt = CoinTossWidget(self._model)
        self.coin_toss_wgt.signal_switch_menu.connect(self.show_menu)
        self.coin_toss_wgt.signal_switch_game_board.connect(self.show_game_board)
        # set coin toss as current widget
        self.set_current_widget(self.coin_toss_wgt)

    def show_game_board(self):
        try:
            # create game board window and connect signals
            self.game_board_wgt = GameBoardWidget(self._model)
            self.game_board_wgt.hide()
            self.game_board_wgt.signal_quit_game.connect(self.show_quit_confirm)
            self.game_board_wgt.signal_switch_score_board.connect(self.show_score_board)
            self.game_board_wgt.signal_save_game.connect(self.show_save_game)
            self.game = GameController(self._model, self.game_board_wgt)
            self.game.signal_round_ended.connect(self.show_round_result)
            self.game.signal_anyone_gone_out.connect(self.show_gone_out)
            # set game board as current widget
            self.set_current_widget(self.game_board_wgt)
        except:
            if self.game_board_wgt:
                self.game_board_wgt.close()
            QtWidgets.QMessageBox.warning(None, "Error", "Could not load game. <br>This file might be invalid.<br>Try again.")

    def show_score_board(self):
        # create scores window and connect signals
        self.score_board_wgt = ScoreBoardWidget(self._model)
        self.score_board_wgt.signal_continue.connect(self.show_game_board)
        self.set_current_widget(self.score_board_wgt)

    def show_final_score_board(self):
        # create the last round score window and connect signals
        self.score_board_wgt = ScoreBoardWidget(self._model)
        self.score_board_wgt.signal_continue.connect(self.show_game_over_view)
        self.set_current_widget(self.score_board_wgt)

    def show_round_result(self):
        # create round result window and connect signals
        self.round_result_wgt = RoundResultWidget(self._model)
        ended_round = self._model.get_data('cur_round')
        if ended_round >= 11:
            self.round_result_wgt.signal_continue.connect(self.show_game_over_view)
        else:
            self.round_result_wgt.signal_continue.connect(self.next_round)
        self.set_current_widget(self.round_result_wgt)
        self.game = None

    def next_round(self):
        # show the game board of the new round
        self._model.init_new_round(False)
        self.show_game_board()

    def show_game_over_view(self):
        # create game over window and connect signals
        self.game_over_wgt = GameOverWidget(self._model)
        self.game_over_wgt.signal_switch_scores.connect(self.show_final_score_board)
        self.game_over_wgt.signal_quit_game.connect(self.quit_game)
        self.set_current_widget(self.game_over_wgt)

    def show_save_game(self):
        # create save window and connect signals
        self.save_game_wgt = SaveGameWidget(self._model)
        self.save_game_wgt.signal_switch_game_board.connect(self.show_game_board)
        self.set_current_widget(self.save_game_wgt)

    def show_save_and_exit(self):
        self.save_game_wgt = SaveGameWidget(self._model, True)
        self.save_game_wgt.signal_switch_game_board.connect(self.show_game_board)
        self.save_game_wgt.signal_quit_game.connect(self.quit_game)
        self.set_current_widget(self.save_game_wgt)

    def show_quit_confirm(self):
        self.quit_confirm_wgt = QuitConfirmWidget()
        self.quit_confirm_wgt.signal_switch_save_game.connect(self.show_save_and_exit)
        self.quit_confirm_wgt.signal_quit_game.connect(self.quit_game)
        self.quit_confirm_wgt.signal_switch_game_board.connect(self.show_game_board)
        self.set_current_widget(self.quit_confirm_wgt)

    def show_gone_out(self):
        self.gone_out_wgt = GoOutWidget(self._model)
        self.gone_out_wgt.signal_continue.connect(self.show_game_board)
        self.set_current_widget(self.gone_out_wgt)
        self.game = None

    def quit_game(self):
        self._model.clear_data()
        self.show_menu()
        

