from utils import read_raw_input

class CupGame:
    def __init__(self, cup_order):
        self.cups = [None] * len(cup_order)
        for i in range(len(cup_order)):
            self.cups[int(cup_order[i]) - 1] = int(cup_order[(i + 1) % len(cup_order)]) - 1
        self.current = int(cup_order[0]) - 1
    
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
        available_cups = [cup for cup in range(len(self.cups)) if cup not in three_cups]
        return max(available_cups) if self.current == min(available_cups) else max(cup for cup in available_cups if cup < self.current)

    def insert_three_cups(self, destination_cup, three_cups):
        self.cups[three_cups[-1]] = self.cups[destination_cup]
        self.cups[destination_cup] = three_cups[0]

    def play_one_move(self):
        three_cups = self.take_three_cups()
        destination_cup = self.destination_cup(three_cups)
        self.insert_three_cups(destination_cup, three_cups)
        self.current = self.cups[self.current]

    def print_labelling(self, start):
        pos = self.cups[start - 1]
        for _ in range(len(self.cups) - 1):
            print(pos + 1, end="")
            pos = self.cups[pos]
        print("")

raw_input = read_raw_input(23)

cupgame = CupGame(raw_input)

for _ in range(100):
    cupgame.play_one_move()

cupgame.print_labelling(1)