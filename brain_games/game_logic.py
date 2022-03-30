from random import randint
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def current_answer():
    rand_num = randint(1, 100)
    correct_answ = ''
    if rand_num % 2 == 0:
        correct_answ += 'yes'
    else:
        correct_answ += 'no'
    return str(rand_num), str(correct_answ)


def logic():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        quest, answer = current_answer()
        print(f'Question :{quest}')
        answer_player = prompt.string()
        print(f'Your answer: {answer_player}')
        if answer_player == answer:
            count += 1
            print('Correct')
        else:
            print(f"'{answer_player}' is wrong answer ;(."
                f"'Correct answer was '{answer}'\n"
                f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
