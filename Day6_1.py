from typing import List
from utils import read_blank_line_separated_input

replies = read_blank_line_separated_input(6, list)

def get_distinct_replies(reply: List[str]):
    print(reply)
    reply_set = set(reply)
    if '\n' in reply_set:
        reply_set.remove('\n')
    return reply_set

print(sum(len(get_distinct_replies(reply)) for reply in replies))
