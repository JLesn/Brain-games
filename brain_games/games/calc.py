from random import randint

MESSAGE = 'What is the result of the expression?'


def qw_and_answ():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    operations = ["+", "-", "*"]
    rand_operation = operations[randint(0, 2)]
    qw_operation = str(eval(f'{num1} {rand_operation} {num2}'))
    question = f'{num1} {rand_operation} {num2}'
    return question, qw_operation
