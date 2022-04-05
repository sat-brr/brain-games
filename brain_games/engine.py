import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_logic(game):
    user_name = welcome_user()
    print(game.game_rules())
    count = 0  # Счетчик правильных ответов
    TOTAL = 3  # Требуемое количество правильных ответов для победы в игре
    while count < TOTAL:
        quest, answer = game.question_and_correct_answer()
        print(f'Question: {quest}')
        answer_player = prompt.string('')
        print(f'Your answer: {answer_player}')
        if answer_player == answer:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer_player}' is wrong answer ;(."
                  f"'Correct answer was '{answer}.'\n"
                  f"Let's try again, {user_name}!")
            break
    if count == TOTAL:
        print(f'Congratulations, {user_name}!')
