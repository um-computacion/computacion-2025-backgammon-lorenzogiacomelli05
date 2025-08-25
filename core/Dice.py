import random

class Dice:
    """
    Clase que representa los dados del Backgammon.

    Atributos
    ---------
    _valores : list
        Lista con los valores obtenidos en la última tirada.
    """

    def __init__(self):
        """Inicializa el objeto Dice con una lista vacía de valores."""
        self._valores = []

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
            self._valores = [d1, d1, d2, d2]
        else:
            self._valores = [d1, d2]

        return self._valores

    def get_values(self):
        """Devuelve valores de la última tirada."""
        return self._valores

    def tirada_doble(self):
        """Indica si la última tirada fue un doble."""
        return len(self._valores) == 4

    def individual_values(self):
        """
        Devuelve los valores individuales de cada dado.
        Siempre devuelve dos elementos: [d1, d2].
        """
        if self.tirada_doble():
            return [self._valores[0], self._valores[2]]
        return self._valores
