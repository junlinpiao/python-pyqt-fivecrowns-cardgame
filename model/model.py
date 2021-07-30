from PyQt5.QtCore import QObject, pyqtSignal
import os
from base_class.card import Card
from base_class.hand import Hand
from base_class.pile import Pile
from base_class.human import Human
from base_class.computer import Computer

class Model(QObject):

    def __init__(self):
        super().__init__()

        self.saved_game_file_extension = ".txt"
        self.saved_game_files_path = os.getcwd() + "/saved_games"
        self.init_default_game_data()
        self.init_new_round(True)
        
    # initialize default game data
    def init_default_game_data(self):
        self._game_data = {}
        self._game_data['play_state'] = 0   # 0: new game, 1: load saved game
        self._game_data['deck_count'] = 2
        self._game_data['player_count'] = {"computer": 1, "human": 1}
        self._game_data['players'] = []
        self._game_data['cur_round'] = 0
        self._game_data['first_gone_out'] = None
        self._game_data['cur_state'] = "discarded"
        
    # initialize data for the new round
    def init_new_round(self, new_game):
        if new_game:
            self._game_data['cur_round'] = 1
        else:
            self._game_data['cur_round'] = self._game_data['cur_round'] + 1
        self._game_data['draw_pile'] = Pile(self._game_data['deck_count'], False, self._game_data['cur_round'])
        self._game_data['discard_pile'] = Pile()
        self._game_data['anyone_gone_out'] = False
        self._game_data['cur_turn'] = self._game_data['first_gone_out']
        self._game_data['round_last_loop_id'] = 0
        self.clear_player_hands()
        self._game_data['dealt'] = False
    
    # delete all cards of the players
    def clear_player_hands(self):
        players = self._game_data['players']
        for player in players:
            player.clear_hand()
    
    # calculate the scores of the players in the round
    def calc_round_score(self):
        players = self._game_data['players']
        for player in players:
            player.calc_cur_score(self._game_data['cur_round'])

    # get scores of the players
    def get_scores(self):
        score_data = {}
        players = self._game_data['players']
        for player in players:
            player_name = player.get_player_name()
            player_score = player.get_player_score()
            score_data[player_name] = player_score
        return score_data

    # create player objects
    def create_players(self):
        computer_count = self._game_data['player_count']['computer']
        human_count = self._game_data['player_count']['human']
        self._game_data['players'] = []
        tmp_id = 0
        if computer_count == 1:
            self._game_data['players'].append(Computer(tmp_id, 'Computer'))
            tmp_id += 1
        else:
            for i in range(computer_count):
                self._game_data['players'].append(Computer(tmp_id, 'Computer {}'.format(i+1)))
                tmp_id += 1
        if human_count == 1:
            self._game_data['players'].append(Human(tmp_id, 'Human'))
            tmp_id += 1
        else:
            for i in range(human_count):
                self._game_data['players'].append(Human(tmp_id, 'Human {}'.format(i+1)))
                tmp_id += 1
        self._game_data['cur_turn'] = self._game_data['players'][0]

    # deal cards to the players
    def deal(self):
        deal_count = self._game_data['cur_round'] + 2
        players = self._game_data['players']
        draw_pile = self._game_data['draw_pile']
        discard_pile = self._game_data['discard_pile']
        for i in range(deal_count):
            for player in players:
                player_hand = player.get_hand()
                player_hand.add_card(draw_pile.pop_card())
        discard_pile.add_card(draw_pile.pop_card())
        self._game_data['dealt'] = True
    
    # pick up a card from the draw pile
    def pickup_from_draw_pile(self):
        cur_player = self._game_data['cur_turn']
        draw_pile = self._game_data['draw_pile']
        player_hand = cur_player.get_hand()
        popped_card = draw_pile.pop_card()
        player_hand.add_card(popped_card)
        player_hand.set_new_picked(popped_card)
        if draw_pile.deck_len() == 0:
            tmp = self._game_data['draw_pile']
            self._game_data['draw_pile'] = self._game_data['discard_pile']
            self.self._game_data['discard_pile'] = tmp
            self._game_data['draw_pile'].shuffle()
            self._game_data['discard_pile'].add_card(self._game_data['draw_pile'].pop_card())

    # pick up a card from the discard pile
    def pickup_from_discard_pile(self):
        cur_player = self._game_data['cur_turn']
        discard_pile = self._game_data['discard_pile']
        player_hand = cur_player.get_hand()
        popped_card = discard_pile.pop_card()
        player_hand.add_card(popped_card)
        player_hand.set_new_picked(popped_card)

    # discard a card from the hand of the current player
    def discard_from_cur_hand(self, cur_card_index):
        cur_player = self._game_data['cur_turn']
        discard_pile = self._game_data['discard_pile']
        player_hand = cur_player.get_hand()
        player_hand.set_new_picked(None)
        player_hand.set_selected_cards([])
        discard_pile.add_card(player_hand.pop_card(cur_card_index))

    # put down the selected cards
    def drop_selected(self):
        cur_player = self._game_data['cur_turn']
        cur_player.drop_selected()

    # rehold the put-down cards
    def cancel_drop(self, drop_hand):
        cur_player = self._game_data['cur_turn']
        cur_player.cancel_drop(drop_hand)

    # set data for the next turn.
    def next_player(self):
        cur_player = self._game_data['cur_turn']
        players = self._game_data['players']
        player_count = len(players)
        cur_player_id = players.index(cur_player)
        next_player_id = (cur_player_id + 1) % player_count
        self._game_data['cur_turn'] = players[next_player_id]

    # set the player who has gone out first
    def set_gone_out_player(self):
        self._game_data['first_gone_out'] = self._game_data['cur_turn']
        self._game_data['anyone_gone_out'] = True

    # check if the cards of the player matches all runs and blocks
    def run_block_match(self):
        cur_player = self._game_data['cur_turn']
        if cur_player.get_hand().deck_len() == 0:
            return True
        else:
            return False

    # check if current round is ended
    def is_cur_round_ended(self):
        if self._game_data['anyone_gone_out']:
            self._game_data['round_last_loop_id'] = self._game_data['round_last_loop_id'] + 1
        player_count = len(self._game_data['players'])
        if self._game_data['round_last_loop_id'] == player_count:
            return True
        else:
            return False


    # update game data
    def update_data(self, index, value):
        self._game_data[index] = value

    # get game data
    def get_data(self, index):
        return self._game_data[index]

    # clear model
    def clear_data(self):
        self.init_default_game_data()
        self.init_new_round(True)

    # get winner
    def get_winner_data(self):
        players = self._game_data['players']
        sorted_players = sorted(players, key=lambda x: (x.get_player_total_score()), reverse=False)
        min_score = sorted_players[0].get_player_total_score()
        data = []
        for player in sorted_players:
            if player.get_player_total_score() == min_score:
                data.append({"name": player.get_player_name(), "total_score": player.get_player_total_score()})
        return data


    # get filenames of the specified directory
    def get_filenames(self, path):
        filenames = []
        if not os.path.isdir(path):
            return filenames
        for fname in os.listdir(path):
            if fname.endswith(self.saved_game_file_extension):
                filenames.append(fname)
        return filenames

    # get the list of saved game file names
    def saved_game_file_names(self):
        return self.get_filenames(self.saved_game_files_path)

    # load saved game data
    def load_saved_game_data(self, file_name):
        file_path = self.saved_game_files_path + "/" + file_name
        try:
            saved_file = open(file_path, "r")
            lines = saved_file.readlines()
            saved_file.close()
            player_id = 0
            com_count = 0
            human_count = 0
            cards_count = 0
            self._game_data['players'] = []
            line_index = 0
            line_count = len(lines)
            while line_index < line_count:
                line = lines[line_index]
                if line.strip() == "":
                    line_index += 1
                    continue
                elif "Round:" in line:
                    load_round = line.replace("Round:", "").strip()
                    self._game_data['cur_round'] = int(load_round)
                elif ("Computer" in line or "Human" in line) and not "Next Player:" in line:
                    player_type = ""
                    if "Computer" in line:
                        player_type = "computer"
                    elif "Human" in line:
                        player_type = "human"
                    player_name = line.replace(":", "").strip()
                    player_score = ""
                    player_hand = ""
                    player = None
                    while line.strip() != "":
                        line_index += 1
                        line = lines[line_index]
                        if "Score:" in line:
                            player_score = line.replace("Score:", "").strip()
                        elif "Hand:" in line:
                            player_hand = line.replace("Hand:", "").strip()
                    if player_type == "computer":
                        player = Computer(player_id, player_name)
                        com_count += 1
                    elif player_type == "human":
                        player = Human(player_id, player_name)
                        human_count += 1
                    player.load_from_saved_score(int(player_score))
                    cards_count += player.load_from_saved_hand(player_hand, self._game_data['cur_round'])
                    self._game_data['players'].append(player)
                    player_id += 1
                elif "Draw Pile:" in line:
                    draw_pile_str = line.replace("Draw Pile:", "").strip()
                    draw_pile = Pile()
                    cards_count += draw_pile.load_from_saved(draw_pile_str, self._game_data['cur_round'])
                    self._game_data['draw_pile'] = draw_pile
                elif "Discard Pile:" in line:
                    discard_pile_str = line.replace("Discard Pile:", "").strip()
                    discard_pile = Pile()
                    cards_count += discard_pile.load_from_saved(discard_pile_str, self._game_data['cur_round'])
                    self._game_data['discard_pile'] = discard_pile
                elif "Next Player:" in line:
                    next_player_str = line.replace("Next Player:", "").strip()
                    for player in self._game_data['players']:
                        if next_player_str == player.get_player_name():
                            self._game_data['cur_turn'] = player
                            break 

                line_index += 1
            self._game_data['play_state'] = 1
            # self._game_data['first_gone_out'] = self._game_data['cur_turn']
            self._game_data['anyone_gone_out'] = False
            self._game_data['round_last_loop_id'] = 0
            self._game_data['dealt'] = True
            self._game_data['cur_state'] = "discarded"
            self._game_data['player_count'] = {"computer": com_count, "human": human_count}
            self._game_data['deck_count'] = int(cards_count / 58 + 0.5)

            return "success"
        except:
            return "error"

    # save game data
    def save_game(self, file_name):
        file_path = self.saved_game_files_path + "/" + file_name
        if not os.path.isdir(self.saved_game_files_path):
            os.mkdir(self.saved_game_files_path)
        if os.path.isfile(file_path):
            return "duplicate"
        try:
            save_file = open(file_path, "w")
            save_file.write("Round: {}\n\n".format(self._game_data['cur_round']))

            players = self._game_data['players']
            for player in players:
                save_file.write("{}:\n".format(player.get_player_name()))
                save_file.write("   Score: {}\n".format(player.get_player_total_score()))
                hand_str = ""
                for drop_hand in player.get_drop_hands():
                    hand_str += drop_hand.toStringFormat()
                hand_str += player.get_hand().toStringFormat()
                save_file.write("   Hand: {}\n\n".format(hand_str))

            draw_pile_str = self._game_data['draw_pile'].toStringFormat()
            save_file.write("Draw Pile: {}\n\n".format(draw_pile_str))

            discard_pile_str = self._game_data['discard_pile'].toStringFormat()
            save_file.write("Discard Pile: {}\n\n".format(discard_pile_str))

            cur_player_name = self._game_data['cur_turn'].get_player_name()
            save_file.write("Next Player: {}\n\n".format(cur_player_name))

            save_file.close()
            return "success"
        except:
            return "error"
    
    # find books in the hand of the current player
    def get_cur_books(self):
        ranks = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cur_player = self.get_data('cur_turn')
        cur_hand = cur_player.get_hand()
        wild_rank = str(self.get_data('cur_round') + 2).strip()
        wild_cards = []
        joker_cards = []
        books_cards = {}
        for rank in ranks:
            if rank == wild_rank:
                continue
            books_cards[rank] = []

        cur_cards = cur_hand.get_cards()
        for cur_card in cur_cards:
            cur_rank = cur_card.get_rank()
            if cur_rank in ["J1", "J2", "J3"]:
                joker_cards.append(cur_card)
            elif cur_rank == wild_rank:
                wild_cards.append(cur_card)
            else:
                books_cards[cur_rank].append(cur_card)
        final_books = {}
        for book_rank in books_cards:
            if len(books_cards[book_rank]) < 2:
                continue
            elif len(books_cards[book_rank]) == 2:
                if len(joker_cards) > 0:
                    final_books[book_rank] = books_cards[book_rank]
                    final_books[book_rank].append(joker_cards.pop())
                    continue
                if len(wild_cards) > 0:
                    final_books[book_rank] = books_cards[book_rank]
                    final_books[book_rank].append(wild_cards.pop())
            else:
                final_books[book_rank] = books_cards[book_rank]
        return final_books

    # find the runs in the hand of the current player
    def get_cur_runs(self):
        suits = ['diamond', 'heart', 'club', 'spade', 'star']
        ranks = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cur_player = self.get_data('cur_turn')
        cur_hand = cur_player.get_hand()
        wild_rank = str(self.get_data('cur_round') + 2).strip()
        wild_cards = []
        joker_cards = []
        cards_by_suit = {}

        for suit in suits:
            cards_by_suit[suit] = []

        cur_cards = cur_hand.get_cards()
        for cur_card in cur_cards:
            cur_rank = cur_card.get_rank()
            if cur_rank in ["J1", "J2", "J3"]:
                joker_cards.append(cur_card)
            elif cur_rank == wild_rank:
                wild_cards.append(cur_card)
            else:
                cur_suit = cur_card.get_suit()
                cards_by_suit[cur_suit].append(cur_card)

        final_runs = []
        for card_suit in cards_by_suit:
            suit_cards_list = []
            missing_counts_list = []
            tmp_list = []
            for card in cards_by_suit[card_suit]:
                if len(tmp_list) == 0:
                    tmp_list.append(card)
                    continue
                if card.get_value() == tmp_list[-1].get_value() + 1:
                    tmp_list.append(card)
                elif card.get_value() == tmp_list[-1].get_value():
                    continue
                else:
                    suit_cards_list.append(tmp_list)
                    missing_counts_list.append(card.get_value() - tmp_list[-1].get_value() -1)
                    tmp_list = []
                    tmp_list.append(card)
            if tmp_list != []:
                suit_cards_list.append(tmp_list)

            tmp_run = []
            part_index = 0
            done_index_list = []
            for missing_count in missing_counts_list:
                if len(wild_cards) + len(joker_cards) >= missing_count:
                    part_index = missing_counts_list.index(missing_count)
                    tmp_run.extend(suit_cards_list[part_index])
                    done_index_list.append(part_index)
                    for j in range(missing_count):
                        if len(joker_cards) > 0:
                            tmp_run.append(joker_cards.pop())
                        else:
                            tmp_run.append(wild_cards.pop())
                    tmp_run.extend(suit_cards_list[part_index+1])
                    suit_cards_list.pop(part_index)
                    suit_cards_list.pop(part_index)
                    break
                else:    
                    continue
            if tmp_run != []:
                final_runs.append(tmp_run)
            
            for cards_part in suit_cards_list:
                if len(cards_part) > 2:
                    final_runs.append(cards_part)
        return final_runs

    # get runs and books in the hand of the player
    def get_cur_runs_books(self):
        suits = ['diamond', 'heart', 'club', 'spade', 'star']
        ranks = {"3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9", "10":"10", "11":"J", "12":"Q", "13":"K"}
        cur_player = self.get_data('cur_turn')
        cur_hand = cur_player.get_hand()
        wild_rank = str(self.get_data('cur_round') + 2).strip()
        wild_rank = ranks[wild_rank]
        wild_cards = []
        joker_cards = []
        final_books_runs = []
        cur_cards = cur_hand.get_cards()

        for cur_card in cur_cards:
            cur_rank = cur_card.get_rank()
            if cur_rank in ["J1", "J2", "J3"]:
                joker_cards.append(cur_card)
            elif cur_rank == wild_rank:
                wild_cards.append(cur_card)

        ##############  find runs  ##################
        final_runs = []
        while True:
            used_card_ids = []
            final_runs = []
            for book in final_books_runs:
                for book_card in book:
                    used_card_ids.append(cur_cards.index(book_card))

            cards_by_suit = {}
            for suit in suits:
                cards_by_suit[suit] = []

            for cur_card in cur_cards:
                if cur_cards.index(cur_card) in used_card_ids:
                    continue
                cur_rank = cur_card.get_rank()
                if cur_rank in ["J1", "J2", "J3"]:
                    continue
                elif cur_rank == wild_rank:
                    continue
                else:
                    cur_suit = cur_card.get_suit()
                    cards_by_suit[cur_suit].append(cur_card)

            for card_suit in cards_by_suit:
                suit_cards_list = []
                missing_counts_list = []
                tmp_list = []
                for card in cards_by_suit[card_suit]:
                    if len(tmp_list) == 0:
                        tmp_list.append(card)
                        continue
                    if card.get_value() == tmp_list[-1].get_value() + 1:
                        tmp_list.append(card)
                    elif card.get_value() == tmp_list[-1].get_value():
                        continue
                    else:
                        suit_cards_list.append(tmp_list)
                        missing_counts_list.append(card.get_value() - tmp_list[-1].get_value() -1)
                        tmp_list = []
                        tmp_list.append(card)
                if tmp_list != []:
                    suit_cards_list.append(tmp_list)

                tmp_run = []
                part_index = 0
                done_index_list = []
                for missing_count in missing_counts_list:
                    if len(wild_cards) + len(joker_cards) >= missing_count:
                        part_index = missing_counts_list.index(missing_count)
                        tmp_run.extend(suit_cards_list[part_index])
                        done_index_list.append(part_index)
                        for j in range(missing_count):
                            if len(joker_cards) > 0:
                                tmp_run.append(joker_cards.pop())
                            else:
                                tmp_run.append(wild_cards.pop())
                        tmp_run.extend(suit_cards_list[part_index+1])
                        suit_cards_list.pop(part_index)
                        suit_cards_list.pop(part_index)
                        break
                    else:    
                        continue
                if tmp_run != []:
                    final_runs.append(tmp_run)
                
                for cards_part in suit_cards_list:
                    if len(cards_part) > 2:
                        final_runs.append(cards_part)
                    elif len(cards_part) == 2 and (len(joker_cards) + len(wild_cards)) > 0:
                        tmp_list = []
                        tmp_list.extend(cards_part)
                        if len(joker_cards) > 0:
                            tmp_list.append(joker_cards.pop())
                        elif len(wild_cards) > 0:
                            tmp_list.append(wild_cards.pop())
                        final_runs.append(tmp_list)
            if len(final_runs) == 0:
                break
            else:
                final_books_runs.extend(final_runs)
        ########################################################
        

        #############  find books  ##################
        final_books = []
        books_cards = {}

        for book in final_books_runs:
            for book_card in book:
                used_card_ids.append(cur_cards.index(book_card))

        for rank in ranks:
            if ranks[rank] == wild_rank:
                continue
            books_cards[ranks[rank]] = []

        for cur_card in cur_cards:
            if cur_cards.index(cur_card) in used_card_ids:
                continue
            cur_rank = cur_card.get_rank()
            if cur_rank in ["J1", "J2", "J3"]:
                continue
            elif cur_rank == wild_rank:
                continue
            else:
                books_cards[cur_rank].append(cur_card)
        
        for book_rank in books_cards:
            if len(books_cards[book_rank]) < 2:
                continue
            elif len(books_cards[book_rank]) == 2:
                tmp_book = []
                if len(joker_cards) > 0:
                    tmp_book = books_cards[book_rank]
                    tmp_book.append(joker_cards.pop())
                    final_books.append(tmp_book)
                    continue
                if len(wild_cards) > 0:
                    tmp_book = books_cards[book_rank]
                    tmp_book.append(wild_cards.pop())
                    final_books.append(tmp_book)
                    continue
            else:
                final_books.append(books_cards[book_rank])
        final_books_runs.extend(final_books)
        ############################################

        used_card_ids = []
        for book_run in final_books_runs:
            for book_run_card in book_run:
                used_card_ids.append(cur_cards.index(book_run_card))

        unused_cards=[]
        for cur_card in cur_cards:
            if cur_cards.index(cur_card) in used_card_ids:
                continue
            if cur_card.is_joker() or cur_card.is_wild():
                continue
            unused_cards.append(cur_card)
        if len(unused_cards) == 1:
            if len(joker_cards) > 0:
                for joker_card in joker_cards:
                    final_books_runs[-1].append(joker_card)
            if len(wild_cards) > 0:
                for wild_card in wild_cards:
                    final_books_runs[-1].append(wild_card)
        elif len(unused_cards) == 2:
            if len(joker_cards) + len(wild_cards) > 1:
                tmp_list = []
                tmp_list.append(unused_cards.pop())
                for joker_card in joker_cards:
                    tmp_list.append(joker_card)
                for wild_card in wild_cards:
                    tmp_list.append(wild_card)
                final_books_runs.append(tmp_list)
        if len(used_card_ids) == len(cur_cards):
            final_books_runs.pop()
                
        return final_books_runs





                
        
            


