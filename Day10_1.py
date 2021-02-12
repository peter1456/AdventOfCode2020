from utils import read_split_line_input
from collections import Counter

adapters = read_split_line_input(10, int)
adapters.append(0)
adapters.sort()
adapters.append(adapters[-1] + 3)

jolt_diff = []

for i in range(len(adapters) - 1):
    jolt_diff.append(adapters[i + 1] - adapters[i])

jolt_diff_counter = Counter(jolt_diff)
print(jolt_diff_counter[1] * jolt_diff_counter[3])