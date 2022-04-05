from random import randint, randrange


def game_rules():
    return 'What number is missing in the progression?'


def question_and_correct_answer():
    start = randint(1, 50)
    random_step = randint(1, 10)
    i = 0
    progression = [start]
    for i in range(9):
        a = start + random_step
        progression.append(a)
        start = a
    # random_choice = choice(progression)
    # hidden_choice = progression.index(random_choice)
    # progression[hidden_choice] = '..'
    random_index = randrange(len(progression))
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = ''
    for n in range(len(progression)):
        value_progression = progression[n]
        question = question + str(value_progression) + ' '
    return question.strip(), str(correct_answer)
