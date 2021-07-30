from PyQt5 import QtCore, QtWidgets
from view.game_board_view_ui import Ui_GameBoard
from view.hand_view import HandWidget
from view.pile_view import PileWidget
from view.indexed_button import IndexedButton

class GameBoardWidget(QtWidgets.QWidget):
    
    signal_quit_game = QtCore.pyqtSignal()
    signal_switch_score_board = QtCore.pyqtSignal()
    signal_discard_btn_clicked = QtCore.pyqtSignal(int)
    signal_save_game = QtCore.pyqtSignal()
    ranks = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, model):
        QtWidgets.QWidget.__init__(self)
        self._ui = Ui_GameBoard()
        self._ui.setupUi(self)
        self._model = model

        self._cur_state = self.current_state()
        self.setWindowTitle('Five Crowns Card Game')
        self.setMinimumSize(750, 550)
        self._ui.wgt_hand.setMinimumHeight(160)
        self._ui.wgt_draw_pile.setMinimumHeight(120)
        self._ui.wgt_discard_pile.setMinimumHeight(120)
        # self.load_from_model()
        self.showMaximized()
        self._ui.btn_quit.clicked.connect(self.onQuit)
        self._ui.btn_save.clicked.connect(self.onSave)
        self._ui.btn_discard.clicked.connect(self.onDiscard)
        self._ui.btn_view_scores.clicked.connect(self.onShowScores)

        self.is_computer_turn = False
        self.scroll_vLayout = None
        self.drop_hand_wgts = []
        self.drop_hand_btns = []


    def current_state(self):
        cur_state = self._model.get_data('cur_state')
        return cur_state

    def set_computer_turn(self, com_turn):
        self.is_computer_turn = com_turn

    def setDiscardButtonEnabled(self, bEnable):
        self._ui.btn_discard.setEnabled(bEnable)

    def setDropButtonEnabled(self, str_state):
        if str_state == "run":
            self._ui.btn_drop.setText("Drop")
            self._ui.btn_drop.setEnabled(True)
        elif str_state == "book":
            self._ui.btn_drop.setText("Drop")
            self._ui.btn_drop.setEnabled(True)
        elif str_state == "none":
            self._ui.btn_drop.setText("Drop")
            self._ui.btn_drop.setEnabled(False)

    def setSaveButtonShow(self):
        cur_state = self._model.get_data('cur_state')
        if cur_state == "picked":
            self._ui.btn_save.setEnabled(False)
        else:
            self._ui.btn_save.setEnabled(True)

    def arrange_hand_pile(self):
        hand_geometry = self._ui.wgt_hand.geometry()
        draw_pile_geometry = self._ui.wgt_draw_pile.geometry()
        discard_pile_geometry = self._ui.wgt_discard_pile.geometry()
        try:
            self.hand_wgt.setGeometry(hand_geometry)
            draw_pile_x = draw_pile_geometry.x() + (draw_pile_geometry.width()-self.draw_pile_wgt.width())/2
            draw_pile_y = draw_pile_geometry.y() + draw_pile_geometry.height()-self.draw_pile_wgt.height()
            self.draw_pile_wgt.move(draw_pile_x, draw_pile_y)
            discard_pile_x = discard_pile_geometry.x() + (discard_pile_geometry.width()-self.discard_pile_wgt.width())/2
            discard_pile_y = discard_pile_geometry.y() + discard_pile_geometry.height()-self.discard_pile_wgt.height()
            self.discard_pile_wgt.move(discard_pile_x, discard_pile_y)
        except:
            pass

    def resizeEvent(self, event):
        self.arrange_hand_pile()
        QtWidgets.QWidget.resizeEvent(self, event)

    def load_from_model(self):
        # close old widgets.
        try:
            if self.discard_pile_wgt:
                self.discard_pile_wgt.close()
        except:
            pass
        try:
            if self.draw_pile_wgt:
                self.draw_pile_wgt.close()
        except:
            pass
        try:
            if self.hand_wgt:
                self.hand_wgt.close()
        except:
            pass

        # display round 
        cur_round = self._model.get_data('cur_round')
        self._ui.lbl_round.setText("Round {}".format(cur_round))
        self._ui.lbl_wild_card.setText("<span style='font-size: 30px; color: red; font-weight: bold'>[{}]</span> is wild card".format(self.ranks[cur_round-1]))

        # display current turn
        cur_turn = self._model.get_data('cur_turn')
        cur_state_msg = "<br><span style='color: red'>\"{}\" 's turn!</span><br><br>".format(cur_turn.get_player_name())
        gone_out = self._model.get_data('anyone_gone_out')
        if gone_out:
            gone_out_player = self._model.get_data('first_gone_out')
            cur_state_msg = cur_state_msg + "<span style='color: blue'>\"{}\" has gone out first. <br>You have only this chance.<br><br></span>".format(gone_out_player.get_player_name())
        
        self._cur_state = self.current_state()
        if self._cur_state == "picked":
            self.setDiscardButtonEnabled(False)
            self.setDropButtonEnabled("none")
            cur_state_msg = cur_state_msg + "Please drop down runs and books and discard an unuseful card from your hand."
        else: 
            self.setDiscardButtonEnabled(False)
            self.setDropButtonEnabled("none")
            cur_state_msg = cur_state_msg + "Please pick up a card from draw pile or discard pile."
        self._ui.lbl_cur_turn.setText(cur_state_msg)

        # hand widget
        cur_hand = self._model.get_data('cur_turn').get_hand()
        cur_hand.arrange_order()
        is_available = self.current_state() == "discarded"
        # is_available = False
        self.hand_wgt = HandWidget(cur_hand, self.width() - 100, self.height()/4, self, is_available or self.is_computer_turn)
        self.hand_wgt.show()
        if self._cur_state == "picked":
            self.hand_wgt.signal_discardable.connect(self.setDiscardButtonEnabled)
        self.hand_wgt.signal_droppable.connect(self.setDropButtonEnabled)

        # draw pile widget
        pile_width = 100
        pile_height = 120

        draw_pile = self._model.get_data('draw_pile')
        draw_top_card = draw_pile.get_last_card()
        self.draw_pile_wgt = PileWidget(self._model, draw_top_card, pile_width, pile_height, self, True, not is_available or self.is_computer_turn)
        self.draw_pile_wgt.show()

        discard_pile = self._model.get_data('discard_pile')
        discard_top_card = discard_pile.get_last_card()
        if discard_top_card != None:
            self.discard_pile_wgt = PileWidget(self._model, discard_top_card, pile_width, pile_height, self, False, not is_available or self.is_computer_turn)
            self.discard_pile_wgt.show()
        self.arrange_hand_pile()
        # show/hide save button
        self.setSaveButtonShow()
        # set run_book widget
        self.setup_drop_widget()

    def setup_drop_widget(self):
        scroll_wgt = self._ui.scrollAreaWidgetContents
        if self.scroll_vLayout == None:
            self.scroll_vLayout = QtWidgets.QVBoxLayout(scroll_wgt)

        # clear all layouts and widgets
        for drop_wgt in self.drop_hand_wgts:
            drop_wgt.close()
        self.drop_hand_wgts = []
        for drop_hand_btn in self.drop_hand_btns:
            drop_hand_btn.close()
        self.drop_hand_btns = []
        for i in range(self.scroll_vLayout.count()):
            h_layout_item = self.scroll_vLayout.itemAt(i)
            self.scroll_vLayout.removeItem(h_layout_item)

        cur_player = self._model.get_data('cur_turn')
        cur_drop_hands = cur_player.get_drop_hands()
        for drop_hand in cur_drop_hands:
            scroll_hLayout = QtWidgets.QHBoxLayout()
            drop_hand_wgt = HandWidget(drop_hand, scroll_wgt.width() - 20, 160, scroll_wgt, True)
            drop_hand_wgt.show()
            btn_undo = IndexedButton(scroll_wgt, drop_hand)
            btn_undo.setText("Cancel")
            btn_undo.setMinimumSize(QtCore.QSize(0, 50))
            btn_undo.setStyleSheet("font-size:15px")
            btn_undo.show()
            if self.is_computer_turn:
                btn_undo.setEnabled(False)
            else:
                btn_undo.setEnabled(True)
            scroll_hLayout.addWidget(drop_hand_wgt)
            scroll_hLayout.addWidget(btn_undo)
            scroll_hLayout.setStretch(0, 5)
            scroll_hLayout.setStretch(1, 1)
            self.drop_hand_btns.append(btn_undo)
            self.drop_hand_wgts.append(drop_hand_wgt)
            self.scroll_vLayout.addLayout(scroll_hLayout)
        

    def update_model(self):
        pass

    def onQuit(self):
        self.signal_quit_game.emit()

    def onSave(self):
        self.signal_save_game.emit()

    def onDiscard(self):
        selected_card_id = self.hand_wgt.get_cur_sel_card_id()
        self.signal_discard_btn_clicked.emit(selected_card_id)

    def onShowScores(self):
        self.signal_switch_score_board.emit()

    
    # unused slot, but must be exist.
    def set_cur_sel_card():
        pass


        