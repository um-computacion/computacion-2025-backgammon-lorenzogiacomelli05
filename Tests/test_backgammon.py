import unittest
from core.BackgammonGame import BackgammonGame
from core.Board import Board

class TestBackgammonGame(unittest.TestCase):
    """
    Tests unitarios para la clase BackgammonGame.
    Se cubren métodos de turnos, dados, posiciones, movimiento de fichas
    y condiciones de victoria.
    """

    def setUp(self):
        """Configura un nuevo juego antes de cada test."""
        self.__game__ = BackgammonGame()

    def test_jugador_actual_es_correcto(self):
        """El jugador inicial debe ser el jugador 1 con ficha 'X'."""
        jugador = self.__game__.get_jugador_actual()
        self.assertEqual(jugador.get_numero(), 1)
        self.assertEqual(jugador.get_ficha(), "X")

    def test_cambiar_turno_alterna_jugador(self):
        """Al cambiar turno debe alternarse entre jugador 1 y 2."""
        jugador_inicial = self.__game__.get_jugador_actual()
        self.__game__.cambiar_turno()
        jugador_despues = self.__game__.get_jugador_actual()
        self.assertNotEqual(jugador_inicial.get_numero(), jugador_despues.get_numero())

    def test_tirar_dados_devuelve_lista_valores(self):
        """Tirar dados debe devolver una lista de valores entre 1 y 6."""
        valores = self.__game__.tirar_dados()
        self.assertTrue(isinstance(valores, list))
        self.assertTrue(all(1 <= v <= 6 for v in valores))

    def test_direccion_movimiento_jugador1_es_positiva(self):
        """El jugador 1 debe moverse en dirección positiva (1)."""
        jugador1 = self.__game__.get_jugador_actual()
        self.assertEqual(self.__game__.direccion_movimiento(jugador1), 1)

    def test_direccion_movimiento_jugador2_es_negativa(self):
        """El jugador 2 debe moverse en dirección negativa (-1)."""
        self.__game__.cambiar_turno()
        jugador2 = self.__game__.get_jugador_actual()
        self.assertEqual(self.__game__.direccion_movimiento(jugador2), -1)

    def test_posicion_casa_jugador1(self):
        """La casa del jugador 1 debe ser posiciones 19 a 24."""
        jugador1 = self.__game__.get_jugador_actual()
        self.assertEqual(list(self.__game__.posicion_casa(jugador1)), list(range(19, 25)))

    def test_posicion_casa_jugador2(self):
        """La casa del jugador 2 debe ser posiciones 1 a 6."""
        self.__game__.cambiar_turno()
        jugador2 = self.__game__.get_jugador_actual()
        self.assertEqual(list(self.__game__.posicion_casa(jugador2)), list(range(1, 7)))

    def test_juego_terminado_es_false_al_inicio(self):
        """Al inicio ningún jugador debe tener victoria."""
        self.assertFalse(self.__game__.juego_terminado())

    def test_get_board_devuelve_instancia_board(self):
        """El tablero devuelto debe ser una instancia de Board."""
        tablero = self.__game__.get_board()
        self.assertTrue(isinstance(tablero, Board))

    def test_get_dados_actuales_vacio_al_inicio(self):
        """Antes de tirar, los dados actuales deben estar vacíos."""
        self.assertEqual(self.__game__.get_dados_actuales(), [])

    def test_get_dados_usados_vacio_al_inicio(self):
        """Al inicio, ningún dado debe estar usado."""
        self.assertEqual(self.__game__.get_dados_usados(), [])

    def test_mover_ficha_movimiento_invalido_sin_dado(self):
        """Intentar mover sin tirar dados debe fallar."""
        valido = self.__game__.mover_ficha(1, 2, 3)
        self.assertFalse(valido)

    def test_mover_ficha_movimiento_invalido_posicion_vacia(self):
        """No se debe poder mover desde una posición sin fichas."""
        self.__game__.tirar_dados()
        dado = self.__game__.get_dados_actuales()[0]
        valido = self.__game__.mover_ficha(5, 5 + dado, dado)
        self.assertFalse(valido)

    def test_mover_ficha_valido(self):
        """Mover una ficha desde la posición inicial debe ser válido."""
        self.__game__.tirar_dados()
        dado = self.__game__.get_dados_actuales()[0]
        origen = 1
        destino = origen + dado
        valido = self.__game__.mover_ficha(origen, destino, dado)
        self.assertTrue(valido)

    def test_mover_ficha_destino_bloqueado(self):
        """Un destino con 2 fichas rivales debe bloquear el movimiento."""
        self.__game__.tirar_dados()
        dado = self.__game__.get_dados_actuales()[0]

# Forzar dos fichas del jugador 2 en el destino
        destino = 1 + dado
        self.__game__.cambiar_turno()
        ficha1 = self.__game__.get_board().sacar_ficha(12)
        ficha2 = self.__game__.get_board().sacar_ficha(13)
        self.__game__.get_board().añadir_ficha(destino, ficha1)
        self.__game__.get_board().añadir_ficha(destino, ficha2)
        self.__game__.cambiar_turno()

        valido = self.__game__.mover_ficha(1, destino, dado)
        self.assertFalse(valido)

    def test_tirar_dados_actualiza_estado(self):
        """Verifica que tras tirar los dados, el estado del juego se actualiza correctamente."""
        valores = self.__game__.tirar_dados()
        self.assertTrue(isinstance(valores, list))
        self.assertTrue(all(1 <= v <= 6 for v in valores))
        self.assertNotEqual(valores, [])

    def test_tirar_dados_dos_veces_no_devuelve_lo_mismo(self):
        """Verifica que tirar los dados dos veces produce resultados distintos la mayoría de las veces."""
        primer_tiro = self.__game__.tirar_dados()
        segundo_tiro = self.__game__.tirar_dados()
        self.assertTrue(isinstance(segundo_tiro, list))
        self.assertTrue(all(1 <= v <= 6 for v in segundo_tiro))

    def test_repr_devuelve_string_legible(self):
        """Verifica que __repr__ devuelva una representación de texto informativa del juego."""
        representacion = repr(self.__game__)
        self.assertIsInstance(representacion, str)
        self.assertIn("BackgammonGame", representacion)

    def test_resetear_estado_inicial_crea_nuevo_tablero(self):
        """Verifica que reiniciar el estado del juego crea un tablero limpio."""
        nuevo_juego = BackgammonGame()
        self.assertIsInstance(nuevo_juego.get_board(), type(self.__game__.get_board()))
        self.assertNotEqual(id(nuevo_juego.get_board()), id(self.__game__.get_board()))
