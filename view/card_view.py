from PyQt5 import QtCore, QtWidgets, QtGui
from base_class.card import Card
from time import sleep
# Window class that shows a card.
class CardWidget(QtWidgets.QWidget):
    
    signal_card_clicked = QtCore.pyqtSignal(QtWidgets.QWidget)

    def __init__(self, card, width, height, parent=None, show_backface=False, no_actions=False):
        QtWidgets.QWidget.__init__(self)
        self.setParent(parent)
        self._parent = parent
        self._show_backface = show_backface
        self._no_actions = no_actions
        self.setMouseTracking(True)
        self._back_color = QtGui.QColor(255,255,255)
        self._selected = False
        self._suit = card.get_suit()
        self.suits = {'diamond': '\u2666', 'heart': '\u2665', 'club': '\u2663', 'spade': '\u2660', 'star': '\u2605'}
        self.colors = {'club': 'green', 'diamond': 'blue', 'heart': 'red', 'spade': 'black', 'star': '#ffa720'}
        self._suit_symbol = ""
        self._card_color = "purple"
        if self._suit != "":
            self._suit_symbol = self.suits[self._suit]
            self._card_color = self.colors[self._suit]
        self._rank = card.get_rank()
        self._card = card
        self._width = width
        self._height = height
        # self.setFixedSize(width, height)
        self.label_1 = QtWidgets.QLabel(self)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_special_1 = QtWidgets.QLabel(self)
        self.label_special_2 = QtWidgets.QLabel(self)
        self.label_suit = QtWidgets.QLabel(self)
        self.label_suit_small = QtWidgets.QLabel(self)
        self.label_suit_small.hide()
        self.drawWidget()
        self.signal_card_clicked.connect(self._parent.set_cur_sel_card)

    def get_suit(self):
        return self._suit
    
    def get_rank(self):
        return self._rank

    def get_card(self):
        return self._card

    def show_small_suit(self, bShow):
        if bShow == True:
            self.label_suit_small.show()
        else:
            self.label_suit_small.hide()

    def resizeEvent(self, event):
        self._width = event.size().width()
        self._height = event.size().height()
    
    def enterEvent(self, event):
        if not self._no_actions:
            self._back_color = QtGui.QColor(180,180,180)
            self.update()
        
    def leaveEvent(self, event):
        if not self._no_actions:
            self._back_color = QtGui.QColor(255,255,255)
            self.update()

    def mousePressEvent(self, event):
        if not self._no_actions:
            if self._selected:
                self.card_down()
            else:
                self.card_up()
            self._selected = not self._selected
            self.signal_card_clicked.emit(self)
    
    def causeCardPressEvent(self):
        if self._selected:
            self.card_down()
        else:
            self.card_up()
        self._selected = not self._selected
        self.signal_card_clicked.emit(self)
    
    def card_up(self):
        pos = self.pos()
        self.move(pos.x(), pos.y()-int(self._height/3))

    def card_down(self):
        pos = self.pos()
        self.move(pos.x(), pos.y()+int(self._height/3))

    def selected(self):
        return self._selected

    def is_joker(self):
        if self._rank == "J1" or self._rank == "J2" or self._rank == "J3":
            return True
        else:
            return False
    
    def set_unselected(self):
        if self._selected == True:
            self._selected = False
            self.card_down()
    
    def flip(self, delay = 0):
        self._show_backface = not self._show_backface
        self.update()
        self.drawWidget()
        sleep(delay)

    def paintCard(self):
        painter = QtGui.QPainter(self)
        painter.fillRect(QtCore.QRect(0,0,self._width,self._height),self._back_color)
        if self._show_backface:
            painter.fillRect(QtCore.QRect(0,0,self._width,self._height),QtGui.QBrush(QtCore.Qt.DiagCrossPattern))
        painter.drawRect(0,0,self._width-1, self._height-1)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.fillRect(QtCore.QRect(0,0,self._width,self._height),self._back_color)
        if self._show_backface:
            painter.fillRect(QtCore.QRect(0,0,self._width,self._height),QtGui.QBrush(QtCore.Qt.DiagCrossPattern))
        painter.drawRect(0,0,self._width-1, self._height-1)

    def drawWidget(self):
        if self._show_backface:
            self.label_1.hide()
            self.label_4.hide()
            self.label_special_1.hide()
            self.label_special_2.hide()
            self.label_suit.hide()
        else:
            self.label_1.show()
            self.label_4.show()
            self.label_special_1.show()
            self.label_special_2.show()
            self.label_suit.show()
            gap = self._height / 30
            rank_font_size = int(self._height/5)
            if self.is_joker():
                rank_font_size = int(self._width / 6)
                self.label_1.hide()
                self.label_4.hide()
                self.label_special_1.setText("J\nO\nK\nE\nR")
                self.label_special_2.setText("J\nO\nK\nE\nR")
                self.label_special_1.setAlignment(QtCore.Qt.AlignCenter)
                self.label_special_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_special_1.setStyleSheet("font-size: {}px; color: {}; font-weight: bold;".format(rank_font_size, self._card_color))
                self.label_special_2.setStyleSheet("font-size: {}px; color: {}; font-weight: bold;".format(rank_font_size, self._card_color))
                self.label_special_1.adjustSize()
                self.label_special_2.adjustSize()
                self.label_special_1.move(gap,0)
                self.label_special_2.move(self._width-self.label_special_2.width()-gap,self._height-self.label_special_2.height())
                self.label_suit.setText('\u2603')
                self.label_suit.setStyleSheet("font-size: {}px; color: {};".format(rank_font_size*2, self._card_color))
                self.label_suit.adjustSize()
                self.label_suit.move(self._width/2-self.label_suit.width()/2,self._height/2-self.label_suit.height()/2-gap*2)
            else:
                self.label_special_1.hide()
                self.label_special_2.hide()
                self.label_1.setText(self._rank)
                self.label_4.setText(self._rank)
                self.label_1.setStyleSheet("font-size: {}px; color: {}; font-weight: bold;".format(rank_font_size, self._card_color))
                self.label_4.setStyleSheet("font-size: {}px; color: {}; font-weight: bold;".format(rank_font_size, self._card_color))
                self.label_1.adjustSize()
                self.label_4.adjustSize()
                self.label_1.move(gap,0)
                self.label_4.move(self._width-self.label_4.width()-gap,self._height-self.label_4.height())
                self.label_suit.setText(self._suit_symbol)
                self.label_suit.setStyleSheet("font-size: {}px; color: {};".format(rank_font_size*2, self._card_color))
                self.label_suit.adjustSize()
                self.label_suit.move(self._width/2-self.label_suit.width()/2,self._height/2-self.label_suit.height()/2-gap*2)
                self.label_suit_small.setText(self._suit_symbol)
                self.label_suit_small.setStyleSheet("font-size: {}px; color: {};".format(rank_font_size, self._card_color))
                self.label_suit_small.adjustSize()
                self.label_suit_small.move(gap+(self.label_1.width()-self.label_suit_small.width())/2, self.label_1.height()-gap)

