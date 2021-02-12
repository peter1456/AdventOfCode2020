def read_raw_input(day: int):
    with open(f"Day{day}.in", "r") as f:
        return f.read()[:-1]

def read_split_line_input(day: int, convert_to: type=None):
    """Read a file and split the lines, possibly converting the type"""
    with open(f"Day{day}.in", "r") as f:
        lines = f.read().split('\n')[:-1]
    if convert_to is not None:
        return [convert_to(line) for line in lines]
    return lines

def read_grid_input(day: int):
    with open(f"Day{day}.in", "r") as f:
        lines = f.read().split('\n')[:-1]
    return [list(line) for line in lines]

def read_blank_line_separated_input(day: int, convert_to: type=None):
    """Read a file and split by blank lines, possibly converting the type"""
    with open(f"Day{day}.in", "r") as f:
        chunks = (f.read()[:-1]).split('\n\n')
    if convert_to is not None:
        return [convert_to(chunk) for chunk in chunks]
    return chunks