import random

a = 1
b = 100


while True:
  print('Click enter to start the game')
  y = random.randint(a, b)
  while True:
    num = input('Enter your number guess: ')
    num = int(num)
    print(num)

    if(num > y):
      print('Your guess is more than the answer')
    elif(y > num):
      print('Your guess is less than the answer')
    elif(y == num):
      print('You guessed right!!')
    