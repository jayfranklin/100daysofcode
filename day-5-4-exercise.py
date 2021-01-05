#Write your code below this row 👇

# If number is divisible by 3, instead print fizz
# If number is divisible by 5, intead print buzz
# If number is divisible by both, instead print fizz buzz

Fizz = 0
Buzz = 0
FizzBuzz = 0
Neither = 0

for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:
    FizzBuzz += 1
    print("FizzBuzz")
  elif i % 3 == 0:
    Fizz += 1
    print("Fizz")
  elif i % 5 ==0:
    Buzz += 1
    print("Buzz")
  else:
    Neither +=1
    print(i)



print("Total of each: \n")
print(f"\tFizz:\t\t{Fizz}")
print(f"\tBuzz:\t\t{Buzz}")
print(f"\tFizzBuzz:\t{FizzBuzz}")
print(f"\tNeither:\t{Neither}")
