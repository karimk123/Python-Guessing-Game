
from random import seed
from random import randint
import time


print('Hello! What is your name ?')
myName = input()





def playGame():
  

  guessesTaken = 0
  num = randint(1,10)

 
  print("Well " + myName + ' I am thinking of a number between 1-10.')

  while guessesTaken < 6 :
      print("Take a guess.")
      guess = input()
      guess = int(guess)
      guessesTaken+=1

      if (guess < num):
        print('Your guess is too low.')
      if (guess > num):
        print('Your guess is too high')

      
      if(guess == num):
        guessesTaken = str(guessesTaken)
        print('Good job '+ myName + ' ! You guessed my number in ' +  guessesTaken + ' guesses !')
        break
  
  if (guess != num):
    num = str(num)
    print('Nope. The number I was thinking of was ' + num)
       
       
      
      
  # restart
  print('Hey, ' + myName+ " Want to play again ?")
  guessTwo = input()
  
 
  if (guessTwo == 'yes' or guessTwo == 'ok' or guessTwo == 'sure' or guessTwo == 'fine' or guessTwo == 'okay'):
      playGame()
  if(guessTwo == 'no'):
      exit()
    
playGame()    