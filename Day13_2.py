from utils import read_raw_input
import numpy as np

def inverse_mod(col):
    return pow(int(col[0]), -1, int(col[1]))

raw_input = read_raw_input(13)

contest_schedule = raw_input.split('\n')[1].split(',')
bus_ids = np.array([(bus_id[0], int(bus_id[1])) for bus_id in enumerate(contest_schedule) if bus_id[1] != "x"], dtype=np.int64)

a = (bus_ids[:,1] - bus_ids[:,0]) % bus_ids[:,1]
y = (np.product(bus_ids[:,1]) / bus_ids[:,1]).astype(np.int64)
z = np.apply_along_axis(inverse_mod, 0, np.vstack((y, bus_ids[:,1])))

print(np.sum(a * y * z) % np.product(bus_ids[:,1]))