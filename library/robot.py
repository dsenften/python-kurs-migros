"""
Roboterklasse zur Positionsbeschreibung und Veränderung von Objekten
in einem zweidimensionalen Koordinatennsystem.
"""


class Robot(object):

    def __init__(self, position=None, orientation="north", name="marvin"):
        if position is None:
            position = [0, 0]
        self.__position = position
        self.__orientation = orientation
        self.__name = name

    def __str__(self):
        """ Stringdarstellung einer Instanz  """
        return f'{self.__name} faces {self.__orientation} at position {self.__position}'

    def __repr__(self):
        return f'{__class__.__name__}({self.__position}, \'{self.__orientation}\', \'{self.__name}\')'

    def move(self, distance):
        """ Methode zum Bewegen eines Roboters in Richtung seiner
        aktuellen Orientierung.

        Wird ein Roboter x mit x.move(10) aufgerufen und ist dieser
        Roboter östlich orientiert, also x.get_position() == ,,east''
        und ist beispielsweise [3,7] die aktuelle Position des
        Roboters, dann bewegt er sich 10 Felder östlich und befindet
        sich anschliessend in Position [3,17].

        """

        if self.__orientation == "north":
            self.__position[1] += distance
        elif self.__orientation == "south":
            self.__position[1] -= distance
        elif self.__orientation == "west":
            self.__position[0] -= distance
        elif self.__orientation == "east":
            self.__position[0] -= distance

    @property
    def orientation(self):
        """ Ein Aufruf von x.get_orientation() für einen Roboter x liefert
        dessen aktuelle Orientierung zurück, also eine der Richtungen
        "west", "south", "east" oder "north".
        """

        return self.__orientation

    @orientation.setter
    def orientation(self, o):
        """ Mit der Methode new_ox  rientation ädern wir die Orientierung
        des Roboters.

        o has to be in {"north","south","west","east"}

        Falls eine unbekannte Orientierung übergeben wird, wird der
        Roboter nicht bewegt.
        """

        if o in {"north", "south", "west", "east"}:
            self.__orientation = o

    @property
    def position(self):
        """Liefert eine 2er-Liste mit [x,y] zurück."""

        return self.position

    @position.setter
    def position(self, pos):
        """Damit kann man den Roboter auf eine neue Position im
        Koordinatensystem positionieren.

        pos muss eine Liste oder ein Tupel mit zwei Elementen sein.
        Ansonsten wird nichts unternommen."""

        # https://docs.python.org/3.3/library/functions.html#isinstance
        if isinstance(pos, (tuple, list)) and len(pos) == 2:
            self.__position = pos

    @property
    def name(self):
        """ Liefert den Namen des Roboters zurück. """
        return self.__name

    @name.setter
    def name(self, name):
        """ Damit kann man dem Roboter einen neuen Namen geben. """
        self.__name = name


if __name__ == "__main__":
    """
    Die folgenden Aufrufe sollten eigentlich aus einer externen Umgebung
    aufgerufen werden, da wir mit dieser Datei/Klasse auch die Verwendung 
    von eigenen Modulen/Libraries aufzeigen wollen. 
    """

    my_robot = Robot([3, 4], "north", "Marvin")
    print(my_robot)

    my_robot.move(10)
    my_robot.orientation = "west"
    my_robot.move(7)
    print(my_robot)

    new_name = "Andrew"
    print(f'{my_robot.name} will be renamed as {new_name}')

    my_robot.name = new_name
    print(f'Hi, this is {my_robot.name}')

    my_robot.position = [0, 0]
    print(my_robot)
    print(my_robot.__repr__())
