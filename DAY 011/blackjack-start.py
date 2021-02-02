############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Import required libraries
import random


# Define deck of cards (list)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Definie global variables
continue_playing = True

# Deal Hand
def deal_hand():
  your_cards = []
  computer_cards =[]
  your_cards.append(random.choice(cards))
  your_cards.append(random.choice(cards))
  computer_cards.append(random.choice(cards))
  computer_cards.append(random.choice(cards))
  print(f"Your cards: {your_cards}, current score {calculate_score(your_cards)}")
  print(f"Computer's first card: {computer_cards[0]}")
  
  add_own_card(your_cards)
  add_computer_card(computer_cards)

  if calculate_score(your_cards) > 21:
    bust(your_cards,computer_cards)
  else:
    show_final_scores(your_cards,computer_cards)
  

def bust(your_cards, computer_cards):
  show_final_scores(your_cards, computer_cards)
  end()

def show_final_scores(your_cards, computer_cards):
  print(f"Your cards: {your_cards}, final score: {calculate_score(your_cards)}")
  print(f"Computer cards: {computer_cards}, final score: {calculate_score(computer_cards)}")
  if calculate_score(your_cards) > 21:
    print("You went over. You lose.")
    end()
  elif calculate_score(computer_cards) > 21:
    print("You win! The computer bust!")
    end()
  elif calculate_score(your_cards) >  calculate_score(computer_cards):
    print("You win!")
    end()
  else:
    print("You lose.")
    end()

def end():
  play_game()


# Add card to existing hand
def add_own_card(some_cards):
  your_cards = some_cards
  hit_me = True
  while hit_me == True:
    if calculate_score(your_cards) > 21:
      hit_me = False
    else:
      hit = input("Type 'y' to hit or 'n' to stay  ")
      if hit == 'y':
        some_cards.append(random.choice(cards))
        print(f"Your cards: {your_cards}, current score: {calculate_score(your_cards)}")
      else:
        hit_me = False
        print(f"Your cards: {your_cards}, current score: {calculate_score(your_cards)}")
        return

# Add card to existing hand
def add_computer_card(some_cards):
  computer_cards = some_cards
  while calculate_score(some_cards) <= 16:
    if calculate_score(some_cards) <=16:
      some_cards.append(random.choice(cards))
    elif calculate_score(some_cards) > 21:
      bust()
    
     

def show_scores():
  # Should we make this it's own function?
  print()


# Calculate score among cards in hand
def calculate_score(some_cards):
  point_total = 0
  for i in some_cards:
    point_total += i
  return point_total

# Play Game
def play_game():
  continue_playing = True
  play = input("Do you want to play a game of blackjack? Enter 'y' or 'n'")
  if play == 'n':
    quit_game()
  else:
    deal_hand()

# End game
def quit_game():
  continue_playing = False
  print("Thanks for playing! Goodbye.")
  quit()


while continue_playing == True:
  deal_hand()



