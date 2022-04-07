from operator import mul, add, sub
from random import randint, choice


def game_rules():
    return 'What is the result of the expression?'


def question_and_correct_answer():
    rand_num1 = randint(1, 10)
    rand_num2 = randint(1, 10)
    operators_and_func = (('*', mul), ('+', add), ('-', sub))
    operator, func = choice(operators_and_func)
    question = f'{rand_num1} {operator} {rand_num2}'
    correct_answer = func(rand_num1, rand_num2)
    return str(question), str(correct_answer)
