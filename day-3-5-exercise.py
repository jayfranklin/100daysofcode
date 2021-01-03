# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Convert names to lowercase
names = name1 + name2
names_lower = names.lower()

#truelove = "truelove"
true = "true"
love = "love"


true_score = 0
true_score += names_lower.count(true[0])
true_score += names_lower.count(true[1])
true_score += names_lower.count(true[2])
true_score += names_lower.count(true[3])


# Testing variables
#print(true_score)

love_score = 0
love_score += names_lower.count(love[0])
love_score += names_lower.count(love[1])
love_score += names_lower.count(love[2])
love_score += names_lower.count(love[3])


# Testing variables
#print(love_score)
#
total_score = str(true_score) + str(love_score)
#
#print(type(total_score))
#
total_score_int = int(total_score)
#
#print(type(total_score_int))
#
#print(total_score)

if total_score_int < 10 or total_score_int > 90:
  print(f"Total score is {total_score} and you go together like coke and mentos.")
elif total_score_int >= 40 and total_score_int <= 50:
  print(f"Total score is {total_score} and you are alright together.")
else:
  print(f"Total score is {total_score}.")

