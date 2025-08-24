# Primer esqueleto de clase Dice
import random

class Dice:
    """
    Clase que representa los dados del Backgammon.

    Atributos
    ---------
    __valores__ : list
        Lista con los valores obtenidos en la última tirada.
    """

    def __init__(self):
        """
        Inicializa el objeto Dice con una lista vacía de valores.
        """
        self.__valores__ = []

    def roll(self):
        """
        Simula una tirada de dos dados de seis caras.

        Returns
        -------
        list :
            - Si es normal → [d1, d2]
            - Si es doble  → [d1, d1, d2, d2]
        """
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        
        if d1 == d2:  # tirada doble
            self.__valores__ = [d1, d1, d2, d2]
        else:
            self.__valores__ = [d1, d2]

        return self.__valores__

def get_values(self):
    """
    Devuelve los valores de la última tirada.
    """
    return self.__valores__

