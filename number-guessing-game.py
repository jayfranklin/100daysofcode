#Number Guessing Game Objectives:
from art_number import logo
import random

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print(logo)

NUMBER = random.randint(1,100)
#print(f"DEBUG - The number is {NUMBER}")

def intro():
  '''Introduction. Welcome user to game and have them pick a difficulty. Return the difficulty in amount of guesses'''
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    guesses = 10
  else:
    guesses = 5
  return guesses

def end_game():
  print("Thanks for playing!")
  return

guesses = intro()
total_guesses = guesses
continue_game = True

while continue_game == True:
  print(f"You have {guesses} attempts remaining to guess the number.")
  if guesses == total_guesses:
    guess = int(input("Make a guess: "))
  else:
    guess = int(input("Guess again: "))
  if guess == NUMBER:
    print(f"You got it! The number was {NUMBER}")
    continue_game = False
  elif guess > NUMBER:
    guesses -= 1
    print(f"Too high.")
  else: # guess < NUMBER
    print(f"Too low.")
    guesses -= 1
  if guesses == 0:
    print("You are out of guesses. You lose.")
    continue_game = False

end_game()
