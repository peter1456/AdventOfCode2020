from utils import read_raw_input
import numpy as np

raw_input = read_raw_input(13)

timestamp = int(raw_input.split('\n')[0])

bus_ids = np.array([int(bus_id) for bus_id in raw_input.split('\n')[1].split(',') if bus_id != "x"])
waiting_time = bus_ids - (timestamp % bus_ids)

print(waiting_time.min() * bus_ids[np.argmin(waiting_time)])