from random import randint
import prompt


def game_progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name ? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    counter = 0
    while counter != 3:
        counter += 1
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
            print('Correct!')
        else:
            print(
                f'\'{answ}\' is wrong answer ;(.'
                f' Correct answer was \'{hidden}\'.'
            )
            print(f'Let\'s try again, {name}!')
            break
        if counter == 3:
            print(f'Congratulations, {name}!')
