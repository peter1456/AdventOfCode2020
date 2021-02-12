from utils import read_split_line_input

class Ship:
    direction_to_coor: dict = {
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
        "N": (0, 1)
    }

    direction_order = ("N", "E", "S", "W")

    rotate_function = {
        -180: lambda x: [-x[0], -x[1]],
        180: lambda x: [-x[0], -x[1]],
        90: lambda x: [x[1], -x[0]],
        -90: lambda x: [-x[1], x[0]]
    }

    def __init__(self):
        self.waypoint_pos = [10, 1]
        self.ship_pos = [0, 0]
    
    def _move_waypoint(self, direction, value):
        self.waypoint_pos[0] += self.direction_to_coor[direction][0] * value
        self.waypoint_pos[1] += self.direction_to_coor[direction][1] * value

    def _rotate_waypoint(self, direction, value):
        angle = value * (1 if direction == "R" else -1)
        self.waypoint_pos = self.rotate_function[angle](self.waypoint_pos)

    def _move_ship(self, times):
        waypoint_offset = (self.waypoint_pos[0] - self.ship_pos[0], self.waypoint_pos[1] - self.ship_pos[1])
        for i in range(2):
            self.ship_pos[i] += waypoint_offset[i] * times
            self.waypoint_pos += waypoint_offset * (times + 1) 

    def handle_instruction(self, instruction):
        action, value = instruction[0], int(instruction[1:])
        if action in "LR":
            self._rotate_waypoint(action, value)
        elif action == "F":
            self._move_ship(value)
        else:
            self._move_waypoint(action, value)

instructions = read_split_line_input(12)
ship = Ship()

for instruction in instructions:
    ship.handle_instruction(instruction)

print(abs(ship.pos[0]) + abs(ship.pos[1]))