from math import gcd
from random import randint


def game_rules():
    print('Find the greatest common divisor of given numbers.')


def quest_and_correct_answer():
    rand_num1 = randint(1, 10)
    rand_num2 = randint(1, 10)
    correct_answ = gcd(rand_num1, rand_num2)
    quest = f'{rand_num1} {rand_num2}'
    return str(quest), str(correct_answ)
