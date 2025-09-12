import random

class Dice:
    """
    Clase que representa los dados del Backgammon.
    """

    def __init__(self):
        """
        Inicializa los dados con valores vacíos.
        """
        self.__valores__ = []
        self.__usados__ = []

    def roll(self):
        """
        Simula una tirada de dos dados de seis caras.
        Returns:
            list[int]: valores de los dados (4 si es doble, 2 si no lo es).
        """
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        if d1 == d2:  # tirada doble
            self.__valores__ = [d1, d1, d2, d2]
        else:
            self.__valores__ = [d1, d2]

        self.__usados__ = []  # reiniciar cuando hay nueva tirada
        return self.__valores__

    def get_values(self):
        """
        Devuelve los valores de la última tirada.
        Returns:
            list[int]: valores de la tirada.
        """
        return self.__valores__

    def tirada_doble(self):
        """
        Indica si la última tirada fue un doble.
        Returns:
            bool: True si hay 4 valores, False en caso contrario.
        """
        return len(self.__valores__) == 4

    def individual_values(self):
        """
        Devuelve siempre dos elementos: los valores de cada dado.
        Returns:
            list[int]: dos valores, uno por dado.
        """
        if self.tirada_doble():
            return [self.__valores__[0], self.__valores__[2]]
        return self.__valores__

    def usar_valor(self, value):
        """
        Marca un valor como usado si está disponible en la tirada.
        Args:
            value (int): valor a utilizar.
        Returns:
            bool: True si se pudo usar, False si no estaba disponible.
        """
        if value in self.__valores__:
            self.__valores__.remove(value)
            self.__usados__.append(value)
            return True
        return False

    def valores_usados(self):
        """
        Devuelve los valores que ya fueron usados en la tirada actual.
        Returns:
            list[int]: valores ya utilizados.
        """
        return self.__usados__
