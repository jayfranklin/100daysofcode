# Import required modules
import random

# Import art
from art import logo  # Main logo
from art import vs    # VS logo

# Import game data
from game_data import data

# Import clear function
from replit import clear

# Sample data  - contains 50 elements (len(data))
#data = [
#    {
#        'name': 'Instagram',
#        'follower_count': 346,
#        'description': 'Social media platform',
#        'country': 'United States'
#    },

def generate_new_player():
  player = random.choice(data)
  return player

person_a = generate_new_player()
person_b = generate_new_player()

#print(person_a)

# Iterate through person_a
def a_stats(person):
  name = person.get('name')
  count = person.get('follower_count')
  desc = person.get('description')
  country = person.get('country')
  print(f"Compare A: {name}, a {desc}, from {country}.")

def b_stats(person):
  name = person.get('name')
  count = person.get('follower_count')
  desc = person.get('description')
  country = person.get('country')
  #print(f"Against B: {name}, a {desc}, from {country} with {count} followers.")
  print(f"Against B: {name}, a {desc}, from {country}.")

#a_stats(person_a)
#b_stats(person_b)

correct_count = 0

def end_game():
  print(f"You were correct {correct_count} times.")
  return

continue_game = True
while continue_game == True:
  # Determine who is winner for next round
  winner = {}
  # Print main logo
  print(logo)
  
  # Check if on a winning streak. If so, congratulate and print streak count
  if correct_count > 0:
    print(f"You're right! Current score: {correct_count}")

  a_stats(person_a)
  print(vs) # VS logo
  b_stats(person_b)

  guess = input("Who has more followers? Type 'A' or 'B': ")
  if guess == 'A':
    if person_a.get('follower_count')  > person_b.get('follower_count'):
      correct_count += 1
      winner = person_a
      clear()
    else:
      print("Incorrect. You lose.")
      continue_game = False
  else:
    if person_a.get('follower_count')  < person_b.get('follower_count'):
      correct_count += 1
      winner = person_b
      clear()
    else:
      print("Incorrect. You lose.")
      continue_game = False
  
  # Move winning player to person_a and generate new person_b
  person_a = winner
  #print(person_a)
  person_b = generate_new_player()
  #print(person_b)

         

end_game()

