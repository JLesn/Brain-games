from random import randint


def game():
  print('What number is missing in the progression?')
  step = randint(1, 10)
  position = randint(0, 9)
  stop = randint(0, 100)
  start = stop - step * 10
  lst = [i for i in range(start, stop, step)]
  hidden = str(lst[position])
  lst[position] = '..'
  given = ' '.join(str(el) for el in lst)
  print(f'Question: {given}')
  answ = input()
  print(f'Your answer: {answ}')
  if hidden == answ:
    return True
  else:
    print(
      f'\'{answ}\' is wrong answer ;(.'
      f' Correct answer was \'{hidden}\'.'
    )
    return False
