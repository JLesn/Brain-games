import prompt
from random import randint
from math import gcd


def game_gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter != 3:
        counter += 1
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        res = str(gcd(num1, num2))
        print(f'Question: {num1} {num2}')
        answ = input()
        print(f'Your answer: {answ}')
        if res == answ:
            print('Correct!')
        else:
            print(
                f'\'{answ}\' is wrong answer ;(.'
                f' Correct answer was \'{res}\'.'
            )
            print(f'Let\'s try again, {name}!')
            break
        if counter == 3:
            print(f'Congratulations, {name}!')
