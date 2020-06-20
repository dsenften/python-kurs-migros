"""Mit diesem Beispiel wollen wir die Funktionalität
von Ausnahmen (Exceptions) zeigen."""

# Was passiert bei einer Division durch '0'

x, y = 3, 0
print(x / y)

# Hier ein anderes Beispiel
while True:
    zahl = input('Bitte eine Zahl eingeben: ')
    zahl = int(zahl)

# Besser...
while True:
    try:
        zahl = input('Bitte eine Zahl eingeben: ')
        zahl = int(zahl)
    except ValueError as e:
        print(f'Fehler: {e}')

# Spezielle Variable `nan`
from math import nan

x, y = 1, nan
print(x / y)
