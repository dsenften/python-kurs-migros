year = int(input("Bitt gib das Jahr ein [yyyy]: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False

if leap_year:
    print(f"{year} ist ein Schaltjahr")
else:
    print(f"{year} ist kein Schaltjahr")