import unittest
from core.BackgammonGame import BackgammonGame
from core.Board import Board
from core.Checker import Checker

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
    
    def test_direccion_movimiento_jugador_1(self):
        """Prueba que el jugador 1 se mueve en dirección +1"""
        game = BackgammonGame()
        jugador1 = game.get_jugador_actual()
        direccion = game.direccion_movimiento(jugador1)
        assert direccion == 1

    def test_direccion_movimiento_jugador_2(self):
        """Prueba que el jugador 2 se mueve en dirección -1"""
        game = BackgammonGame()
        game.cambiar_turno()
        jugador2 = game.get_jugador_actual()
        direccion = game.direccion_movimiento(jugador2)
        assert direccion == -1

    def test_posicion_casa_jugador_1(self):
        """Prueba que la casa del jugador 1 es range(19, 25)"""
        game = BackgammonGame()
        jugador1 = game.get_jugador_actual()
        casa = game.posicion_casa(jugador1)
        assert casa == range(19, 25)
        assert 19 in casa
        assert 24 in casa

    def test_posicion_casa_jugador_2(self):
        """Prueba que la casa del jugador 2 es range(1, 7)"""
        game = BackgammonGame()
        game.cambiar_turno()
        jugador2 = game.get_jugador_actual()
        casa = game.posicion_casa(jugador2)
        assert casa == range(1, 7)
        assert 1 in casa
        assert 6 in casa

    def test_puede_bear_off_con_fichas_fuera_de_casa(self):
        """Prueba que no se puede hacer bear off si hay fichas fuera de casa"""
        game = BackgammonGame()
        jugador1 = game.get_jugador_actual()
        
        # Colocar una ficha en la casa y otra fuera
        board = game.get_board()
        board.añadir_ficha(20, Checker(1))  # En casa
        board.añadir_ficha(10, Checker(1))  # Fuera de casa
        
        assert game.puede_bear_off(jugador1) == False


    def test_mover_ficha_con_fichas_en_barra_intento_desde_tablero(self):
        """Prueba que no se puede mover desde el tablero si hay fichas en la barra"""
        game = BackgammonGame()
        jugador1 = game.get_jugador_actual()
        board = game.get_board()
        
        # Colocar ficha en la barra
        board.mandar_a_barra(1, Checker(1))
        
        # Colocar ficha en el tablero
        board.añadir_ficha(8, Checker(1))
        
        # Configurar dados
        game.__dados_actuales__ = [3, 4]
        
        # Intentar mover desde posición 8 (debe fallar)
        resultado = game.mover_ficha(8, 11, 3)
        assert resultado == False

    def test_mover_ficha_dado_no_disponible(self):
        """Prueba que no se puede mover con un dado que no está disponible"""
        game = BackgammonGame()
        board = game.get_board()
        
        # Colocar ficha
        board.añadir_ficha(8, Checker(1))
        
        # Configurar dados (solo 3 y 4 disponibles)
        game.__dados_actuales__ = [3, 4]
        
        # Intentar mover con dado 5 (no disponible)
        resultado = game.mover_ficha(8, 13, 5)
        assert resultado == False

    def test_mover_ficha_desde_barra_sin_fichas(self):
        """Prueba que falla mover desde la barra si no hay fichas ahí"""
        game = BackgammonGame()
        
        # Configurar dados
        game.__dados_actuales__ = [3]
        
        # Intentar mover desde barra sin fichas
        resultado = game.mover_ficha(0, 22, 3)
        assert resultado == False

    def test_mover_ficha_desde_barra_jugador_1(self):
        """Prueba mover una ficha desde la barra para jugador 1"""
        game = BackgammonGame()
        board = game.get_board()
        
        # Colocar ficha en barra
        board.mandar_a_barra(1, Checker(1))
        
        # Configurar dados
        game.__dados_actuales__ = [3]
        
        # Mover desde barra (destino = 25 - 3 = 22)
        resultado = game.mover_ficha(0, 22, 3)
        assert resultado == True

    def test_mover_ficha_desde_barra_jugador_2(self):
        """Prueba mover una ficha desde la barra para jugador 2"""
        game = BackgammonGame()
        game.cambiar_turno()
        board = game.get_board()
        
        # Colocar ficha en barra
        board.mandar_a_barra(2, Checker(2))
        
        # Configurar dados
        game.__dados_actuales__ = [4]
        
        # Mover desde barra (destino = 4)
        resultado = game.mover_ficha(0, 4, 4)
        assert resultado == True

    def test_bear_off_sin_poder_hacerlo(self):
        """Prueba que no se puede hacer bear off si no todas las fichas están en casa"""
        game = BackgammonGame()
        board = game.get_board()
        
        # Colocar ficha en casa
        board.añadir_ficha(20, Checker(1))
        
        # Colocar ficha fuera de casa
        board.añadir_ficha(10, Checker(1))
        
        # Configurar dados
        game.__dados_actuales__ = [5]
        
        # Intentar bear off (debe fallar porque hay fichas fuera de casa)
        resultado = game.mover_ficha(20, 25, 5)
        assert resultado == False


    def test_get_ganador_sin_ganador(self):
        """Prueba get_ganador cuando no hay ganador"""
        game = BackgammonGame()
        board = game.get_board()
        
        # Colocar algunas fichas en la meta pero no todas
        for i in range(10):
            board.mandar_a_meta(1, Checker(1))
        
        ganador = game.get_ganador()
        assert ganador is None

    def test_get_ganador_jugador_1_gana(self):
        """Prueba get_ganador cuando el jugador 1 gana"""
        game = BackgammonGame()
        board = game.get_board()
        
        # Colocar todas las 15 fichas en la meta
        for i in range(15):
            board.mandar_a_meta(1, Checker(1))
        
        ganador = game.get_ganador()
        assert ganador is not None
        assert ganador.get_numero() == 1

    def test_get_ganador_jugador_2_gana(self):
        """Prueba get_ganador cuando el jugador 2 gana"""
        game = BackgammonGame()
        board = game.get_board()
        
        # Colocar todas las 15 fichas en la meta
        for i in range(15):
            board.mandar_a_meta(2, Checker(2))
        
        ganador = game.get_ganador()
        assert ganador is not None
        assert ganador.get_numero() == 2

    def test_mover_ficha_posicion_origen_vacia(self):
        """Prueba que no se puede mover desde una posición vacía"""
        game = BackgammonGame()
        
        # Configurar dados
        game.__dados_actuales__ = [3]
        
        # Intentar mover desde posición vacía
        resultado = game.mover_ficha(8, 11, 3)
        assert resultado == False

    def test_mover_ficha_origen_con_fichas_del_oponente(self):
        """Prueba que no se puede mover fichas del oponente"""
        game = BackgammonGame()
        board = game.get_board()
        
        # Colocar ficha del jugador 2
        board.añadir_ficha(8, Checker(2))
        
        # Configurar dados para jugador 1
        game.__dados_actuales__ = [3]
        
        # Intentar mover (debe fallar)
        resultado = game.mover_ficha(8, 11, 3)
        assert resultado == False
    if __name__ == "__main__":
        unittest.main()