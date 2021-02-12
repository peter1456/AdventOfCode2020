from utils import read_raw_input

class CupGame:
    def __init__(self, cup_order):
        self.cups = [None] * len(cup_order)
        for i in range(len(cup_order)):
            self.cups[cup_order[i]] = cup_order[(i + 1) % len(cup_order)]
        self.current = cup_order[0]
    
    def take_three_cups(self):
        pos = self.current
        three_cups = []
        for _ in range(3):
            next_cup = self.cups[pos]
            three_cups.append(next_cup)
            pos = next_cup
        self.cups[self.current] = self.cups[pos]
        self.cups[pos] = None
        return three_cups

    def destination_cup(self, three_cups):
        dest_cup = self.current - 1
        while (dest_cup in three_cups) or (dest_cup < 0):
            dest_cup = dest_cup - 1 if dest_cup in three_cups else 10**6 - 1
        return dest_cup

    def insert_three_cups(self, destination_cup, three_cups):
        self.cups[three_cups[-1]] = self.cups[destination_cup]
        self.cups[destination_cup] = three_cups[0]

    def play_one_move(self):
        three_cups = self.take_three_cups()
        destination_cup = self.destination_cup(three_cups)
        self.insert_three_cups(destination_cup, three_cups)
        self.current = self.cups[self.current]

raw_input = read_raw_input(23)
cup_order = [int(cup) - 1 for cup in raw_input] + list(range(9, 10**6))

cupgame = CupGame(cup_order)

for _ in range(10**7):
    cupgame.play_one_move()

sol = 1
pos = 0
for i in range(2):
    next_cup = cupgame.cups[pos]
    sol *= (next_cup + 1)
    pos = next_cup
print(sol)
