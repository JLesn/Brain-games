from random import randint

MESSAGE = 'What number is missing in the progression?'


def qw_and_answ():
    step = randint(1, 10)
    position = randint(0, 9)
    stop = randint(0, 100)
    start = stop - step * 10
    lst = [i for i in range(start, stop, step)]
    hidden = str(lst[position])
    lst[position] = '..'
    given = ' '.join(str(el) for el in lst)
    return given, hidden
