from utils import read_split_line_input
from functools import lru_cache

adapters = read_split_line_input(10, int)
adapters.sort()

WALL_ADAPTER = 0
BUILTIN_ADAPTER = adapters[-1] + 3

@lru_cache
def count_arrangements(start):
    if start + 3 == BUILTIN_ADAPTER:
        return 1
    adapters_range = lambda x: start < x <= start + 3
    adapters_in_range = filter(adapters_range, adapters)
    return sum(count_arrangements(start) for start in adapters_in_range)

print(count_arrangements(0))