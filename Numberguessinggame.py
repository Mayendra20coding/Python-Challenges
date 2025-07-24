import random
import time
number=random.randint(1,100)
def intro():
  print('may i ask for your name')
  global name
  name=input()
  print(name + ',we are going to play a game.I am thinking of a number between 1 and 100')
  if(number%2==0):
    x='even'
  else:
    x='odd'
  print('\nThis is an{}number'.format(x))
  time.sleep(.5)
  print('Go ahead.Guess!')
def pick():
  guessestaken=0
  while guessestaken <6:
    time.sleep(.25)
    enter=input('Guess: ')
    try:
      guess=int('enter')
      if guess<=100 and guess>=1:
        guessestaken=guessestaken+1
        if guessestaken<6:
          if guess<number:
            print('The guess of the number that you have entered is too low')
          if guess>number:
            print('The guess of the number that you have entered is too high')
          if guess != number:
             time.sleep(.5)
             print('Try Again!')
          if guess==number:
            break
      if guess>100 or guess<1:
        print('Silly Goose! That number isnt in the range')
        time.sleep(.25)
        print('please enter a number between 1 and 100')
    except:
        print('I dont think that '+enter+' is a number Sorry.')
  if guess == number:
      guessestaken=str(guessestaken)
      print('Good job,{}!You guessed my number in {} guesses!'.format(name,guessestaken))
  if guess != number:
      print('Nope. The number i was thinking of was' + str(number))
playagain='yes'
while playagain=='yes':
    intro()
    pick()
    print('Do you want to play again?')
    playagain=input()