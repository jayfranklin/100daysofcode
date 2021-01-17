#Write your code below this line 👇
def prime_checker(number):
  number = number
  prime = True
  print(f"You chose {number}")
  for i in range(2,number):
    if number % i == 0:
      prime = False
      #print("This is not a prime number.")
    i += 1

  if prime == False:
    print("It is not a prime number")
  else:
    print("It is a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)