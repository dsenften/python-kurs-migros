class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        '''This method returns the string representation of the object.
        This method is called when print() or str() function is invoked
        on the object.'''

        return(f'{self.first_name} {self.last_name}')

person = Person('Peter', 'Müller')

print(person)
