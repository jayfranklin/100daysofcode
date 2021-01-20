# Define basic calculator functions

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

# Dictionary for storing mathematical functions
operations = {"+":add, "-":subtract, "*":multiply, "/":divide}

# Ask user for input
num1 = int(input("What's the first number? "))

print("Available operations: ")
for key in operations:
  print(key)
choice = input("Choose the operation from above that you wish to use. ")
num2 = int(input("What's the second number? "))
answer = operations[choice](num1, num2)
print(f"{num1} {choice} {num2} = {answer}")

choice2 = input("Choose another operation. ")
num3 = int(input("Choose another number. "))

answer2 =operations[choice2](answer,num3)
print(f"{answer} {choice2} {num3} = {answer2}")
