from base_class.hand import Hand
# Player class.
class Player:
    def __init__(self, pid, pname, ptype):
        self.player_id = pid
        self.player_name = pname
        self.player_hand = Hand()
        self.drop_hands = []
        self.player_type = ptype
        self.player_score = {}
        self.total_score = 0

    # put down the selected cards(run or block)
    def drop_selected(self):
        sel_cards = self.player_hand.get_selected_cards()
        drop_hand = Hand()
        for sel_card in sel_cards:
            cards = self.player_hand.get_cards()
            sel_id = cards.index(sel_card)
            drop_hand.add_card(self.player_hand.pop_card(sel_id))
        self.player_hand.set_selected_cards([])
        self.drop_hands.insert(0,drop_hand)
    
    # hold on put-down runs or blocks
    def cancel_drop(self, drop_hand):
        self.player_hand.add_cards(drop_hand.get_cards())
        drop_hand_id = self.drop_hands.index(drop_hand)
        self.drop_hands.pop(drop_hand_id)

    # hold on put-down runs or blocks
    def cancel_all_drops(self):
        for drop_hand in self.drop_hands:
            self.player_hand.add_cards(drop_hand.get_cards())
        self.drop_hands = []
    
    # get put-down cards
    def get_drop_hands(self):
        return self.drop_hands

    # get the type of the player -  computer or human
    def get_player_type(self):
        return self.player_type
    
    # get the identifier of the player
    def get_player_id(self):
        return self.player_id

    # get the name of the player
    def get_player_name(self):
        return self.player_name

    # get the score of the player
    def get_player_score(self):
        return self.player_score
    
    # get the current total score of the player
    def get_player_total_score(self):
        return self.total_score

    # get the cards in the player's hand
    def get_hand(self):
        return self.player_hand

    # put all cards from the hand of the player
    def clear_hand(self):
        self.player_hand.clear_cards()
        for drop_hand in self.drop_hands:
            drop_hand.clear_cards()
        self.drop_hands = []

    # calculate the score of the round.
    def calc_cur_score(self, cur_round):
        cards = self.player_hand.get_cards()
        t_score = 0
        for card in cards:
            t_score += card.get_value()
        self.player_score[str(cur_round)] = t_score
        self.total_score += t_score
    
    # load the score of the player from the saved file
    def load_from_saved_score(self, score):
        self.total_score = score

    # load the cards of the hand from the saved file
    def load_from_saved_hand(self, hand_data, cur_round):
        return self.player_hand.load_from_saved(hand_data, cur_round)

