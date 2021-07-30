from PyQt5 import QtCore, QtWidgets, QtGui
from view.card_view import CardWidget
from base_class.hand import Hand

class HandWidget(QtWidgets.QWidget):

    signal_discardable = QtCore.pyqtSignal(bool)
    signal_droppable = QtCore.pyqtSignal(str)

    def __init__(self, hand_data, width, height, parent=None, no_actions=False):
        QtWidgets.QWidget.__init__(self)
        self.setParent(parent)
        self.setMouseTracking(True)
        self._no_actions=no_actions
        self._width = width
        self._height = height
        # self.setFixedSize(width, height)
        self._original_card_width = 100
        self._original_card_height = 120
        if self._no_actions:
            self.setMinimumHeight(self._original_card_height)
            # self.setFixedHeight(self._original_card_height)
        else:
            self.setMinimumHeight(self._original_card_height*4/3+1)
            # self.setFixedHeight(self._original_card_height*4/3+1)

        self._cur_sel_card = None
        self._cur_sel_card_id = -1
        # self.signal_discardable.emit(False)
        self._hand_data = hand_data
        self._cards = hand_data.get_cards()
        # set Minimum width
        card_count = len(self._cards)
        min_width = self._original_card_width * (card_count-1) / 3 + self._original_card_width
        self.setMinimumWidth(min_width)
        self._card_wgts = []
        self.create_cards()
        # self.arrange_cards()

        # QLabel for display "NEW" for new cards
        self._new_picked_label = QtWidgets.QLabel(self)
        self._new_picked_label.setText("NEW")
        self._new_picked_label.setStyleSheet("font-size:20px; color: red")
        self._new_picked_label.adjustSize()
        self._new_picked_label.hide()

    def resizeEvent(self, event):
        self._width = event.size().width()
        self._height = event.size().height()
        self.arrange_cards()
        
    def mousePressEvent(self, event):
        mousePos = event.pos()
        for card_widget in self._card_wgts:
            if card_widget.geometry().contains(mousePos):
                return
        for card_wgt in self._card_wgts:
            card_wgt.set_unselected()
        self.update_selected_cards()
        self._hand_data.set_selected_cards([])

    def calc_card_width(self, card_count):
        # width = int(self._width / card_count)
        # if width > self._original_card_width:
        #     return self._original_card_width
        # else:
        #     return width
        return self._original_card_width

    def calc_card_height(self):
        # return self._height*3/4
        return self._original_card_height
    
    def get_cur_sel_card_id(self):
        sel_cards = self._hand_data.get_selected_cards()
        if len(sel_cards) == 1:
            cur_sel_card = sel_cards[0]
            all_cards = self._hand_data.get_cards()
            return all_cards.index(cur_sel_card)
        else:
            return -1
    
    def create_cards(self):
        card_count = len(self._cards)
        card_width = self.calc_card_width(card_count)
        card_height = self.calc_card_height()
        for card in self._cards:
            rank = card.get_rank()
            suit = card.get_suit()
            self._card_wgts.append(CardWidget(card, card_width, card_height, self, False, self._no_actions))

    def arrange_cards(self):
        index = 0
        card_count = len(self._cards)
        card_width = self.calc_card_width(card_count)
        card_height = self.calc_card_height()
        card_overflow = False
        offset_width = self._width - card_width * card_count
        if offset_width < 0:
            offset_width = 0
            card_overflow = True
        offset_width = offset_width / 2
        for wgt in self._card_wgts:
            offset_selected = 0
            if wgt.selected():
                offset_selected = card_height / 3
            card_x_pos = offset_width+index*(card_width-1)
            if card_overflow:
                card_showed_width = (self._width - card_width) / (card_count-1)
                if card_showed_width < (card_width*2/3):
                    wgt.show_small_suit(True)
                else:
                    wgt.show_small_suit(False)
                card_x_pos = card_showed_width * index
            wgt.setGeometry(card_x_pos, self._height-card_height-offset_selected, card_width, card_height)
            index += 1
        
        # show "New Picked" Label
        new_picked_card = self._hand_data.get_new_picked()
        if new_picked_card != None:
            new_picked_id = self._cards.index(new_picked_card)
            label_pos_x = offset_width+new_picked_id*(card_width-1)
            if card_overflow:
                card_showed_width = (self._width - card_width) / (card_count-1)
                label_pos_x = new_picked_id*card_showed_width
            label_pos_y = self._height-card_height-self._new_picked_label.height()
            self._new_picked_label.move(label_pos_x, label_pos_y)
            self._new_picked_label.show()
    
    def update_selected_cards(self):
        selected_cards = []
        for card_wgt in self._card_wgts:
            if card_wgt.selected():
                sel_index = self._card_wgts.index(card_wgt)
                self._cards[sel_index]
                selected_cards.append(self._cards[sel_index])
        self._hand_data.set_selected_cards(selected_cards)
        if not self._no_actions:
            if self._hand_data.is_run_selected():
                self.signal_droppable.emit("run")
            elif self._hand_data.is_book_selected():
                self.signal_droppable.emit("book")
            else:
                self.signal_droppable.emit("none")

            if len(selected_cards) == 1:
                self.signal_discardable.emit(True)
            else:
                self.signal_discardable.emit(False)

    def set_cur_sel_card(self, sel_card_wgt):
        self.update_selected_cards()

        # hide NEW label when it is clicked
        new_picked_card = self._hand_data.get_new_picked()
        cur_sel_card_id = self._card_wgts.index(sel_card_wgt)
        if new_picked_card != None:
            new_picked_id = self._cards.index(new_picked_card)
            if new_picked_id == cur_sel_card_id:
                self._hand_data.set_new_picked(None)
                self._new_picked_label.hide()

        



