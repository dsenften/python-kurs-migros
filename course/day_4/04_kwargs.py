def foo(*args, **kwargs):
    print(f'args   → {args}')
    print(f'kwargs → {kwargs}')


foo(42, 89, 12, x=17, y='Hello', z=[3, 8, 9])

def bar(x, y=0):
    print(x + y)

bar(x=5, y=6)
bar(5)