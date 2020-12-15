class Person:

    def __init__(self, first_name, last_name):
        """Konstruktor zur Erstellung einer neuen Person"""
        self.__first_name = first_name
        self.__last_name = last_name

    def __str__(self):
        return f'{self.__first_name} {self.__last_name}'

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    last_name = property(get_last_name, set_last_name)

a = Person('Peter', 'Müller')
a.last_name = 'Müller-Meier'

print(a)