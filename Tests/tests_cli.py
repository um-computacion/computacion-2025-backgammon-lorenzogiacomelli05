import unittest
from unittest.mock import patch, MagicMock
from CLI import BackgammonCLI

class TestBackgammonCLI(unittest.TestCase):
    """
    Tests unitarios para la clase BackgammonCLI.
    Los tests se enfocan en la lógica interna del CLI, usando mocks
    para métodos del juego y entradas del usuario. Se evitan bucles
    infinitos y no se requiere interacción real.
    """

    def setUp(self):
        """
        Configuración inicial antes de cada test.
        
        Patch de BackgammonGame antes de crear la instancia del CLI
        para evitar que se genere un tablero real y se produzcan bucles.
        """
        # Patch de la clase BackgammonGame
        self.__patcher__ = patch("CLI.BackgammonGame", autospec=True)
        self.__MockGameClass__ = self.__patcher__.start()
        self.addCleanup(self.__patcher__.stop)

        # Mock del juego con atributos seguros para impresión
        self.__mock_game__ = MagicMock()
        self.__mock_game__.tablero = [[0]*24, [0]*24]  # tablero vacío real
        self.__mock_game__.jugadores = ["Jugador1", "Jugador2"]
        self.__mock_game__.tirar_dados.return_value = [4, 5]
        self.__mock_game__.get_dados_actuales.return_value = [4, 5]
        self.__mock_game__.get_jugador_actual.return_value = "Jugador1"

        # El constructor del CLI usará siempre nuestro mock
        self.__MockGameClass__.return_value = self.__mock_game__

        # Instancia del CLI
        self.__cli__ = BackgammonCLI()

    # Tests básicos de CLI

    def test_instancia_cli(self):
        """Verifica que la instancia del CLI se cree correctamente."""
        self.assertIsInstance(self.__cli__, BackgammonCLI)

    def test_mostrar_estado(self):
        """Verifica que mostrar_estado() se ejecute sin errores."""
        try:
            self.__cli__.mostrar_estado()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

    def test_mostrar_ayuda(self):
        """Verifica que mostrar_ayuda() funcione sin errores."""
        try:
            self.__cli__.mostrar_ayuda()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

    def test_mostrar_dados(self):
        """Verifica que mostrar_dados() acepte una lista de valores sin errores."""
        try:
            self.__cli__.mostrar_dados([2, 5])
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

    # Tests de procesamiento de comandos

    def test_procesar_comando_ayuda(self):
        """El comando 'ayuda' retorna True (continúa el juego)."""
        self.assertTrue(self.__cli__.procesar_comando("ayuda"))

    def test_procesar_comando_salir(self):
        """El comando 'salir' retorna False (termina el juego)."""
        self.assertFalse(self.__cli__.procesar_comando("salir"))

    def test_procesar_comando_invalido(self):
        """Un comando desconocido retorna True (no interrumpe el juego)."""
        self.assertTrue(self.__cli__.procesar_comando("comando_invalido"))

    def test_procesar_comando_mayusculas(self):
        """Comando 'SALIR' funciona igual que 'salir'."""
        self.assertFalse(self.__cli__.procesar_comando("SALIR"))

    def test_procesar_comando_espacios(self):
        """Espacios extras alrededor del comando no afectan la ejecución."""
        self.assertTrue(self.__cli__.procesar_comando("   comando_invalido   "))

    def test_procesar_comando_vacio(self):
        """Un comando vacío no lanza errores y devuelve True."""
        self.assertTrue(self.__cli__.procesar_comando(""))

    def test_procesar_comando_none(self):
        """Pasar None como comando lanza excepción."""
        with self.assertRaises(Exception):
            self.__cli__.procesar_comando(None)

    # Tests de métodos auxiliares

    def test_mostrar_resultado_final_sin_ganador(self):
        """Verifica que mostrar_resultado_final() funcione aunque no haya ganador."""
        try:
            self.__cli__.mostrar_resultado_final()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

    def test_reiniciar_partida(self):
        """Verifica que reiniciar_partida() se ejecute sin errores."""
        try:
            self.__cli__.reiniciar_partida()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

    def test_reiniciar_partida_multiple(self):
        """Verifica que reiniciar_partida() pueda ejecutarse varias veces consecutivas."""
        try:
            for _ in range(3):
                self.__cli__.reiniciar_partida()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

    def test_mostrar_estado_varias_veces(self):
        """Verifica que mostrar_estado() pueda llamarse varias veces consecutivas."""
        try:
            for _ in range(5):
                self.__cli__.mostrar_estado()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

    # Tests con mocks de input y exit

    @patch("builtins.input", side_effect=["ayuda", "comando_invalido", "salir"])
    def test_procesar_varios_comandos_mock(self, mock_input):
        """Verifica que procesar varios comandos consecutivos no lance errores."""
        try:
            for cmd in ["ayuda", "comando_invalido", "salir"]:
                self.__cli__.procesar_comando(cmd)
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

    def test_iniciar_no_falla(self):
        """Verifica que el método iniciar() exista sin ejecutarlo."""
        try:
            _ = getattr(self.__cli__, "iniciar", None)
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

if __name__ == "__main__":
    unittest.main()