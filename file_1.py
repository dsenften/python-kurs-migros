class Roboter:

    def say_hello(self):


if __name__ == "__main__":
    x = Roboter()
    y = Roboter()
    y2 = y
    print(id(y2), id(y))
