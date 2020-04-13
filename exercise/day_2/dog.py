age = int(input("Alter des Hundes: "))

if age < 0:
    print("Das stimmt wohl kaum!")
elif age == 1:
    print("Entspricht ca. 14 Jahren")
elif age == 2:
    print("Entspricht ca. 22 Jahren")
elif age > 2:
    human = 22 + (age - 2) * 5
    print(f"Entsprich ca. {human} Jahren")
