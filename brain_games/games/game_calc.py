from operator import mul, add, sub
from random import randint, choice


def correct_answer():
    rand_num1 = randint(1, 100)
    rand_num2 = randint(1, 100)
    operators = (('*', mul),('+', add),('-', sub))
    random_oper = choice(operators)
    task = '{0} {1} {2}'.format(rand_num1, random_oper[0], rand_num2)
    correct_answ = random_oper[1](rand_num1,rand_num2)
    return str(task), str(correct_answ)

