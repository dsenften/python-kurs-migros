"""
Roboterklasse zur Positionsbeschreibung und Veränderung von Objekten
in einem zweidimensionalen Koordinatennsystem.
"""


class Robot(object):

    def __init__(self, x=0, y=0, orientation="north", name="marvin"):
        self.position = [x, y]
        self.orientation = orientation
        self.name = name

    def __str__(self):
        """ Stringdarstellung einer Instanz  """
        return f'{self.name} faces {self.orientation} at position {self.position}'

    def __repr__(self):
        return f'({self.name}, {self.orientation}, {self.position})'

    def move(self, distance):
        """ Methode zum Bewegen eines Roboters in Richtung seiner
        aktuellen Orientierung.

        Wird ein Roboter x mit x.move(10) aufgerufen und ist dieser
        Roboter östlich orientiert, also x.get_position() == ,,east''
        und ist beispielsweise [3,7] die aktuelle Position des
        Roboters, dann bewegt er sich 10 Felder östlich und befindet
        sich anschliessend in Position [3,17].

        """

        if self.orientation == "north":
            self.position[1] += distance
        elif self.orientation == "south":
            self.position[1] -= distance
        elif self.orientation == "west":
            self.position[0] -= distance
        elif self.orientation == "east":
            self.position[0] -= distance

    def new_orientation(self, o):
        """ Mit der Methode new_ox  rientation ädern wir die Orientierung
        des Roboters.

        o has to be in {"north","south","west","east"}

        Falls eine unbekannte Orientierung übergeben wird, wird der
        Roboter nicht bewegt.
        """

        if o in {"north", "south", "west", "east"}:
            self.orientation = o

    def get_orientation(self):
        """ Ein Aufruf von x.get_orientation() für einen Roboter x liefert
        dessen aktuelle Orientierung zurück, also eine der Richtungen
        "west", "south", "east" oder "north".
        """

        return self.orientation

    def get_position(self):
        """Liefert eine 2er-Liste mit [x,y] zurück."""

        return self.position

    def set_position(self, pos):
        """Damit kann man den Roboter auf eine neue Position im
        Koordinatensystem positionieren.

        pos muss eine Liste oder ein Tupel mit zwei Elementen sein.
        Ansonsten wird nichts getan."""

        # https://docs.python.org/3.3/library/functions.html#isinstance
        if isinstance(pos, (tuple, list)) and len(pos) == 2:
            self.position = pos

    def rename(self, name):
        """ Damit kann man dem Roboter einen neuen Namen geben. """
        self.name = name

    def get_name(self):
        """ Liefert den Namen des Roboters zurück. """
        return self.name
