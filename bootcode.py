class BootCodeInterpreter:
    def __init__(self, code):
        self.code = self.parse_code(code)
        self.ptr = 0
        self.acc = 0
        self.terminated = False

    @staticmethod
    def parse_code(code):
        instructions = code.split('\n')
        instructions = [[ins.split(' ')[0], int(ins.split(' ')[1])] for ins in instructions]
        return instructions
    
    def run_one_ins(self):
        if self.ptr == len(self.code):
            return False
        ins = self.code[self.ptr]
        if ins[0] == "acc":
            self.acc += ins[1]
            self.ptr += 1
        elif ins[0] == "jmp":
            self.ptr += ins[1]
        elif ins[0] == "nop":
            self.ptr += 1
        return True

    def run_until_loop_or_terminate(self):
        ins_ran = set()
        while (self.ptr not in ins_ran):
            ins_ran.add(self.ptr)
            if not self.run_one_ins():
                self.terminated = True
                return self.acc
        return self.acc