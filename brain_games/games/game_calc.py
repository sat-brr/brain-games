from operator import mul, add, sub
from random import randint, choice


def game_rules():
    return 'What is the result of the expression?'


def question_and_correct_answer():
    rand_num1 = randint(1, 10)
    rand_num2 = randint(1, 10)
    operators = (('*', mul), ('+', add), ('-', sub))
    random_operator = choice(operators)
    question = f'{rand_num1} {random_operator[0]} {rand_num2}'
    correct_answer = random_operator[1](rand_num1, rand_num2)
    return str(question), str(correct_answer)
