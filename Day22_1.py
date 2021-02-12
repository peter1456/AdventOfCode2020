from utils import read_blank_line_separated_input
from queue import SimpleQueue

class Combat:
    def __init__(self, player1_hand, player2_hand):
        self.player_1_deck = SimpleQueue()
        self.player_2_deck = SimpleQueue()
        self.insert_deck(self.player_1_deck, *player1_hand)
        self.insert_deck(self.player_2_deck, *player2_hand)

    @staticmethod
    def insert_deck(deck, *cards):
        for card in cards:
            deck.put(card)

    @staticmethod
    def compute_deck_score(deck):
        cards = []
        while not deck.empty():
            cards.append(deck.get())
        return sum(card * (multiplier + 1) for card, multiplier in zip(cards, reversed(range(len(cards)))))

    def winner(self):
        if self.player_1_deck.empty() or self.player_2_deck.empty():
            return "player_1" if self.player_2_deck.empty() else "player_2"
        return None
    
    def print_winner_score(self):
        print(self.compute_deck_score(self.player_1_deck) if self.winner() == "player_1" else self.compute_deck_score(self.player_2_deck))

    def play_one_round(self):
        player_1_card = self.player_1_deck.get()
        player_2_card = self.player_2_deck.get()
        if player_1_card > player_2_card:
            self.insert_deck(self.player_1_deck, player_1_card, player_2_card)
        else:
            self.insert_deck(self.player_2_deck, player_2_card, player_1_card)

    def play_one_game(self):
        while self.winner() is None:
            self.play_one_round()
        self.print_winner_score()

player_1_input, player_2_input = read_blank_line_separated_input(22)
player_1_hand = [int(card) for card in player_1_input.split("\n")[1:]]
player_2_hand = [int(card) for card in player_2_input.split("\n")[1:]]

combat_game = Combat(player_1_hand, player_2_hand)
combat_game.play_one_game()