alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # Redefined into original alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(direction,text,shift):
  if direction == "encode":
    cipherlist = []
    cipher = ""
    for letter in text:
      # find index of letter in alphabet
      position = alphabet.index(letter) + 1
      #print(f"Letter {letter} is in position {position}")
      new_position = position + shift
      if new_position > 26:
        new_position -=26
      #print(f"Letter {letter} shifted {shift} positions is {new_position}")
      cipherlist.append(alphabet[new_position -1])
    for i in cipherlist:
      cipher += i
    print(f"Cipher of {text} is {cipher}")
    
  elif direction == "decode":
    plainlist=[]
    plain = ""
    for letter in text:
      # find index of letter in alphabet
      position = alphabet.index(letter) + 1
      # determine if position - shift will be <= 0
      if position - shift <= 0:
        #difference = position - shift
        new_position = position - shift
        new_position +=26
      new_position = position - shift
      #print(f"Letter {letter} shifted left into position {new_position}")
      plainlist.append(alphabet[new_position -1])
    for i in plainlist:
      plain += i
    print(f"Plain of {text} is {plain}")  

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(direction, text, shift)