from random import randint


def current_answer():
    rand_num = randint(1, 100)
    correct_answ = ''
    if rand_num % 2 == 0:
        correct_answ += 'yes'
    else:
        correct_answ += 'no'
    return str(rand_num), str(correct_answ)