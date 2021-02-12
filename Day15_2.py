from utils import read_raw_input

starting_numbers = [int(num) for num in read_raw_input(15).split(',')]

num_records = {num: idx + 1 for idx, num in enumerate(starting_numbers[:-1])}
last_number_spoken = starting_numbers[-1]

for i in range(len(starting_numbers) + 1, 30000001):
    if last_number_spoken not in num_records:
        to_speak = 0
    else:
        to_speak = i - 1 - num_records[last_number_spoken]
    num_records[last_number_spoken] = i - 1
    last_number_spoken = to_speak

print(last_number_spoken)