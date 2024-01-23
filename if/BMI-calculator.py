# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height**2)

if bmi < 18.5:
  print(f"Your BMI is {round(bmi, 5)}, you are underweight.")
  quit()

if bmi < 25:
  print(f"Your BMI is {round(bmi, 1)}, you have a normal weight.")
  quit()

if bmi < 30:
  print(f"Your BMI is {round(bmi, 5)}, you are slightly overweight.")
  quit()

if bmi < 35:
  print(f"Your BMI is {round(bmi, 5)}, you are obese.")
  quit()

print(f"Your BMI is {round(bmi, 5)}, you are clinically obese.")