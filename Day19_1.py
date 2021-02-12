from utils import read_blank_line_separated_input
from functools import lru_cache
from itertools import product

rules, strings = read_blank_line_separated_input(19)
strings = strings.split("\n")
rules = {int(rule.split(": ")[0]): rule.split(": ")[1] for rule in rules.split("\n")}

def concat_rule(rule):
    first_rule, second_rule = rule.split(" ")
    return {string[0] + string[1] for string in product(get_rule_strings(int(first_rule)), get_rule_strings(int(second_rule)))}

def evaluate_subrule(rule):
    if " " in rule:
        return concat_rule(rule)
    return get_rule_strings(int(rule))

@lru_cache
def get_rule_strings(rule_no):
    rule = rules[rule_no]
    print(rule)
    if rule.startswith('"'):
        return {rule[1]}
    elif "|" in rule:
        first_part, second_part = rule.split(" | ")
        return evaluate_subrule(first_part) | evaluate_subrule(second_part)
    return evaluate_subrule(rule)

print(get_rule_strings(8))

rule_0_strings = get_rule_strings(0)

print(len(list(filter(lambda x: x in rule_0_strings, strings))))
        