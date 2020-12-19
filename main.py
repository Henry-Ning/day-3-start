# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight/height**2, 2)

print(bmi)

if bmi < 18.5:
  print("underweight")
elif bmi < 25:
  print("normal weight")
elif bmi < 30:
  print("overweight")
else:
  print("obese")