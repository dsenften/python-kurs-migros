class Lift:
    """Meine Klasse List macht dies und das."""

    def __init__(self, name):
        """Erstellen eines neuen Objektes..."""
        self.__name = name

    def up(self):
        pass

    def get_name(self):
        return self.__name

lift = Lift('A')

print(lift.get_name())

print(help(Lift))