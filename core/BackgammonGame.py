from core.Board import Board
from core.Player import Player
from core.Dice import Dice

class BackgammonGame:
    """
    Clase principal que maneja el flujo general del juego de Backgammon.
    Controla el tablero, los jugadores, los dados y los turnos.
    """

    def __init__(self):
        """
        Inicializa un nuevo juego de Backgammon. 
        Argumentos: - 
        Returns: - 
        Descripcion: Crea el tablero. Define a los dos jugadores (1 y 2). Prepara los dados. Establece el turno inicial en el Jugador 1.
        """
        self.board = Board()
        self.players = [Player(1, "X"), Player(2, "O")]
        self.dice = Dice()
        self.turno = 0  # índice del jugador en self.players

    def get_jugador_actual(self):
        """
        Devuelve el jugador actual según el turno.
        Args: - 
        Returns: Player: instancia del jugador actual.
        """
        return self.players[self.turno]

    def cambiar_turno(self):
        """
        Cambia el turno al otro jugador.
        Args: -
        Returns: - 
        Descripcion: Si el turno es del Jugador 1, pasa al Jugador 2, y viceversa.
        """
        self.turno = 1 - self.turno

    def tirar_dados(self):
        """
        Tira los dados para el jugador actual.
        Args: - 
        Returns: list: valores obtenidos en los dados.
        """
        valores = self.dice.roll()
        print(f"Jugador {self.get_jugador_actual().get_numero()} tiró los dados: {valores}")
        return valores

    def mover_ficha(self, origen, destino):
        """
        Intenta mover una ficha del jugador actual desde una posición a otra.
        Args: origen (int): posición inicial (0 - 23). destino (int): posición destino (0 - 23).
        Returns: bool: True si se pudo mover la ficha, False en caso contrario.

        Description: Lógica inicial, no valida todas las reglas de Backgammon.
        """
        fichas = self.board.get_position(origen)
        if not fichas:
            print("No hay fichas en esa posición.")
            return False

        ficha = self.board.sacar_ficha(origen)
        self.board.añadir_ficha(destino, ficha)
        print(f"Jugador {self.get_jugador_actual().get_numero()} movió ficha de {origen} a {destino}")
        return True

    def estado_juego(self):
        """
        Muestra en consola el estado actual del tablero.
        Args: - 
        Returns: - 
        """
        self.board.display()

    def juego_terminado(self):
        """
        Determina si el juego ha terminado.
        Args: - 
        Returns: bool: False (por ahora siempre devuelve False).
        """
        return False


if __name__ == "__main__":

    juego = BackgammonGame()
    juego.estado_juego()
    
    while not juego.juego_terminado():
        input("Presiona Enter para tirar dados...")
        juego.tirar_dados()
        # Acá se va a pedir origen y destino con input()
        juego.cambiar_turno()
