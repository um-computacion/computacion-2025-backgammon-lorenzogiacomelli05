class Checker:
    """
    Representa una ficha individual en el Backgammon.
    Cada ficha pertenece a un jugador y puede estar en la barra o en la meta.
    """

    def __init__(self, jugador: int):
        """
        Inicializa una ficha para un jugador determinado.
        Args:
            jugador (int): 1 o 2, indica el jugador dueño de la ficha.
        """
        if jugador not in (1, 2):
            raise ValueError("El jugador debe ser 1 o 2")
        self.__jugador__ = jugador    # Jugador dueño de la ficha (1 o 2)
        self.__en_barra__ = False     # True si la ficha está en la barra
        self.__en_meta__ = False      # True si la ficha ya salió del tablero

    # --- Getters ---

    def get_jugador(self) -> int:
        """Devuelve el jugador dueño de la ficha."""
        return self.__jugador__

    def esta_en_barra(self) -> bool:
        """Devuelve True si la ficha está en la barra."""
        return self.__en_barra__

    def esta_en_meta(self) -> bool:
        """Devuelve True si la ficha ya salió del tablero (meta)."""
        return self.__en_meta__

    def esta_en_tablero(self) -> bool:
        """Devuelve True si la ficha sigue en el tablero."""
        return not self.__en_barra__ and not self.__en_meta__

    # --- Cambios de estado ---

    def mandar_a_barra(self) -> None:
        """Manda la ficha a la barra."""
        self.__en_barra__ = True
        self.__en_meta__ = False

    def sacar_de_barra(self) -> None:
        """Saca la ficha de la barra y la devuelve al tablero."""
        self.__en_barra__ = False

    def mandar_a_meta(self) -> None:
        """Manda la ficha a la meta (fuera del tablero)."""
        self.__en_meta__ = True
        self.__en_barra__ = False

    # --- Representación ---
    
    def __repr__(self):
        if self.__en_barra__:
            estado = "barra"
        elif self.__en_meta__:
            estado = "meta"
        else:
            estado = "tablero"
        return f"<Checker jugador={self.__jugador__}, estado={estado}>"
