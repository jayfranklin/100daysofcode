# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
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

# Finally, we print the result
print(bmi_whole)

