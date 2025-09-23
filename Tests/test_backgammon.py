import unittest
from core.BackgammonGame import BackgammonGame
from core.Checker import Checker

class TestBackgammonGame(unittest.TestCase):
    """
    Tests unitarios para la clase BackgammonGame.
    """

    def setUp(self):
        self.game = BackgammonGame()

    def test_turno_inicial(self):
        """El turno inicial debe ser del jugador 1."""
        self.assertEqual(self.game.turno, 1)

    def test_tirar_dados_normal(self):
        """La tirada de dados devuelve 2 movimientos (o 4 si son dobles)."""
        tirada = self.game.tirar_dados()
        self.assertTrue(all(1 <= d <= 6 for d in tirada))
        self.assertIn(len(tirada), [2, 4])

    def test_cambiar_turno(self):
        """El turno debe cambiar entre jugador 1 y 2, y vaciar movimientos."""
        self.game.tirar_dados()
        self.game.cambiar_turno()
        self.assertEqual(self.game.turno, 2)
        self.assertEqual(self.game.movimientos, [])
        self.game.cambiar_turno()
        self.assertEqual(self.game.turno, 1)

    def test_puede_mover_fuera_de_rango(self):
        """No debe permitir mover si el destino queda fuera del tablero."""
        self.assertFalse(self.game.puede_mover(23, 6))  # jugador 1 → fuera

    def test_mover_valido(self):
        """Debe permitir mover si el movimiento es válido y consumir el dado."""
        self.game.movimientos = [1]
        origen = 0
        destino = 1
        self.assertTrue(self.game.puede_mover(origen, 1))
        self.assertTrue(self.game.mover(origen, 1))
        self.assertEqual(len(self.game.movimientos), 0)
        # ahora debe haber al menos una ficha en la casilla destino
        self.assertGreater(len(self.game.board._Board__positions__[destino]), 0)

    def test_mover_invalido_consumo(self):
        """No debe mover si el paso no está en la lista de movimientos."""
        self.game.movimientos = [3]
        self.assertFalse(self.game.mover(0, 2))
        self.assertEqual(self.game.movimientos, [3])  # no lo consumió

    def test_juego_terminado(self):
        """Debe detectar cuando un jugador metió todas las fichas en home."""
        self.game.board._Board__home__["X"] = [Checker(1) for _ in range(15)]
        self.assertTrue(self.game.esta_terminado())
        self.game.board._Board__home__["X"] = []
        self.assertFalse(self.game.esta_terminado())

    # Tests de integración

    def test_tirar_y_mover_ficha_integra(self):
        """Simula una tirada y un movimiento válido usando el dado tirado."""
        tirada = self.game.tirar_dados()
        paso = tirada[0]
        origen = 0
        destino = paso
        if self.game.puede_mover(origen, paso):
            exito = self.game.mover(origen, paso)
            self.assertTrue(exito)
            self.assertEqual(len(self.game.movimientos), len(tirada) - 1)

    def test_cambiar_turno_y_tirar_dados(self):
        """Verifica que el ciclo de cambiar turno y tirar dados funcione."""
        self.assertEqual(self.game.turno, 1)
        self.game.cambiar_turno()
        self.assertEqual(self.game.turno, 2)
        tirada = self.game.tirar_dados()
        self.assertTrue(all(1 <= d <= 6 for d in tirada))
        self.assertGreater(len(self.game.movimientos), 0)

    def test_estado_juego_no_rompe(self):
        """El método estado_juego debe ejecutarse sin lanzar errores."""
        try:
            self.game.estado_juego()
        except Exception as e:
            self.fail(f"estado_juego lanzó excepción: {e}")

if __name__ == "__main__":
    unittest.main()
