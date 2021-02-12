from utils import read_split_line_input
from queue import LifoQueue

homework = read_split_line_input(18, list)
homework = [[token for token in expression if token != " "] for expression in homework]


def evaluate_single(expression):
    if expression[1] == "+":
        return str(int(expression[0]) + int(expression[2]))
    else:
        return str(int(expression[0]) * int(expression[2]))

def evaluate_expression_one_operator(expression):
    if "+" in expression:
        operator_index = expression.index("+")
    else:
        operator_index = expression.index("*")
    result = evaluate_single(expression[operator_index - 1:operator_index + 2])
    expression[operator_index - 1] = result
    expression[operator_index: operator_index + 2] = ["#"] * 2
    return expression

def eliminate_placeholder(expression):
    return [token for token in expression if token != "#"]

def evaluate_expression_no_brackets(expression):
    expression = eliminate_placeholder(expression)
    while len(expression) > 1:
        expression = evaluate_expression_one_operator(expression)
        expression = eliminate_placeholder(expression)
    return expression[0]

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