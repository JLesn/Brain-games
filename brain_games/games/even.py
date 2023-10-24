from random import randint

MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def qw_and_answ():
    num = randint(0, 100)
    qw = str(num)
    if (num % 2 == 0):
        right = 'yes'
    else:
        right = 'no'
    return qw, right
