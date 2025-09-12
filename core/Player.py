class Player:
    """
    Clase que representa a un jugador en Backgammon.
    """

    def __init__(self, numero, ficha):
        """
        Inicializa un jugador.
        Args:
            numero (int): número del jugador (1 o 2)
            ficha (str): símbolo de la ficha ('X' o 'O')
        """
        self.__numero__ = numero
        self.__ficha__ = ficha

    def get_numero(self):
        """
        Devuelve el número del jugador.
        Returns:
            int: 1 o 2
        """
        return self.__numero__

    def get_ficha(self):
        """
        Devuelve el símbolo de la ficha del jugador.
        Returns:
            str: 'X' o 'O'
        """
        return self.__ficha__
