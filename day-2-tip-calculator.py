#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator.")
subtotal = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people should split the bill? ")

# psudocode 
#  Incorrect first go around (maths)
#  total = ((subtotal * tip) + tiptotal) / people
#  
# Correct psudocode
# total = (tip / 1000 * subtotal + subtotal) / people

tiptotal = ((float(tip) / 100 * float(subtotal) + float(subtotal)))

total = round(float(tiptotal) / float(people),2)
total_amount = "{:.2f}".format(total)


# One liner, because why not
#total = "{:.2f}".format(round((float(tip)/100*float(subtotal)+float(subtotal))/float(people),2))


print(f"Each person should pay: {total_amount}")