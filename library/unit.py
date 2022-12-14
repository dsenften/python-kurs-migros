class Length:
    __metric = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344,
        "nm": 1852,
    }

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit

    def converte_to_meter(self):
        return self.value * Length.__metric[self.unit]

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            l = self.converte_to_meter() + other
        else:
            l = self.converte_to_meter() + other.converte_to_meter()
        return Length(l / Length.__metric[self.unit], self.unit)

    def __iadd__(self, other):
        if type(other) == int or type(other) == float:
            l = self.converte_to_meter() + other
        else:
            l = self.converte_to_meter() + other.converte_to_meter()
        self.value = l / Length.__metric[self.unit]
        return self

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            l = self.converte_to_meter() - other
        else:
            l = self.converte_to_meter() - other.converte_to_meter()
        return Length(l / Length.__metric[self.unit], self.unit)

    def __isub__(self, other):
        if type(other) == int or type(other) == float:
            l = self.converte_to_meter() - other
        else:
            l = self.converte_to_meter() - other.converte_to_meter()
        self.value = l / Length.__metric[self.unit]
        return self

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            l = self.converte_to_meter() * other
        else:
            l = self.converte_to_meter() * other.converte_to_meter()
        return Length(l / Length.__metric[self.unit], self.unit)

    def __imul__(self, other):
        if type(other) == int or type(other) == float:
            l = self.converte_to_meter() * other
        else:
            l = self.converte_to_meter() * other.converte_to_meter()
        self.value = l / Length.__metric[self.unit]
        return self

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            l = self.converte_to_meter() / other
        else:
            l = self.converte_to_meter() / other.converte_to_meter()
            return Length(l / Length.__metric[self.unit], self.unit)

    def __itruediv__(self, other):
        if type(other) == int or type(other) == float:
            l = self.converte_to_meter() / other
        else:
            l = self.converte_to_meter() / other.converte_to_meter()
        self.value = l / Length.__metric[self.unit]
        return self

    def __radd__(self, other):
        return Length.__add__(self, other)

    def __rsub__(self, other):
        return Length.__sub__(self, other)

    def __rmul__(self, other):
        return Length.__mul__(self, other)

    def __rtrudiv__(self, other):
        return Length.__truediv__(self, other)

    def __str__(self):
        return str(self.converte_to_meter())

    def __repr__(self):
        return str((self.value, self.unit))


if __name__ == "__main__":
    """
    Die folgenden Aufrufe sollten eigentlich aus einer externen Umgebung
    aufgerufen werden, da wir mit dieser Datei/Klasse auch die Verwendung 
    von eigenen Modulen/Libraries aufzeigen wollen. 
    """

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
