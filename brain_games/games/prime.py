from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    deviders = 0
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            deviders += 1
            break
    if deviders == 0:
        return 'yes'
    else:
        return 'no'


def question_and_correct_answer():
    rand_num = randint(2, 20)
    return str(rand_num), is_prime(rand_num)
