import prompt


NUMBER_OF_ROUNDS = 3


def launch(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_RULE)
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
    else:
        print(f'Congratulations, {user_name}!')
