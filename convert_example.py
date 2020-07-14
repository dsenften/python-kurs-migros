from conversions.unit import Length

if __name__ == "__main__":
    x = Length(4)
    print(x)
    print(repr(x))
    print(x + 5.6)
    print(7 + x)
    x += Length(4, "yd")
    print(x)
    x += 4
    x -= Length(4, "m")
    print(x)
    z = 4 + Length(8, "yd")
    y = Length(4.5, "yd") + x / Length(0.77, "in")
    print(repr(y))
    print(y)
