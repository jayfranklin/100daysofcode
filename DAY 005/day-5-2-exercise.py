# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Since we can't use min and max, we also don't want to use sort and grab the last item
#  Let's use a for loop to iterate through the list and pick out the highest index

high = 0
for score in student_scores:
  if score > high:
    high = score


print(f"The high score is {high}")

