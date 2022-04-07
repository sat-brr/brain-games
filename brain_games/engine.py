import prompt


CORRECT_ANSWERS_FOR_WIN = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_logic(game):
    user_name = welcome_user()
    print(game.game_rules())
    correct_answer_counter = 0
    while correct_answer_counter < CORRECT_ANSWERS_FOR_WIN:
        question, answer = game.question_and_correct_answer()
        print(f'Question: {question}')
        answer_player = prompt.string('')
        print(f'Your answer: {answer_player}')
        if answer_player == answer:
            correct_answer_counter += 1
            print('Correct!')
        else:
            print(f"'{answer_player}' is wrong answer ;(."
                  f"'Correct answer was '{answer}.'\n"
                  f"Let's try again, {user_name}!")
            break
    if correct_answer_counter == CORRECT_ANSWERS_FOR_WIN:
        print(f'Congratulations, {user_name}!')
