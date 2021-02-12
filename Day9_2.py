from utils import read_split_line_input

xmas_data = read_split_line_input(9, int)

TARGET = 507622668

low_idx = 0
high_idx = 1

while high_idx < len(xmas_data):
    con_arr = xmas_data[low_idx:high_idx + 1]
    con_sum = sum(con_arr)
    if con_sum > TARGET:
        low_idx += 1
    elif con_sum < TARGET:
        high_idx += 1
    else:
        print(max(con_arr) + min(con_arr))
        break