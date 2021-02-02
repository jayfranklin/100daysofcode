# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# Without using for loop
#  total = sum(student_heights)
#  average = round(total / len(student_heights))
#  print(average)

# Using some for loops

total = 0
for student in student_heights:
  total += student

students = 0
for each in student_heights:
  students += 1

average = round(total/students)
print(average)
