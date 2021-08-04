Weight = float(input("Enter your weight(kg):"))
Height = float(input("Enter your height(meter):"))
BMI = Weight/Height**2
if BMI < 18.5:
    a = "underweight"
if BMI > 18.4 and BMI < 25:
    a = "normal"
if BMI > 24.9 and BMI < 30:
    a = "overweight"
if BMI > 29.9 and BMI < 35:
    a = "obese"
if BMI > 35:
    a = "extremely obese"
print("Your BMI is:", BMI , a)
