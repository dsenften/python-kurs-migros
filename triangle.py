"""
USAGE:
    $ python triangle.py

    Triangle's height: 5

         *
        * *
       * * *
      * * * *
     * * * * *
"""

height = int(input("Triangle's height: "))
for i in range(height + 1):
    print(' ' * (height - i), '* ' * i)
