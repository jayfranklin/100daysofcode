# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# Get length of list so we can feed that into the random integer function
#   We could probably do this on the random.randint line, but this is probably easier to read
length = len(names)
random = random.randint(0,length)

#  We have to subtract 1 from our random integer because lists start at 0. 
pick = str(names[random-1])
print(f"{pick} was chosen to paying for lunch!")