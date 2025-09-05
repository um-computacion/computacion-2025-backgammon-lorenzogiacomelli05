import unittest
from core.Player import Player

class TestJugador(unittest.TestCase):

    def test_get_numero(self):
        # Verifica que devuelva correctamente el número del jugador
        j = Player(1, "X")
        self.assertEqual(j.get_numero(), 1)

    def test_get_ficha(self):
        # Verifica que devuelva correctamente la ficha del jugador
        j = Player(2, "O")
        self.assertEqual(j.get_ficha(), "O")

if __name__ == "__main__":
    unittest.main()
