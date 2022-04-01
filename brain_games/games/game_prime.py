from random import randint


def game_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def quest_and_correct_answer():
    rand_num = randint(2, 20)
    counter = 0
    correct_answer = ''
    for i in range(2, (rand_num // 2) + 1):
        if rand_num % i == 0:
            counter += 1
            break
    if counter == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(rand_num), str(correct_answer)
