from os import read
from utils import read_split_line_input

inputs = read_split_line_input(1, int)
inputs.sort()

low = 0
high = len(inputs) - 1

while(inputs[low] + inputs[high] != 2020):
    if inputs[low] + inputs[high] > 2020:
        high -= 1
    else:
        low += 1

print(inputs[low] * inputs[high])