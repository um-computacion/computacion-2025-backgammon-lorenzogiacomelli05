1. PROMPT PARA AYUDA CON CREACIÓN DE TABLERO EN BOARD:
- Herramienta: GPT-5
- Prompt: Necesito que me expliques cómo puedo crear mi tablero, respetando la disposición inicial cuando empieza la partida de Backgammon.
- Respuesta: 
self.__positions__ = [[] for _ in range(25)]  # índices 1 - 24 
self.__bar__ = {1: [], 2: []}    # fichas en la barra por jugador 
self.__home__ = {1: [], 2: []}   # fichas en la meta por jugador

- Dejé igual en mi clase Board, luego lo integré con Checker y quedó el tablero final (core/Board.py). 

2. PROMPT PARA CLASE DICE (método roll, import random, etc):
- Herramienta: GPT-5
- Prompt: Necesito crear la clase de los dados, para poder tirarlos y que devuelva resultados aleatorios de los números 1 a 6. Necesito que esté la posibilidad de los dados dobles como en Backgammon, osea que si dos dados salen repetidos, que devuelva 4 valores. 
- Respuesta: 
import random

class Dice:

    def __init__(self):

        self.__valores__ = []
        self.__usados__ = []

    def roll(self):

        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        if d1 == d2:
            self.__valores__ = [d1, d1, d2, d2]
        else:
            self.__valores__ = [d1, d2]

        self.__usados__ = []
        return self.__valores__

- Acá se dejó igual en la clase Dice (core/Dice.py)

3. PROMPT PARA VALIDACIONES DE CHECKER.
- Herramienta: GPT-5
- Prompt: Necesito que me crees las validaciones para saber dónde esta la ficha en mi clase Checker. Añadile docstrings explicativos. 
- Respuesta:    
    def esta_en_barra(self) -> bool:
        """Devuelve True si la ficha está en la barra."""
        return self.__en_barra__

    def esta_en_meta(self) -> bool:
        """Devuelve True si la ficha ya salió del tablero (meta)."""
        return self.__en_meta__

    def esta_en_tablero(self) -> bool:
        """Devuelve True si la ficha sigue en el tablero."""
        return not self.__en_barra__ and not self.__en_meta__

- Se dejó igual (core/Checker.py)

4. PROMPT PARA FUNCIÓN mover_ficha
- Herramienta: GPT-5
- Prompt: Necesito que me crees una funcion para mover una ficha en el tablero, cumpliendo todas las reglas de backgammon reales. Añadi docstrings y comentarios explicativos.
- Respuesta: 
    def mover_ficha(self, origen: int, destino: int, dado: int) -> bool:
        """
        Intenta mover una ficha respetando todas las reglas de Backgammon.
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

- Se dejó igual (core/BackgammonGame.py)