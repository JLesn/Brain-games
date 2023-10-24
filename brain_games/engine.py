import prompt

ROUNDS = 3


def run_game(game_name):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print(f'Hello, {name}!')
    print(game_name.MESSAGE)
    count_rounds = 1
    while count_rounds <= ROUNDS:
        qw, answ = game_name.qw_and_answ()
        print(f'Question: {qw}')
        user_answ = prompt.string('Your answer: ')
        if not (user_answ == answ):
            print(f"'{user_answ}' is wrong answer ;(. "
                  f"Correct answer was '{answ}'.\n"
                  f"Let\'s try again, {name}!")
            break
        print('Correct!')
        count_rounds += 1
    else:
        print(f'Congratulations, {name}!')
