from utils import read_split_line_input
from queue import LifoQueue

homework = read_split_line_input(18, list)
homework = [[token for token in expression if token != " "] for expression in homework]


def evaluate_single(expression):
    if expression[1] == "+":
        return [str(int(expression[0]) + int(expression[2]))]
    else:
        return [str(int(expression[0]) * int(expression[2]))]

def evaluate_expression_no_brackets(expression):
    expression_no_placeholder = [token for token in expression if token != "#"]
    while len(expression_no_placeholder) > 1:
        expression_no_placeholder = evaluate_single(expression_no_placeholder[:3]) + expression_no_placeholder[3:]
    return expression_no_placeholder[0]

def evaluate_expression(expression):
    bracket_stack = LifoQueue(maxsize=10)
    if "(" not in expression:
        return evaluate_expression_no_brackets(expression)
    for idx, token in enumerate(expression):
        token = expression[idx]
        if token == "(":
            bracket_stack.put(idx)
        elif token == ")":
            expr_start = bracket_stack.get() + 1
            eval_result = evaluate_expression_no_brackets(expression[expr_start:idx])
            expression[expr_start - 1] = str(eval_result)
            expression[expr_start:idx + 1] = ["#"] * (idx - expr_start + 1)
    return evaluate_expression_no_brackets(expression)

print(sum(int(evaluate_expression(expression)) for expression in homework))