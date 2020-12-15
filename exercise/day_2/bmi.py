# Berechnen des BMI

body_height = float(input("Körpergrösse [m]: "))
body_weight = float(input("Körpergewicht [kg]: "))

bmi = body_weight / body_height ** 2

print(f"\nBMI = {round(bmi,2)}")