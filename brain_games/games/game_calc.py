from operator import mul, add, sub
from random import randint, choice


def game_rules():
    print('What is the result of the expression?')


def quest_and_correct_answer():
    rand_num1 = randint(1, 10)
    rand_num2 = randint(1, 10)
    operators = (('*', mul), ('+', add), ('-', sub))
    random_oper = choice(operators)
    quest = f'{rand_num1} {random_oper[0]} {rand_num2}'
    correct_answ = random_oper[1](rand_num1, rand_num2)
    return str(quest), str(correct_answ)
