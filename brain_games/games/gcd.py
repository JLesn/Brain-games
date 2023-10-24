from random import randint
from math import gcd

MESSAGE = 'Find the greatest common divisor of given numbers.'


def qw_and_answ():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    qw = f'{num1}{num2}'
    result = str(gcd(num1, num2))
    return qw, result
