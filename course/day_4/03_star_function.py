def f(x, y, z):
    print(x, y, z)


p = (1, 2, 3)
f(*p)


# ---

def g(*args):
    return args

g(1, 2, 3, 4)
