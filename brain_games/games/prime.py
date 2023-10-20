from random import randint


def game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    num = randint(2, 100)
    res = 'yes'
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            res = 'no'
    print(f'Question: {num}')
    answ = input()
    print(f'Your answer: {answ}')
    if res == answ:
        return True
    else:
        print(
          f'\'{answ}\' is wrong answer ;(.'
          f' Correct answer was \'{res}\'.'
        )
        return False
