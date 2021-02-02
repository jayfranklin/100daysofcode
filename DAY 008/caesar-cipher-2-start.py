alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
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


def decrypt(text,shift):
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

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)

