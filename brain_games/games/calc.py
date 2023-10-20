from random import randint


def game():
  print('What is the result of the expression?')
  num1 = randint(0, 100)
  num2 = randint(0, 100)
  operations = ["+", "-", "*"]
  rand_operation = operations[randint(0, 2)]
  qw_operation = str(eval(f'{num1} {rand_operation} {num2}'))
  print(f'Question: {num1} {rand_operation} {num2}')
  answ = input()
  print(f'Your answer: {answ}')
  if qw_operation == answ:
    return True
  else:
    print(
      f'\'{answ}\' is wrong answer'
      f';(. Correct answer was \'{qw_operation}\'.'
    )
  return False
