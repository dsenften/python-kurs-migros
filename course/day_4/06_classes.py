class Person:

    def __init__(self):

    def say_hello(self):
        print("Hello")


if __name__ == '__main__':
    peter = Person()
    marie = Person()
    print(peter == marie)

    print(type(peter))
