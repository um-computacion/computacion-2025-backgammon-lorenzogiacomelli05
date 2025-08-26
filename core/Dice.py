import random

class Dice:
    """
    Clase que representa los dados del Backgammon.
    """

    def __init__(self):
        self.__valores__ = []
        self.__usados__ = []

    def roll(self):
        """Simula una tirada de dos dados de seis caras."""
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        if d1 == d2:  # tirada doble
            self.__valores__ = [d1, d1, d2, d2]
        else:
            self.__valores__ = [d1, d2]

        self.__usados__ = []  # reiniciar cuando hay nueva tirada
        return self.__valores__

    def get_values(self):
        """Devuelve los valores de la última tirada."""
        return self.__valores__

    def tirada_doble(self):
        """Indica si la última tirada fue un doble."""
        return len(self.__valores__) == 4

    def individual_values(self):
        """Devuelve siempre dos elementos: los valores de cada dado."""
        if self.tirada_doble():
            return [self.__valores__[0], self.__valores__[2]]
        return self.__valores__

    def usar_valor(self, value):
        """
        Marca un valor como usado si está disponible en la tirada.
        Retorna True si lo pudo usar, False si no.
        """
        if value in self.__valores__:
            self.__valores__.remove(value)
            self.__usados__.append(value)
            return True
        return False

    def valores_usados(self):
        """Devuelve los valores que ya fueron usados en la tirada actual."""
        return self.__usados__
