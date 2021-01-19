student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to add the grades to student_grades.👇
for k, v in student_scores.items():
  if v > 90:
    grade = "Outstanding"
  elif v > 80:
    grade = "Exceeds Expectations"
  elif v > 70:
    grade = "Acceptable"
  else:
    grade = "Fail"
  student_grades[k] = grade

#for k, v in student_grades.items():
#  print(f"Student {k} -> {v}")


# 🚨 Don't change the code below 👇
print(student_grades)
