import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def logic(game_name):
    name = welcome_user()
    game_name.game_rules()
    count = 0
    while count < 3:
        quest, answer = game_name.quest_and_correct_answer()
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
