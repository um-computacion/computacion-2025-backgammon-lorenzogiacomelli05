from core.Board import Board
from core.Player import Player
from core.Dice import Dice

class BackgammonGame:
    """
    Clase principal que maneja el flujo completo del juego de Backgammon.
    Coordina tablero, jugadores, dados, turnos y reglas.
    """

    def __init__(self):
        """
        Inicializa un nuevo juego de Backgammon.
        """
        self.__board__ = Board()
        self.__players__ = [Player(1, "X"), Player(2, "O")]
        self.__dice__ = Dice()
        self.__turno__ = 0
        self.__dados_actuales__ = []
        self.__dados_usados__ = []

    def get_jugador_actual(self):
        """Devuelve el jugador actual según el turno."""
        return self.__players__[self.__turno__]

    def cambiar_turno(self):
        """Cambia el turno al otro jugador y reinicia los dados."""
        self.__turno__ = 1 - self.__turno__
        self.__dados_actuales__ = []
        self.__dados_usados__ = []

    def tirar_dados(self):
        """Tira los dados para el jugador actual."""
        valores = self.__dice__.roll()
        self.__dados_actuales__ = self.__dice__.individual_values()
        self.__dados_usados__ = []
        print(f"Jugador {self.get_jugador_actual().get_numero()} tiró: {valores}")
        return valores

    def direccion_movimiento(self, jugador):
        """Devuelve +1 si el jugador avanza de 1→24 o -1 si avanza 24→1."""
        return 1 if jugador.get_numero() == 1 else -1

    def posicion_casa(self, jugador):
        """Devuelve las posiciones de la 'casa' según el jugador."""
        return range(19, 25) if jugador.get_numero() == 1 else range(1, 7)

    def puede_bear_off(self, jugador):
        """Verifica si el jugador puede empezar a sacar fichas (todas en casa)."""
        for pos in range(1, 25):
            fichas = self.__board__.get_position(pos)
            if fichas and fichas[-1].get_jugador() == jugador.get_numero():
                if pos not in self.posicion_casa(jugador):
                    return False
        return True

    def mover_ficha(self, origen: int, destino: int, dado: int):
        """
        Intenta mover una ficha respetando todas las reglas de Backgammon.
        """
        jugador = self.get_jugador_actual()
        num_jugador = jugador.get_numero()
        direccion = self.direccion_movimiento(jugador)

        # Si hay fichas en la barra, debe reingresar primero
        if len(self.__board__.get_bar(num_jugador)) > 0 and origen != 0:
            print("Debes reingresar desde la barra primero.")
            return False

        # Verificar dado disponible
        if dado not in self.__dados_actuales__:
            print("Ese dado no está disponible.")
            return False

        # Movimiento desde barra
        if origen == 0:
            entrada = 25 - dado if num_jugador == 1 else dado
            destino = entrada
            ficha = self.__board__.sacar_de_barra(num_jugador)
            if not ficha:
                print("No hay fichas en la barra.")
                return False
        else:
            # Movimiento normal
            fichas = self.__board__.get_position(origen)
            if not fichas or fichas[-1].get_jugador() != num_jugador:
                print("Movimiento ilegal.")
                return False
            ficha = self.__board__.sacar_ficha(origen)

        # Bearing off (sacar ficha del tablero)
        if destino == 25 or destino == 0:
            if not self.puede_bear_off(jugador):
                print("No puedes sacar fichas aún.")
                self.__board__.añadir_ficha(origen, ficha)  # devolver
                return False
            self.__board__.mandar_a_meta(num_jugador, ficha)
            print(f"Jugador {num_jugador} sacó una ficha de {origen}.")
        else:
            destino_fichas = self.__board__.get_position(destino)
            if destino_fichas and destino_fichas[-1].get_jugador() != num_jugador:
                if len(destino_fichas) == 1:
                    # Captura
                    capturada = self.__board__.sacar_ficha(destino)
                    self.__board__.mandar_a_barra(3 - num_jugador, capturada)
                    print(f"Jugador {num_jugador} capturó una ficha en {destino}.")
                else:
                    print("Destino bloqueado.")
                    self.__board__.añadir_ficha(origen, ficha)
                    return False
            self.__board__.añadir_ficha(destino, ficha)
            print(f"Jugador {num_jugador} movió ficha de {origen} a {destino}.")

        # Marcar dado como usado
        self.__dados_actuales__.remove(dado)
        self.__dados_usados__.append(dado)
        return True

    def estado_juego(self):
        """Muestra en consola el estado actual del tablero."""
        self.__board__.display()

    def juego_terminado(self):
        """Determina si el juego ha terminado (todas fichas en meta)."""
        for player in self.__players__:
            if len(self.__board__.get_home(player.get_numero())) == 15:
                print(f"¡Jugador {player.get_numero()} ({player.get_ficha()}) ganó!")
                return True
        return False

    def jugar_turno(self):
        """
        Maneja un turno completo del jugador actual.
        """
        jugador = self.get_jugador_actual()
        print(f"\nTurno del Jugador {jugador.get_numero()} ({jugador.get_ficha()})")
        self.tirar_dados()

        while self.__dados_actuales__:
            try:
                origen = int(input("Origen (1-24, 0=barra): "))
                destino = int(input("Destino (1-24, 0/25=meta): "))
                dado = int(input(f"Elige dado {self.__dados_actuales__}: "))
                self.mover_ficha(origen, destino, dado)
            except ValueError:
                print("Entrada inválida, intenta de nuevo.")
            self.estado_juego()

        self.cambiar_turno()

if __name__ == "__main__":
    juego = BackgammonGame()
    juego.estado_juego()
    while not juego.juego_terminado():
        juego.jugar_turno()
