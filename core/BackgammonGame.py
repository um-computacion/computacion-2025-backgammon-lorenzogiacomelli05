from core.Board import Board
from core.Player import Player
from core.Dice import Dice

class BackgammonGame:
    """
    Clase principal que maneja el flujo general del juego de Backgammon.
    Coordina el tablero, los jugadores, los dados y los turnos.
    """

    def __init__(self):
        """
        Inicializa un nuevo juego de Backgammon. 
        """
        self.__board__ = Board()
        self.__players__ = [Player(1, "X"), Player(2, "O")]
        self.__dice__ = Dice()
        self.__turno__ = 0              # índice del jugador en __players__
        self.__dados_actuales__ = []    # valores de la tirada actual

    def get_jugador_actual(self):
        """
        Devuelve el jugador actual según el turno.
        """
        return self.__players__[self.__turno__]

    def cambiar_turno(self):
        """
        Cambia el turno al otro jugador.
        """
        self.__turno__ = 1 - self.__turno__
        self.__dados_actuales__ = []

    def tirar_dados(self):
        """
        Tira los dados para el jugador actual.
        """
        valores = self.__dice__.roll()
        self.__dados_actuales__ = valores
        print(f"Jugador {self.get_jugador_actual().get_numero()} tiró los dados: {valores}")
        return valores

    def mover_ficha(self, origen, destino):
        """
        Intenta mover una ficha del jugador actual desde una posición a otra.
        """
        fichas = self.__board__.get_position(origen)
        if not fichas:
            print("No hay fichas en esa posición.")
            return False

        jugador_actual = self.get_jugador_actual()

        # La ficha que se mueve es la última de la pila (tope)
        ficha = fichas[-1]

        if ficha.get_jugador() != jugador_actual.get_numero():
            print("Esa ficha no es tuya.")
            return False

        # Sacar la ficha del origen y añadirla al destino
        ficha_movida = self.__board__.sacar_ficha(origen)
        self.__board__.añadir_ficha(destino, ficha_movida)
        print(f"Jugador {jugador_actual.get_numero()} movió ficha de {origen} a {destino}")
        return True

    def estado_juego(self):
        """
        Muestra en consola el estado actual del tablero.
        """
        self.__board__.display()

    def juego_terminado(self):
        """
        Determina si el juego ha terminado.
        """
        for player in self.__players__:
            fichas_en_tablero = sum(
                len(self.__board__.get_position(pos)) 
                for pos in range(1, 25)
                if self.__board__.get_position(pos) 
                and self.__board__.get_position(pos)[-1].get_jugador() == player.get_numero()
            )
            if fichas_en_tablero == 0:
                print(f"¡Jugador {player.get_numero()} ({player.get_ficha()}) ganó el juego!")
                return True
        return False

    def jugar_turno(self):
        """
        Maneja el turno completo de un jugador.
        """
        jugador = self.get_jugador_actual()
        print(f"\nTurno del Jugador {jugador.get_numero()} ({jugador.get_ficha()})")

        # Tirar dados
        self.tirar_dados()

        try:
            origen = int(input("Elige la posición de origen (1-24): "))
            destino = int(input("Elige la posición de destino (1-24): "))
            self.mover_ficha(origen, destino)
        except ValueError:
            print("Entrada inválida, turno perdido.")

        self.estado_juego()
        self.cambiar_turno()


if __name__ == "__main__":
    juego = BackgammonGame()
    juego.estado_juego()

    while not juego.juego_terminado():
        juego.jugar_turno()