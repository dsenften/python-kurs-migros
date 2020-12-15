def fahrenheit(celsius):
    """Returns the temperature in degrees Fahrenheit"""
    return (celsius * 9 / 5) + 32

for degree in(10, 20, 30, 40):
    print(f'{degree}ºC → {fahrenheit(degree)}ºF')
    print(degree, ' ', fahrenheit(degree))