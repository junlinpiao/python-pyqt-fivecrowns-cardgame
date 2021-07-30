from base_class.deck import Deck
# Hand class
class Hand(Deck):
    """Represents a hand of playing cards."""
 
    def __init__(self, deck_count=2, empty=True):
        super().__init__(deck_count, empty)
        self.new_picked = None
        self.arrange_order()
        self.selected_card_cards = []

    # Arrange cards in ascending order in the hand.
    def arrange_order(self):
        all_cards = self.cards
        self.cards = sorted(all_cards)

    # set picked card of the hand
    def set_new_picked(self, new_card):
        self.new_picked = new_card
    
    # get newly picked card from the pile
    def get_new_picked(self):
        return self.new_picked

    # set selected cards in the hand
    def set_selected_cards(self, cards_list):
        self.selected_card_cards = cards_list

    # get selected cards in the hand
    def get_selected_cards(self):
        return self.selected_card_cards

    # add a new card into the hand
    def add_card(self, new_card):
        self.cards.append(new_card)
        self.arrange_order()

    def is_run_or_book_selected(self):
        return self.is_run_selected() or self.is_book_selected()

    # check if the selected cards is a RUN.
    def is_run_selected(self):
        if len(self.selected_card_cards) < 3:
            return False
        tmp_cards = []
        tmp_wild_cards_count = 0
        for cur_card in self.selected_card_cards:
            if cur_card.is_wild() or cur_card.is_joker():
                tmp_wild_cards_count += 1
            else:
                tmp_cards.append(cur_card)
        if len(tmp_cards) == 0:
            return True
        tmp_cards = sorted(tmp_cards)
        first_card_suit = tmp_cards[0].get_suit()
        for tmp_card in tmp_cards:
            if tmp_card.get_suit() != first_card_suit:
                return False
        tmp_card = tmp_cards[0]
        prev_card_value = tmp_cards[0].get_value()
        for tmp_card in tmp_cards:
            if tmp_card == tmp_cards[0]:
                continue
            if tmp_card.get_value() != prev_card_value + 1:
                while tmp_card.get_value() != prev_card_value + 1:
                    if tmp_wild_cards_count > 0:
                        tmp_wild_cards_count -= 1
                        prev_card_value += 1
                    else:
                        return False
            prev_card_value += 1
        return True

    # check if the selected cards is a BOOK
    def is_book_selected(self):
        if len(self.selected_card_cards) < 3:
            return False
        first_card = 0
        for cur_card in self.selected_card_cards:
            if cur_card.is_wild() or cur_card.is_joker():
                continue
            first_card = cur_card
            break
        first_card_rank = first_card.get_rank()
        cur_card = None
        for cur_card in self.selected_card_cards:
            if cur_card.is_wild() or cur_card.is_joker():
                continue
            if cur_card.get_rank() != first_card_rank:
                return False
        return True

        