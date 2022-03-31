#from operator import mul, add, sub
#from random import randint, choice
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


#def current_answer(game):
    if game == 'even':
        rand_num = randint(1, 100)
        correct_answ = ''
        if rand_num % 2 == 0:
            correct_answ += 'yes'
        else:
            correct_answ += 'no'
        return str(rand_num), str(correct_answ)
    elif game == 'calc':
        rand_num1 = randint(1, 100)
        rand_num2 = randint(1, 100)
        operators = (('*', mul),('+', add),('-', sub))
        random_oper = choice(operators)
        task = '{0} {1} {2}'.format(rand_num1, random_oper[0], rand_num2)
        correct_answ = random_oper[1](rand_num1,rand_num2)
        return str(task), str(correct_answ)
        

def game_rules(game):
    if game == 'game_even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game == 'game_calc':
        print('What is the result of the expression?')

def logic(game_name):
    name = welcome_user()
    game_rules(str(game_name))
    count = 0
    while count < 3:
        quest, answer = game_name.correct_answer()
        print(f'Question: {quest}')
        answer_player = prompt.string('')
        print(f'Your answer: {answer_player}')
        if answer_player == answer:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer_player}' is wrong answer ;(."
                  f"'Correct answer was '{answer}.'\n"
                  f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')