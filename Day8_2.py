from utils import read_raw_input
from bootcode import BootCodeInterpreter

code = read_raw_input(8)

def is_faulty_ins(line_num):
    interpreter = BootCodeInterpreter(code)
    target_ins = interpreter.code[line_num]
    if target_ins[0] == "acc":
        return False
    elif target_ins[0] == "nop":
        interpreter.code[line_num][0] = "jmp"
    else:
        interpreter.code[line_num][0] = "nop"
    acc_val = interpreter.run_until_loop_or_terminate()
    if interpreter.terminated:
        return acc_val
    else:
        return False

for i in range(len(BootCodeInterpreter.parse_code(code))):
    if acc := is_faulty_ins(i):
        print(acc)
        break
