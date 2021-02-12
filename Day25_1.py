from utils import read_split_line_input
from sympy.ntheory.residue_ntheory import discrete_log

public_keys = read_split_line_input(25, convert_to=int)
subject_no = 7
mod = 20201227

loop_sizes = [discrete_log(mod, public_key, subject_no) for public_key in public_keys]

subject = subject_no
for loop_size in loop_sizes:
    subject = pow(subject, loop_size, 20201227)

print(subject)