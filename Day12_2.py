from utils import read_split_line_input

class Ship:
    direction_to_coor: dict = {
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
        "N": (0, 1)
    }

    rotate_function = [
        lambda x: x,
        lambda x: [x[1], -x[0]],
        lambda x: [-x[0], -x[1]],
        lambda x: [-x[1], x[0]]
    ]

    def __init__(self):
        self.waypoint_offset = [10, 1]
        self.ship_pos = [0, 0]
    
    def _move_waypoint(self, direction, value):
        self.waypoint_offset[0] += self.direction_to_coor[direction][0] * value
        self.waypoint_offset[1] += self.direction_to_coor[direction][1] * value

    def _rotate_waypoint(self, direction, value):
        rotate_idx = int(value / 90 * (1 if direction == "R" else -1))
        self.waypoint_offset = self.rotate_function[rotate_idx](self.waypoint_offset)

    def _move_ship(self, times):
        self.ship_pos[0] += self.waypoint_offset[0] * times
        self.ship_pos[1] += self.waypoint_offset[1] * times

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

print(abs(ship.ship_pos[0]) + abs(ship.ship_pos[1]))