from math import gcd
from random import randint


def game_rules():
    return 'Find the greatest common divisor of given numbers.'


def question_and_correct_answer():
    rand_num1 = randint(1, 10)
    rand_num2 = randint(1, 10)
    correct_answer = gcd(rand_num1, rand_num2)
    question = f'{rand_num1} {rand_num2}'
    return str(question), str(correct_answer)
