from random import randint
from math import gcd


def game():
    print('Find the greatest common divisor of given numbers.')
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    result = str(gcd(num1, num2))
    print(f'Question: {num1} {num2}')
    answ = input()
    print(f'Your answer: {answ}')
    if result == answ:
        return True
    else:
        print(f'\'{answ}\' is wrong answer ;(.'
              f' Correct answer was \'{result}\'.')
        return False
