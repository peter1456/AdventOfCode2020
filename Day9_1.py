from utils import read_split_line_input

xmas_data = read_split_line_input(9, int)

def has_two_sum(num_list, target):
    num_list.sort()
    low = 0
    high = len(num_list) - 1

    while (low != high and num_list[low] + num_list[high] != target):
        if num_list[low] + num_list[high] > target:
            high -= 1
        else:
            low += 1
    
    if low == high:
        return False
    return True

for i in range(25, len(xmas_data)):
    preamble = xmas_data[i-25:i]
    if not has_two_sum(preamble, xmas_data[i]):
        print(xmas_data[i])
        break