import unittest
from core.BackgammonGame import BackgammonGame

class TestBackgammonGame(unittest.TestCase):
    """Tests básicos de BackgammonGame - Día 1"""

    def setUp(self):
        """Se crea un nuevo juego antes de cada test"""
        self.juego = BackgammonGame()

    def test_turno_inicial(self):
        """El juego debe iniciar con el turno del jugador 1"""
        jugador = self.juego.get_jugador_actual()
        self.assertEqual(jugador.get_numero(), 1)

    def test_cambiar_turno(self):
        """El turno debe cambiar correctamente entre jugadores"""
        self.juego.cambiar_turno()
        jugador = self.juego.get_jugador_actual()
        self.assertEqual(jugador.get_numero(), 2)

    def test_tirar_dados_devuelve_valores(self):
        """Al tirar los dados deben ser valores entre 1 y 6"""
        valores = self.juego.tirar_dados()
        self.assertTrue(all(1 <= v <= 6 for v in valores))
        self.assertIn(len(valores), [2, 4])  # tirada normal o doble

    def test_direccion_movimiento(self):
        """Cada jugador debe tener dirección correcta"""
        jugador1 = self.juego.get_jugador_actual()
        self.assertEqual(self.juego.direccion_movimiento(jugador1), 1)

        self.juego.cambiar_turno()
        jugador2 = self.juego.get_jugador_actual()
        self.assertEqual(self.juego.direccion_movimiento(jugador2), -1)

    def test_posicion_casa(self):
        """La casa de cada jugador debe estar en el rango correcto"""
        jugador1 = self.juego.get_jugador_actual()
        self.assertEqual(list(self.juego.posicion_casa(jugador1)), list(range(19, 25)))

        self.juego.cambiar_turno()
        jugador2 = self.juego.get_jugador_actual()
        self.assertEqual(list(self.juego.posicion_casa(jugador2)), list(range(1, 7)))


if __name__ == "__main__":
    unittest.main()
