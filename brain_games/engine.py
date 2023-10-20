import prompt


def run_game(game_name):
  print('Welcome to the Brain Games!')
  name = prompt.string('May I have your name ? ')
  print(f'Hello, {name}!')
  counter = 0
  while counter != 3:
    counter += 1
    res = game_name.game()
    if res == True:
      print('Correct!')
      print(f'Congratulations, {name}!')
    if res == False:
      print(f'Let\'s try again, {name}!')
      break
