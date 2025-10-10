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
        """
        Devuelve el jugador actual según el turno.
        Returns:
            Player: jugador que tiene el turno actual.
        """
        return self.__players__[self.__turno__]

    def cambiar_turno(self):
        """
        Cambia el turno al otro jugador y reinicia los dados.
        """
        self.__turno__ = 1 - self.__turno__
        self.__dados_actuales__ = []
        self.__dados_usados__ = []

    def tirar_dados(self):
        """
        Tira los dados para el jugador actual.
        Returns:
            list[int]: valores obtenidos al tirar los dados.
        """
        valores = self.__dice__.roll()
        self.__dados_actuales__ = self.__dice__.individual_values()
        self.__dados_usados__ = []
        return valores

    def direccion_movimiento(self, jugador: Player) -> int:
        """
        Devuelve la dirección de movimiento de un jugador.
        Args:
            jugador (Player): jugador actual.
        Returns:
            int: +1 si avanza de 1→24, -1 si avanza de 24→1.
        """
        return 1 if jugador.get_numero() == 1 else -1

    def posicion_casa(self, jugador: Player) -> range:
        """
        Devuelve las posiciones de la 'casa' según el jugador.
        Args:
            jugador (Player): jugador actual.
        Returns:
            range: rango de posiciones de la casa.
        """
        return range(19, 25) if jugador.get_numero() == 1 else range(1, 7)

    def puede_bear_off(self, jugador: Player) -> bool:
        """
        Verifica si el jugador puede empezar a sacar fichas (todas en casa).
        Args:
            jugador (Player): jugador actual.
        Returns:
            bool: True si todas las fichas están en casa, False en caso contrario.
        """
        for pos in range(1, 25):
            fichas = self.__board__.get_position(pos)
            if fichas and fichas[-1].get_jugador() == jugador.get_numero():
                if pos not in self.posicion_casa(jugador):
                    return False
        return True

    def mover_ficha(self, origen: int, destino: int, dado: int) -> bool:
        """
        Intenta mover una ficha respetando todas las reglas de Backgammon.
        Args:
            origen (int): posición de origen (1-24, 0=barra).
            destino (int): posición de destino (1-24, 0 o 25=meta).
            dado (int): valor del dado usado para el movimiento.
        Returns:
            bool: True si el movimiento fue válido, False en caso contrario.
        """
        jugador = self.get_jugador_actual()
        num_jugador = jugador.get_numero()

        # Si hay fichas en la barra, debe reingresar primero
        if len(self.__board__.get_bar(num_jugador)) > 0 and origen != 0:
            return False

        # Verificar dado disponible
        if dado not in self.__dados_actuales__:
            return False

        # Movimiento desde barra
        if origen == 0:
            entrada = 25 - dado if num_jugador == 1 else dado
            destino = entrada
            ficha = self.__board__.sacar_de_barra(num_jugador)
            if not ficha:
                return False
        else:
            # Movimiento normal
            fichas = self.__board__.get_position(origen)
            if not fichas or fichas[-1].get_jugador() != num_jugador:
                return False
            ficha = self.__board__.sacar_ficha(origen)

        # Bearing off (sacar ficha del tablero)
        if destino == 25 or destino == 0:
            if not self.puede_bear_off(jugador):
                self.__board__.añadir_ficha(origen, ficha)  # devolver ficha
                return False
            self.__board__.mandar_a_meta(num_jugador, ficha)
        else:
            destino_fichas = self.__board__.get_position(destino)
            if destino_fichas and destino_fichas[-1].get_jugador() != num_jugador:
                if len(destino_fichas) == 1:
                    # Captura
                    capturada = self.__board__.sacar_ficha(destino)
                    self.__board__.mandar_a_barra(3 - num_jugador, capturada)
                else:
                    self.__board__.añadir_ficha(origen, ficha)
                    return False
            self.__board__.añadir_ficha(destino, ficha)

# Marcar dado como usado
        self.__dados_actuales__.remove(dado)
        self.__dados_usados__.append(dado)
        return True

    def juego_terminado(self) -> bool:
        """
        Determina si el juego ha terminado (todas las fichas de un jugador en la meta).
        Returns:
            bool: True si el juego terminó, False en caso contrario.
        """
        for player in self.__players__:
            if len(self.__board__.get_home(player.get_numero())) == 15:
                return True
        return False

    def get_board(self) -> Board:
        """
        Devuelve el tablero actual.
        Returns:
            Board: tablero del juego.
        """
        return self.__board__

    def get_dados_actuales(self) -> list:
        """
        Devuelve los dados disponibles para el turno actual.
        Returns:
            list[int]: valores de los dados.
        """
        return self.__dados_actuales__

    def get_dados_usados(self) -> list:
        """
        Devuelve los dados ya utilizados en el turno actual.
        Returns:
            list[int]: valores de los dados usados.
        """
        return self.__dados_usados__

    def get_ganador(self):
        """
        Devuelve el jugador que ganó la partida, si la condición de victoria se cumplió.
        
        Returns:
            Player | None: jugador ganador si todas sus fichas están en la meta,
            o None si aún no hay un ganador.
        """
        for player in self.__players__:
            if len(self.__board__.get_home(player.get_numero())) == 15:
                return player
        return None