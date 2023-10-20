from random import randint


def game():
  print('Answer "yes" if the number is even, otherwise answer "no".')
  num = randint(0, 100)
  print(f'Question: {num}')
  answ = input()
  print(f'Your answer: {answ}')
  if (num % 2 == 0):
    right = 'yes'
  else:
    right = 'no'
  if answ == right:
    return True
  else:
    print(
      f'\'{answ}\' is wrong answer ;('
      f'. Correct answer was \'{right}\'.'
    )
    return False
