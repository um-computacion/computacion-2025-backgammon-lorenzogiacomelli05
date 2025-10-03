import random

class Dice:
    """
    Clase que representa los dados del Backgammon.
    Se encarga únicamente de la lógica de tirar y administrar valores de dados.
    """

    def __init__(self):
        """
        Inicializa los dados con valores y lista de usados vacíos.
        """
        self.__valores__ = []
        self.__usados__ = []

    def roll(self):
        """
        Simula una tirada de dos dados de seis caras.
        Si los valores son iguales (doble), se generan 4 valores.
        Caso contrario, se generan 2.
        
        Returns:
            list[int]: valores resultantes de la tirada.
        """
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        if d1 == d2:
            self.__valores__ = [d1, d1, d2, d2]
        else:
            self.__valores__ = [d1, d2]

        self.__usados__ = []
        return self.__valores__

    def get_values(self):
        """
        Devuelve los valores de la última tirada.
        
        Returns:
            list[int]: valores actuales de los dados.
        """
        return list(self.__valores__)

    def tirada_doble(self):
        """
        Indica si la última tirada fue un doble.
        
        Returns:
            bool: True si hay 4 valores (doble), False si no.
        """
        return len(self.__valores__) == 4

    def individual_values(self):
        """
        Devuelve siempre dos valores, uno por cada dado.
        En caso de haber tirada doble, devuelve el valor repetido.
        
        Returns:
            list[int]: dos valores de dados.
        """
        if self.tirada_doble():
            return [self.__valores__[0], self.__valores__[2]]
        return list(self.__valores__)

    def usar_valor(self, value: int):
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
        return list(self.__usados__)