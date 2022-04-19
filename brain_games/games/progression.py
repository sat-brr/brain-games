from random import randint, randrange


PROGRESSION_SIZE = 10
GAME_RULE = 'What number is missing in the progression?'


def question_and_correct_answer():
    start = randint(1, 50)
    random_step = randint(1, 10)
    progression = [start]
    for _ in range(1, PROGRESSION_SIZE):
        num = start + random_step
        progression.append(num)
        start = num
    random_index = randrange(len(progression))
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = ''
    for n in range(len(progression)):
        value_progression = progression[n]
        question = question + str(value_progression) + ' '
    return question.strip(), str(correct_answer)
