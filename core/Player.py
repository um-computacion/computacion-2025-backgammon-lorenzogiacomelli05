class Player:
    """
    Representa a un jugador en el Backgammon.
    """

    def __init__(self, numero: int, ficha: str):
        """
        Inicializa un jugador con su número y símbolo de ficha.

        Args:
            numero (int): número del jugador (1 o 2).
            ficha (str): símbolo de la ficha (por ejemplo, 'X' o 'O').
        """
        self.__numero__ = numero  # Número del jugador (1 o 2)
        self.__ficha__ = ficha    # Símbolo de la ficha del jugador

    def get_numero(self) -> int:
        """
        Devuelve el número del jugador.
        Returns:
            int: 1 o 2, identificador único del jugador.
        """
        return self.__numero__

    def get_ficha(self) -> str:
        """
        Devuelve el símbolo de la ficha asociado al jugador.
        Returns:
            str: símbolo de la ficha (ej. 'X' o 'O').
        """
        return self.__ficha__
