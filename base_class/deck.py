from base_class.card import Card
import random

# Deck class
class Deck:
    def __init__(self, deck_count=2, empty=True, cur_round = 1):
        """Initializes the Deck with 58 cards."""
        ranks = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ['diamond', 'heart', 'club', 'spade', 'star']
        self.deck_count = deck_count
        self.cards = []
        # initialize cards
        if not empty:
            for i in range(deck_count):
                for suit in suits:
                    for rank in ranks:
                        card = Card(suit, rank, cur_round)
                        self.cards.append(card)
                self.cards.append(Card('', "J1", cur_round))
                self.cards.append(Card('', "J2", cur_round))
                self.cards.append(Card('', "J3", cur_round))
            self.shuffle()

    # shuffle deck
    def shuffle(self):
        random.shuffle(self.cards)
    
    # get the number of cards in the deck.
    def deck_len(self):
        return len(self.cards)
    
    # add a card to the deck
    def add_card(self, card):
        self.cards.append(card)

    # add many cards to the deck
    def add_cards(self, card_list):
        self.cards.extend(card_list)

    # pop a card from the deck
    def pop_card(self, i=-1):
        return self.cards.pop(i)

    # get the top card of the deck
    def get_last_card(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None

    # get all cards of the deck
    def get_cards(self):
        return self.cards

    # convert deck to string format to save into txt file.
    def toStringFormat(self):
        short_suits = {'diamond':'D', 'heart':'H', 'club':'C', 'spade':'S', 'star':'T'}
        short_ranks = {"3":'3', "4":'4', "5":'5', "6":'6', "7":'7', "8":'8', "9":'9', "10":'X', "J":'J', "Q":'Q', "K":'K'}
        result_str = ""
        for card in self.cards:
            card_str = ""
            card_rank = card.get_rank()
            card_suit = card.get_suit()
            if card_rank == "J1" or card_rank == "J2" or card_rank == "J3":
                card_str = card_rank
            else:
                card_str = short_ranks[card_rank] + short_suits[card_suit]
            result_str = result_str + card_str + " "
        return result_str

    # throw away all cards of the deck.
    def clear_cards(self):
        self.cards = []

    # load cards from the saved file into the deck
    def load_from_saved(self, deck_str, cur_round):
        long_ranks = {'3':"3", '4':"4", '5':"5", '6':"6", '7':"7", '8':"8", '9':"9", 'X':"10", 'J':"J", 'Q':"Q", 'K':"K"}
        long_suits = {'D':'diamond', 'H':'heart', 'C':'club', 'S':'spade', 'T':'star'}
        deck_str = deck_str.strip()
        cards_str = deck_str.split(" ")
        for card_str in cards_str:
            card_rank = card_str[0]
            card_suit = card_str[1]
            if card_str == "J1" or card_str == "J2" or card_str == "J3":
                card = Card("", card_str, cur_round)
            else:
                card = Card(long_suits[card_suit], long_ranks[card_rank], cur_round)
            self.cards.append(card)
        return len(cards_str)