from random import randint
import prompt


def game_prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while counter != 3:
        counter += 1
        num = randint(2, 100)
        res = 'yes'
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                res = 'no'
        print(f'Question: {num}')
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
