class Bruch(object):

    def __init__(self, z, n):
        self.__z, self.__n = self.kuerze(z, n)

    def __str__(self):
        return f'{self.__z} / {self.__n}'

    @staticmethod
    def ggT(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @classmethod
    def kuerze(cls, zaehler, nenner):
        g = cls.ggT(zaehler, nenner)
        return (zaehler // g, nenner // g)


x = Bruch(3528, 3780)
print(x)