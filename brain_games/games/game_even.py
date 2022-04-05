from random import randint


def game_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def question_and_correct_answer():
    rand_num = randint(1, 100)
    correct_answer = ''
    if rand_num % 2 == 0:
        correct_answer += 'yes'
    else:
        correct_answer += 'no'
    return str(rand_num), str(correct_answer)
