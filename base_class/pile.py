from base_class.deck import Deck

# Pile class.
# this class extends Deck class
class Pile(Deck):
    def __init__(self, deck_count=2, empty=True, cur_round=1):
        super().__init__(deck_count, empty, cur_round)
