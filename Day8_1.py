from utils import read_raw_input
from bootcode import BootCodeInterpreter

code = read_raw_input(8)
interpreter = BootCodeInterpreter(code)

ins_visited = set()

while interpreter.ptr not in ins_visited:
    ins_visited.add(interpreter.ptr)
    interpreter.run_one_ins()

print(interpreter.acc)