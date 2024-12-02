import random as rd ## for the random number 
import numpy as np ## just in case...


# num = rd.randint(1,10)
# print(num)

def guess_game():
  # Random number create
  ans = rd.randint(1,10) ## random numbers from 1 to 10
  print("Let's begin the guessing game!")
  print("You can guess 1 ~ 10 and 3 trials for the game.")

  attemp = 0 # for counting the number of trials.
  ## while might need 
  while attemp < 3:
  ## for catching the input Error might need to use the try function
    try:
      ## player input
      
      player = int(input("Guess the number: "))
      if player < 1 or player > 10:
        print("please guess the number in 1 ~ 10")
        continue

    except ValueError: ## the case that player does not submit wrong type for the input.
      print("Invalid input. Please enter only integer number!")
      continue
    attemp +=1 # increase the number of trials.

    ## Give hint for the trials
    if player < ans:
      print("The answer is larger than your guess.")
    elif player > ans:
      print("The answer is smaller than your guess.")
    else:
      print(f"Congrats! your guess is correct!. You made it in {attemp}")
      return
    if attemp <3:
      print(f"You have {3- attemp} times for trial.")
    else:
      print("You used all of trials. Computer win!")
      print(f"The answer is {ans}")
      restart = input("Do you want to play again?? (y/n): ").strip().lower()
      attemp = 0 ## when you restart attemp need to be change for while condition.
      if restart != 'y':
        print("Game is done!")
        
        break

    
guess_game()
