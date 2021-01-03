# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Convert names to lowercase
n1_lower = name1.lower()
n2_lower = name2.lower()

truelove = "truelove"

n1_score = 0
n1_score += n1_lower.count(truelove[0])
n1_score += n1_lower.count(truelove[1])
n1_score += n1_lower.count(truelove[2])
n1_score += n1_lower.count(truelove[3])
n1_score += n1_lower.count(truelove[4])
n1_score += n1_lower.count(truelove[5])
n1_score += n1_lower.count(truelove[6])
n1_score += n1_lower.count(truelove[7])

# Testing variables
#print(n1_score)

n2_score = 0
n2_score += n2_lower.count(truelove[0])
n2_score += n2_lower.count(truelove[1])
n2_score += n2_lower.count(truelove[2])
n2_score += n2_lower.count(truelove[3])
n2_score += n2_lower.count(truelove[4])
n2_score += n2_lower.count(truelove[5])
n2_score += n2_lower.count(truelove[6])
n2_score += n2_lower.count(truelove[7])



# Testing variables
#print(n2_score)
#
total_score = str(n1_score) + str(n2_score)
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
elif total_score_int > 40 and total_score_int < 50:
  print(f"Total score is {total_score} and you are alright together.")
else:
  print(f"Total score is {total_score}.")

