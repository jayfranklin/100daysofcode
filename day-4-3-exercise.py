# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# We need to split the string into multiple characters to do our list and convert it to an integer
row = int(position[0])
column = int(position[1])

#print(row)
#print(column)

# Now we need to change  the value of our position [] to an X. We have to use -1 otherwise, we can get an IndexError
map[row-1][column-1] = "X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")