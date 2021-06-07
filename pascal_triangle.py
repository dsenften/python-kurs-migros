"""
$ python pascal_triangle.py
Input level: 5

        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
"""
from math import factorial

level = int(input('Input level: '))

for i in range(level):
    print('\n', ' ' * (level - i + 1), end='')
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=' ')
