import unittest
from unittest.mock import patch, MagicMock
from CLI.CLI import BackgammonCLI

class TestBackgammonCLI(unittest.TestCase):
    """Tests unitarios para la clase BackgammonCLI con mocks completos."""

    def setUp(self):
        """Crea la instancia del CLI y mockea el juego interno."""
        self.cli = BackgammonCLI()
        self.cli.__game__ = MagicMock()

    # ======================
    # TESTS DE INTERFAZ
    # ======================

    @patch("builtins.print")
    def test_mostrar_estado(self, mock_print):
        board_mock = MagicMock()
        self.cli.__game__.get_board.return_value = board_mock
        self.cli.mostrar_estado()
        board_mock.display.assert_called_once()
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_mostrar_ayuda(self, mock_print):
        self.cli.mostrar_ayuda()
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_mostrar_resultado_final_con_ganador(self, mock_print):
        ganador = MagicMock()
        ganador.get_numero.return_value = 1
        ganador.get_ficha.return_value = "X"
        self.cli.__game__.get_ganador.return_value = ganador
        self.cli.mostrar_resultado_final()
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_mostrar_resultado_final_sin_ganador(self, mock_print):
        self.cli.__game__.get_ganador.return_value = None
        self.cli.mostrar_resultado_final()
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_mostrar_dados(self, mock_print):
        self.cli.mostrar_dados([3,5])
        mock_print.assert_called_once()

    @patch("builtins.input", return_value="2")
    @patch("builtins.print")
    def test_mostrar_menu_principal(self, mock_print, mock_input):
        result = self.cli.mostrar_menu_principal()
        self.assertEqual(result, "2")

    # ======================
    # TESTS DE COMANDOS
    # ======================

    @patch("builtins.print")
    def test_procesar_comando_salir(self, mock_print):
        self.assertFalse(self.cli.procesar_comando("salir"))
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_procesar_comando_ayuda(self, mock_print):
        self.assertTrue(self.cli.procesar_comando("ayuda"))
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_procesar_comando_tablero(self, mock_print):
        self.assertTrue(self.cli.procesar_comando("tablero"))
        self.assertTrue(mock_print.called)

    def test_procesar_comando_otro(self):
        self.assertTrue(self.cli.procesar_comando("algo"))

    # ======================
    # TESTS DE JUEGO
    # ======================

    @patch("builtins.print")
    def test_reiniciar_partida(self, mock_print):
        self.cli.mostrar_estado = MagicMock()
        self.cli.reiniciar_partida()
        self.cli.mostrar_estado.assert_called_once()
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_iniciar_opciones(self, mock_print):
        """Prueba todas las opciones principales del menú con mocks."""
        self.cli.mostrar_menu_principal = MagicMock(side_effect=["2", "3", "1", "4"])
        self.cli.mostrar_ayuda = MagicMock()
        self.cli.reiniciar_partida = MagicMock()
        self.cli.mostrar_estado = MagicMock()
        self.cli.ejecutar_turno = MagicMock()
        self.cli.__game__.juego_terminado.side_effect = [False, True]
        self.cli.mostrar_resultado_final = MagicMock()

        self.cli.iniciar()

        self.cli.mostrar_ayuda.assert_called_once()
        self.cli.reiniciar_partida.assert_called_once()
        self.cli.mostrar_estado.assert_called()
        self.cli.ejecutar_turno.assert_called()
        self.cli.mostrar_resultado_final.assert_called_once()
        mock_print.assert_any_call("Gracias por jugar al Backgammon.")

    # ======================
    # TESTS DE TURNOS
    # ======================

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["1","6","3",""])
    def test_turno_valido(self, mock_input, mock_print):
        juego = self.cli.__game__
        jugador = MagicMock()
        jugador.get_numero.return_value = 1
        jugador.get_ficha.return_value = "X"
        juego.get_jugador_actual.return_value = jugador
        juego.tirar_dados.return_value = [3,5]
        juego.get_dados_actuales.side_effect = [[3,5], [5], []]
        juego.mover_ficha.return_value = True
        juego.juego_terminado.return_value = False

        self.cli.ejecutar_turno()

        juego.tirar_dados.assert_called_once()
        juego.mover_ficha.assert_called_with(1,6,3)
        juego.cambiar_turno.assert_called_once()
        mock_print.assert_any_call("Movimiento realizado correctamente.")

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["salir"])
    def test_turno_salir(self, mock_input, mock_print):
        juego = self.cli.__game__
        jugador = MagicMock()
        jugador.get_numero.return_value = 2
        jugador.get_ficha.return_value = "O"
        juego.get_jugador_actual.return_value = jugador
        juego.tirar_dados.return_value = [2,3]
        juego.get_dados_actuales.return_value = [2,3]

        with self.assertRaises(SystemExit):
            self.cli.ejecutar_turno()
        mock_print.assert_any_call("\nJuego interrumpido por el usuario.")

if __name__ == "__main__":
    unittest.main()
