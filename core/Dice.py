#Primer esqueleto de clase Dice
import random

class Dice:
    def __init__(self):
        self.__valores__ = []

    def roll(self):
        """
        Simula tirada de dos dados.
        Devuelve:
        ---------
        list : 
            - Si es normal → [d1, d2]
            - Si es doble → [d1, d1, d2, d2]
        """
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        
        if d1 == d2:  # tirada doble
            self.__valores__ = [d1, d1, d2, d2]
        else:
            self.__valores__ = [d1, d2]

        return self.__valores__
