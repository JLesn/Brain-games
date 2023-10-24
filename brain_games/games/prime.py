from random import randint

MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 1:
        return 'no'
    for i in range(2, (num // 2 + 1)):
        if num % i == 0:
            return 'no'
    return 'yes'


def qw_and_answ():
    num = randint(2, 100)
    qw = str(num)
    return qw, is_prime(num)
