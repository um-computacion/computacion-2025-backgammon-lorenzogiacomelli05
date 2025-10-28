import unittest
from unittest.mock import patch, MagicMock
from CLI.CLI import BackgammonCLI

class TestBackgammonCLI(unittest.TestCase):
    """
    Tests unitarios para la clase BackgammonCLI.
    Se mockea BackgammonGame para evitar dependencias del juego real.
    """

    def setUp(self):
        """Configura una instancia del CLI con un BackgammonGame simulado."""
        patcher = patch("CLI.CLI.BackgammonGame", autospec=True)
        self.addCleanup(patcher.stop)
        MockGame = patcher.start()

        # Mock del juego
        mock_game = MagicMock()
        mock_game.tablero = [[0] * 24, [0] * 24]
        mock_game.jugadores = ["Jugador1", "Jugador2"]
        mock_game.tirar_dados.return_value = [4, 5]
        mock_game.get_dados_actuales.return_value = [4, 5]
        mock_game.get_jugador_actual.return_value = "Jugador1"

        MockGame.return_value = mock_game
        self.cli = BackgammonCLI()

    # ============================
    # Tests básicos
    # ============================

    def test_instancia_cli(self):
        """Debe poder instanciarse correctamente."""
        self.assertIsInstance(self.cli, BackgammonCLI)

    # ============================
    # Métodos de visualización
    # ============================

    def test_mostrar_estado(self):
        """mostrar_estado() no debe lanzar errores."""
        self.cli.mostrar_estado()

    def test_mostrar_ayuda(self):
        """mostrar_ayuda() no debe lanzar errores."""
        self.cli.mostrar_ayuda()

    def test_mostrar_dados(self):
        """mostrar_dados() debe aceptar una lista de valores."""
        self.cli.mostrar_dados([2, 5])

    # ============================
    # Procesamiento de comandos
    # ============================

    def test_comando_ayuda(self):
        """El comando 'ayuda' retorna True."""
        self.assertTrue(self.cli.procesar_comando("ayuda"))

    def test_comando_salir(self):
        """El comando 'salir' retorna False."""
        self.assertFalse(self.cli.procesar_comando("salir"))

    def test_comando_invalido(self):
        """Comando desconocido retorna True."""
        self.assertTrue(self.cli.procesar_comando("comando_invalido"))

    def test_comando_mayusculas(self):
        """'SALIR' funciona igual que 'salir'."""
        self.assertFalse(self.cli.procesar_comando("SALIR"))

    def test_comando_con_espacios(self):
        """Espacios extra no afectan el resultado."""
        self.assertTrue(self.cli.procesar_comando("   comando_invalido   "))

    def test_comando_vacio(self):
        """Comando vacío no lanza errores."""
        self.assertTrue(self.cli.procesar_comando(""))

    def test_comando_none(self):
        """Pasar None lanza excepción."""
        with self.assertRaises(Exception):
            self.cli.procesar_comando(None)

    # ============================
    # Métodos auxiliares
    # ============================

    def test_mostrar_resultado_final(self):
        """mostrar_resultado_final() debe poder ejecutarse sin errores."""
        self.cli.mostrar_resultado_final()

    def test_reiniciar_partida(self):
        """reiniciar_partida() debe ejecutarse sin errores."""
        self.cli.reiniciar_partida()

    def test_reiniciar_partida_multiple(self):
        """reiniciar_partida() puede llamarse varias veces consecutivas."""
        for _ in range(3):
            self.cli.reiniciar_partida()

    def test_mostrar_estado_multiple(self):
        """mostrar_estado() puede llamarse varias veces consecutivas."""
        for _ in range(5):
            self.cli.mostrar_estado()

    # ============================
    # Tests con mocks
    # ============================

    @patch("builtins.input", side_effect=["ayuda", "comando_invalido", "salir"])
    def test_procesar_varios_comandos(self, _):
        """Procesar varios comandos consecutivos no debe fallar."""
        for cmd in ["ayuda", "comando_invalido", "salir"]:
            self.cli.procesar_comando(cmd)

    def test_iniciar_existe(self):
        """Debe existir el método iniciar()."""
        self.assertTrue(hasattr(self.cli, "iniciar"))

if __name__ == "__main__":
    unittest.main()