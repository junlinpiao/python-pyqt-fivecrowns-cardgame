from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from time import sleep
import time
import random

class GameController(QObject):

    signal_round_ended = pyqtSignal()
    signal_anyone_gone_out = pyqtSignal()

    def __init__(self, model, widget):
        super().__init__()
        self._model = model
        self._widget = widget
        if not self._model.get_data('dealt'):
            self.deal()

        # check if current turn is computer
        self.computer_speed = 1000
        random.seed(time.clock())
        self.which_pile_selected = 0
        self.computer_action()
        self._widget.load_from_model()
        self._widget.signal_discard_btn_clicked.connect(self.discard_selected)
        self._widget._ui.btn_drop.clicked.connect(self.drop_selected)
        self.connect_signals()
        
    # connect signals for pile widgets
    def connect_signals(self):
        try:
            self._widget.draw_pile_wgt.signal_pile_clicked.connect(self.pickup_from_draw)
        except:
            pass
        try:
            self._widget.discard_pile_wgt.signal_pile_clicked.connect(self.pickup_from_discard)
        except:
            pass
        for drop_hand_btn in self._widget.drop_hand_btns:
            drop_hand_btn.signal_clicked.connect(self.cancel_drop)
    
    # deal cards to the player
    def deal(self):
        self._model.deal()

    # put down the selected cards of the player hand
    def drop_selected(self):
        self._model.drop_selected()
        self._widget.load_from_model()
        self.connect_signals()
    
    # re-hold the put-down cards 
    def cancel_drop(self, drop_hand):
        self._model.cancel_drop(drop_hand)
        self._widget.load_from_model()
        self.connect_signals()

    # pick a card from the draw pile
    def pickup_from_draw(self):
        self._model.pickup_from_draw_pile()
        self._model.update_data('cur_state', 'picked')
        self._widget.load_from_model()
        self.connect_signals()

    # pick a card from the discard pile
    def pickup_from_discard(self):
        self._model.pickup_from_discard_pile()
        self._model.update_data('cur_state', 'picked')
        self._widget.load_from_model()
        self.connect_signals()

    # slot for what to do when the "Discard" button is clicked
    def discard_selected(self, sel_card_index):
        self._model.discard_from_cur_hand(sel_card_index)
        self._model.update_data('cur_state', 'discarded')
        if self.run_block_match() == True:
            if not self._model.get_data('anyone_gone_out'):
                self._model.set_gone_out_player()
                self.signal_anyone_gone_out.emit()
            # show dialog (xxx matches all runs and blocks, he goes out. others have only 1 chance)
        if self._model.is_cur_round_ended() == False:
            self.next_player()
        else:
            self.onRoundEnded()
            return

        self.computer_action()
        self._widget.load_from_model()
        self.connect_signals()
        
    # goto next player
    def next_player(self):
        self._model.next_player()
    
    # check if all cards match runs and blocks
    def run_block_match(self):
        return self._model.run_block_match()

    # round ended
    def onRoundEnded(self):
        self._model.calc_round_score()
        # self._model.init_new_round(False)
        self.signal_round_ended.emit()

    # computer actions
    def computer_action(self):
        # check if current turn is computer
        cur_player = self._model.get_data('cur_turn')
        if cur_player.get_player_type() == "computer":
            self.disable_all_game_btns()
            self.undo_cur_run_blocks()
            self._widget.set_computer_turn(True)
            QTimer.singleShot(self.computer_speed*2, self.cause_pickup_from_pile1)
        else:
            self.enable_game_btns()
            self._widget.set_computer_turn(False)

    def cause_pickup_from_pile1(self):
        # pick up from draw pile or discard pile
        self.which_pile_selected = random.randint(0,10)
        if self.which_pile_selected in range(4,11):
            # draw pile
            self._widget.draw_pile_wgt.causeEnterEvent()
        else:
            # discard pile
            self._widget.discard_pile_wgt.causeEnterEvent()
        QTimer.singleShot(self.computer_speed, self.cause_pickup_from_pile2)
            

    def cause_pickup_from_pile2(self):
        if self.which_pile_selected in range(4,11):
            self._widget.draw_pile_wgt.causeMousePressEvent()
            self._widget.draw_pile_wgt.causeLeaveEvent()
        else:
            self._widget.discard_pile_wgt.causeMousePressEvent()
            self._widget.discard_pile_wgt.causeLeaveEvent()
        self.run_books = []
        self.run_books = self._model.get_cur_runs_books()
        QTimer.singleShot(self.computer_speed, self.cause_pickup_run_book)

    def cause_pickup_run_book(self):
        card_wgts = self._widget.hand_wgt._card_wgts

        # books = self._model.get_cur_books()
        # for book_rank in books:
        #     for book_card in books[book_rank]:
        #         for card_wgt in card_wgts:
        #             if book_card==card_wgt.get_card():
        #                 card_wgt.causeCardPressEvent()
        #     QTimer.singleShot(self.computer_speed, self.cause_drop)
        #     return
        # runs = self._model.get_cur_runs()
        # for run in runs:
        #     for run_card in run:
        #         for card_wgt in card_wgts:
        #             if run_card==card_wgt.get_card():
        #                 card_wgt.causeCardPressEvent()
        #     QTimer.singleShot(self.computer_speed, self.cause_drop)
        #     return

        if len(self.run_books)>0:
            run_book = self.run_books.pop()
            for run_book_card in run_book:
                for card_wgt in card_wgts:
                    if run_book_card==card_wgt.get_card():
                        card_wgt.causeCardPressEvent()
            QTimer.singleShot(self.computer_speed, self.cause_drop)
        else:
            # if there is no more books or runs, now discard
            cur_player = self._model.get_data('cur_turn')
            cur_cards = cur_player.get_hand().get_cards()
            anyone_gone_out = self._model.get_data('anyone_gone_out')
            max_card_id = 0
            max_card_value = 0
            for cur_card_id in range(len(cur_cards)):
                if not anyone_gone_out:
                    if cur_cards[cur_card_id].is_joker() or cur_cards[cur_card_id].is_wild():
                        continue
                if max_card_value < cur_cards[cur_card_id].get_value():
                    max_card_value = cur_cards[cur_card_id].get_value()
                    max_card_id = cur_card_id
            self.cause_discard_id = max_card_id
            card_wgts[max_card_id].causeCardPressEvent()
            QTimer.singleShot(self.computer_speed, self.cause_discard)

    def cause_drop(self):
        self.drop_selected()
        QTimer.singleShot(self.computer_speed, self.cause_pickup_run_book)

    def cause_discard(self):
        self.discard_selected(self.cause_discard_id)

    def disable_all_game_btns(self):
        self._widget._ui.btn_discard.setEnabled(False)
        self._widget._ui.btn_drop.setEnabled(False)
        self._widget._ui.btn_quit.setEnabled(False)
        self._widget._ui.btn_save.setEnabled(False)
        self._widget._ui.btn_view_scores.setEnabled(False)

    def enable_game_btns(self):
        self._widget._ui.btn_quit.setEnabled(True)
        self._widget._ui.btn_save.setEnabled(True)
        self._widget._ui.btn_view_scores.setEnabled(True)

    def undo_cur_run_blocks(self):
        cur_player = self._model.get_data('cur_turn')
        cur_player.cancel_all_drops()
        # cur_drop_hands = cur_player.get_drop_hands()
        # for cur_drop_id in range(len(cur_drop_hands)):
        #     cur_player.cancel_drop(cur_drop_hands[cur_drop_id])






    