from utils import read_blank_line_separated_input
from functools import reduce

replies = read_blank_line_separated_input(6)

def get_common_answer(group_reply: str):
    replies_by_person = [set(reply) for reply in group_reply.split('\n')]
    common_answer = reduce(lambda x, y: x & y, replies_by_person)
    return common_answer

print(sum(len(get_common_answer(group_reply)) for group_reply in replies))