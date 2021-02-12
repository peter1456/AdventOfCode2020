from utils import read_blank_line_separated_input
from functools import lru_cache
import re

# Use of Regex

rules, strings = read_blank_line_separated_input(19)
strings = strings.split("\n")
rules = {int(rule.split(": ")[0]): rule.split(": ")[1] for rule in rules.split("\n")}

# As Input string has finite length, rule loops for at most 5 times
EXPAND = 5

rules[8] = " | ".join(" ".join(["42"] * (i + 1)) for i in range(EXPAND))
rules[11] = " | ".join(" ".join(["42"] * (i + 1) + ["31"] * (i + 1)) for i in range(EXPAND))

@lru_cache
def get_rule_regex(rule_no):
    rule = rules[rule_no]
    if rule.startswith('"'):
        return rule[1]
    evaluated_rule = [get_rule_regex(int(part)) if part.isnumeric() else part for part in rule.split(" ")]
    return f"({''.join(evaluated_rule)})"

rule_0_regex = re.compile(f"^{get_rule_regex(0)}$")
print(len(list(filter(lambda x: rule_0_regex.match(x), strings))))
