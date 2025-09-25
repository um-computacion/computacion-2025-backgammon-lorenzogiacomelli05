import unittest
from core.Player import Player

class TestPlayer(unittest.TestCase):
    """
    Tests unitarios para la clase Player.
    Se validan las operaciones principales de la clase.
    """

    def setUp(self):
        """Crea dos jugadores de ejemplo para las pruebas."""
        self.player1 = Player(1, "X")
        self.player2 = Player(2, "O")

    def test_get_numero(self):
        """Debe devolver el número correcto del jugador."""
        self.assertEqual(self.player1.get_numero(), 1)
        self.assertEqual(self.player2.get_numero(), 2)

    def test_get_ficha(self):
        """Debe devolver el símbolo de ficha correcto del jugador."""
        self.assertEqual(self.player1.get_ficha(), "X")
        self.assertEqual(self.player2.get_ficha(), "O")

    def test_jugadores_distintos(self):
        """Dos jugadores distintos deben tener diferente número y ficha."""
        self.assertFalse(self.player1.get_numero() == self.player2.get_numero())
        self.assertFalse(self.player1.get_ficha() == self.player2.get_ficha())

    def test_reutilizacion_numero_y_ficha(self):
        """
        Un jugador debe mantener el mismo número y ficha
        durante toda su vida útil.
        """
        numero_inicial = self.player1.get_numero()
        ficha_inicial = self.player1.get_ficha()

        # Se consulta varias veces para confirmar consistencia
        self.assertEqual(self.player1.get_numero(), numero_inicial)
        self.assertEqual(self.player1.get_ficha(), ficha_inicial)
        self.assertEqual(self.player1.get_numero(), 1)
        self.assertEqual(self.player1.get_ficha(), "X")

if __name__ == "__main__":
    unittest.main()

