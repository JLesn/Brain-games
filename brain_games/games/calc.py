import prompt
from random import randint


def game_calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    counter = 0
    while counter != 3:
        counter += 1
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        operations = ["+", "-", "*"]
        rand_operation = operations[randint(0, 2)]
        qw_operation = str(eval(f'{num1} {rand_operation} {num2}'))
        print(f'Question: {num1} {rand_operation} {num2}')
        answ = input()
        print(f'Your answer: {answ}')
        if qw_operation == answ:
            print('Correct!')
        else:
            print(
                f'\'{answ}\' is wrong answer'
                f';(. Correct answer was \'{qw_operation}\'.'
            )
            print(f'Let\'s try again, {name}!')
            break
        if counter == 3:
            print(f'Congratulations, {name}!')
