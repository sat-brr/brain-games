import prompt


NUMBER_OF_ROUNDS = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_launch(game):
    user_name = welcome_user()
    print(game.game_rules())
    correct_answer_counter = 0
    while correct_answer_counter < NUMBER_OF_ROUNDS:
        question, correct_answer = game.question_and_correct_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('')
        print(f'Your answer: {user_answer}')
        if user_answer == correct_answer:
            correct_answer_counter += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"'Correct answer was '{correct_answer}.'\n"
                  f"Let's try again, {user_name}!")
            break
    if correct_answer_counter == NUMBER_OF_ROUNDS:
        print(f'Congratulations, {user_name}!')
