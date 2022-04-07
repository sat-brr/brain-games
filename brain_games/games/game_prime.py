from random import randint


def game_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    deviders = 0
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            deviders += 1
            break
    return deviders


def question_and_correct_answer():
    rand_num = randint(2, 20)
    deviders = is_prime(rand_num)
    correct_answer = ''
    if deviders == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(rand_num), str(correct_answer)
