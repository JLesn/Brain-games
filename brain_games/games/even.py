import prompt
from random import randint


def game_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter != 3:
        counter += 1
        num = randint(0, 100)
        print(f'Question: {num}')
        answ = input()
        print(f'Your answer: {answ}')
        if (num % 2 == 0):
            right = 'yes'
        else:
            right = 'no'
        if answ == right:
            print('Correct!')
        else:
            print(
                f'\'{answ}\' is wrong answer ;('
                f'. Correct answer was \'{right}\'.'
            )
            print(f'Let\'s try again, {name}!')
            break
        if counter == 3:
            print(f'Congratulations, {name}!')
