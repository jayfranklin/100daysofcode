#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

secure = ""
i=0

while i < nr_letters:
  secure += random.choice(letters)
  i += 1

i = 0
while i < nr_symbols:
  secure += random.choice(numbers)
  i += 1

i = 0
while i < nr_numbers:
  secure += random.choice(symbols)
  i += 1

# Alternate method using for loop (duplicate for each list above)
#for i in range(1, nr_letters +1):
#  secure += random.choice(letters)


print(f"Your secure password is:\t{secure}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# Let's randomize our secure password
secure_new = ''.join(random.sample(secure,len(secure)))

# Alternate method using random.shuffle
#secure_new = random.shuffle(secure)
#for i in secure:
#  secure2 += i


print(f"Your new secure password is: \t{secure_new}")