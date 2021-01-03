# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# One line. Works, but difficult to read
#print(int(float(weight)/float(height)**2))

# Let's find out the raw BMI   weight/height^2
#  Remember, our input was a string, so we have to convert them to floats since 
#  we could recieve a number with a decimal point. If we used integers here, it
#  would not be very accurate
bmi_raw = (float(weight)/float(height)**2)

# Store bmi_raw as an integer
bmi_whole = int(bmi_raw)

status = "undefined"

if bmi_whole < 18.5:
  status = "underweight"
elif bmi_whole < 25:
  status = "normal weight"
elif bmi_whole < 30:
  status = "overweight"
elif bmi_whole < 35:
  status = "obese"
else:
  status = "clinically obese"

# Finally, we print the result
#print(bmi_whole)
print(f"Your BMI is {bmi_whole} and you are considered {status}.")
