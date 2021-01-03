# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Year = 365 days or 52 weeks
# 90 Years = 32850 days or 4680 weeks or 1080 months



y_left = 90-int(age)
m_left = 1080-(int(age)*12)
w_left = 4680-(int(age)*52)
d_left = 32850-(int(age)*365)

print(f"You have {d_left} days, {w_left} weeks, {m_left} months, and {y_left} years left")




