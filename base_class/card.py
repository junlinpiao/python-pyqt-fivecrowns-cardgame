# card class
class Card:
    
    values = {"3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "J1":50, "J2":50, "J3":50}
    values_for_order = {"3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "J1":2, "J2":2, "J3":2}
 
    def __init__(self, suit='spade', rank='3', cur_round=1):
        self.suit = suit
        self.rank = rank
        self._is_wild = False
        self.cur_round = cur_round
        self.value = self.values[rank]
        self.value_for_order = self.values_for_order[rank]
        if self.value == cur_round + 2:
            self._is_wild = True
            self.value = 20
            self.value_for_order = 1

    # get suit of this card
    def get_suit(self):
        return self.suit

    # get rank of this card
    def get_rank(self):
        return self.rank

    # get the value of this card
    def get_value(self):
        return self.value

    # check if this card is a wild card
    def is_wild(self):
        return self._is_wild

    # check if this card is a Joker
    def is_joker(self):
        if self.rank == "J1" or self.rank == "J2" or self.rank == "J3":
            return True
        else:
            return False

    # Overriding "<" operator
    def __lt__(self, other):
        t1 = self.value_for_order, self.suit
        t2 = other.value_for_order, other.suit
        # t1 = self.suit, self.values[self.rank]
        # t2 = other.suit, other.values[other.rank]
        return t1 < t2
