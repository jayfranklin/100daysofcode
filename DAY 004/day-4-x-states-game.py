# Quick game to check someone's knwoledge of the US States

# TODO:  
#  Find differences between guesses and states
#  Determine a better looping mechanism

import random


#states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado"]

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


#number = random.randint(1,50)
#print(states[number-1])

tries = 0
errors = 0
guesses = []
correct = []

print("Let's play a game. Try to guess all of the states. When you select a state that's incorrect or has already been mentioned, a warning will be displayed and you can try again!")

#guess = input("Enter a state name: ")

''''
guess = ["Alabama","Kansas","Florida"]

r = random.randint(1,3)
if (guess[r-1] in states):
  print(f"{guess} is in the list.")

'''

while len(guesses) <50 :
  guess = input("Enter a state name: ")
  if (guess in states) and (guess not in guesses):
    tries += 1
    guesses.append(guess)
    correct.append(guess)
    print(f"Correct. {guess} is a US State! Keep going!")
    print(guesses)
  elif guess in guesses:
    errors += 1
    tries += 1
    guesses.append(guess)
    print("You've already mentioned this one! Try again.")
  elif guess not in states:
    errors += 1
    tries += 1
    guesses.append(guess)
    print(f"{guess} is not a US state. Try again!")

# Let's do some sorting for easier comparison
s_guesses = sorted(guesses)
s_states = sorted(states)
s_correct = sorted(correct)
#print(s_guesses)
#print(s_states)
print("=================================================================")
print("=== \t\t\t Results are in ! ")
print("\n\n\n")
if s_guesses == s_states:
  print(f"Congrats! You guessed all of the states! It took you {tries} tries and you had {errors} mistakes")
else:
  print("Sorry. You identified " + str(len(s_correct)) + " states in " + str(tries) + " tries.")
  print(f"Correctly identified states were: \n{s_correct}.")
  # print(f"You missed the following: \n{difference}") 

