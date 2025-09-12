class Checker:
    """
    Representa una ficha individual en el Backgammon.
    Cada ficha pertenece a un jugador y puede estar en la barra o en la meta.
    """

    def __init__(self, jugador):
        """
        Inicializa una ficha para un jugador determinado.
        Args:
            jugador (int): 1 o 2, indica el jugador dueño de la ficha.
        """
        self.__jugador__ = jugador    # Jugador dueño de la ficha (1 o 2)
        self.__en_barra__ = False     # True si la ficha está en la barra
        self.__en_meta__ = False      # True si la ficha ya salió del tablero

    def get_jugador(self):
        """Devuelve el jugador dueño de la ficha."""
        return self.__jugador__

    def esta_en_barra(self):
        """Devuelve True si la ficha está en la barra."""
        return self.__en_barra__

    def esta_en_meta(self):
        """Devuelve True si la ficha ya salió del tablero (meta)."""
        return self.__en_meta__

    def mandar_a_barra(self):
        """Manda la ficha a la barra."""
        self.__en_barra__ = True
        self.__en_meta__ = False

    def sacar_de_barra(self):
        """Saca la ficha de la barra."""
        self.__en_barra__ = False

    def mandar_a_meta(self):
        """Manda la ficha a la meta (fuera del tablero)."""
        self.__en_meta__ = True
        self.__en_barra__ = False