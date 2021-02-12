from utils import read_blank_line_separated_input

class Deck:
    def __init__(self, hand):
        self.deck = []
        self.size = 0
        self.insert_to_deck(*hand)

    def insert_to_deck(self, *cards):
        for card in cards:
            self.deck.append(card)
            self.size += 1
    
    def deal(self):
        self.size -= 1
        return self.deck.pop(0)
    
    def copy(self, size):
        return Deck(self.deck[:size])    

    def score(self):
        return sum(card * (multiplier + 1) for card, multiplier in zip(self.deck, reversed(range(self.size))))

class Combat:
    def __init__(self, player1_hand, player2_hand):
        self.players = [Deck(player1_hand), Deck(player2_hand)]
        self.encoutered_state_hashes = []

    def state_hash(self):
        return hash((tuple(self.players[0].deck), tuple(self.players[1].deck)))

    def copy(self, *cards):
        new_game = Combat([], [])
        for i in (0, 1):
            new_game.players[i] = self.players[i].copy(cards[i])
        return new_game

    def winner(self):
        if self.state_hash() in self.encoutered_state_hashes:
            return 0
        if any(self.players[i].size == 0 for i in (0, 1)):
            return 0 if self.players[1].size == 0 else 1
        return None

    def play_one_round(self):
        self.encoutered_state_hashes.append(self.state_hash())
        cards = [self.players[i].deal() for i in (0, 1)]
        if all(self.players[i].size >= cards[i] for i in (0, 1)):
            winner = self.copy(*cards).play_one_game()
        else:
            winner = 0 if cards[0] > cards[1] else 1
        winner_card = cards.pop(winner)
        loser_card = cards[0]
        self.players[winner].insert_to_deck(winner_card, loser_card)

    def play_one_game(self):
        while (winner:= self.winner()) is None:
            self.play_one_round()
        return winner

player_1_input, player_2_input = read_blank_line_separated_input(22)
player_1_hand = [int(card) for card in player_1_input.split("\n")[1:]]
player_2_hand = [int(card) for card in player_2_input.split("\n")[1:]]

combat_game = Combat(player_1_hand, player_2_hand)
winner = combat_game.play_one_game()
print(combat_game.players[winner].score())