from random import randint, choice


def game_rules():
    print('What number is missing in the progression?')


def quest_and_correct_answer():
    start = randint(1, 50)
    random_step = randint(1, 10)
    i = 0
    progression = [start]
    for i in range(9):
        a = start + random_step
        progression += [a]
        start = a
    rand_choice = choice(progression)
    hidden_choice = progression.index(rand_choice)
    progression[hidden_choice] = '..'
    quest = ''
    for n in range(len(progression)):
        b = progression[n]
        quest = quest + str(b) + ' '
    return quest.strip(), str(rand_choice)
