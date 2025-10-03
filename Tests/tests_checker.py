import unittest
from core.Checker import Checker

class TestChecker(unittest.TestCase):
    """
    Tests unitarios para la clase Checker.
    Verifican que una ficha (Checker) cumpla con sus responsabilidades:
    pertenencia a un jugador y control de estado (barra/meta).
    """

    def setUp(self):
        """Se crea una ficha de ejemplo antes de cada test."""
        self.ficha = Checker(1)  # ficha del jugador 1

    def test_jugador_asignado_correctamente(self):
        """La ficha debe recordar a qué jugador pertenece."""
        self.assertEqual(self.ficha.get_jugador(), 1)

    def test_estado_inicial(self):
        """Al crearse, la ficha no debe estar ni en barra ni en meta."""
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())

    def test_mandar_a_barra(self):
        """La ficha puede enviarse a la barra."""
        self.ficha.mandar_a_barra()
        self.assertTrue(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())

    def test_sacar_de_barra(self):
        """Una ficha en la barra puede salir de ella."""
        self.ficha.mandar_a_barra()
        self.ficha.sacar_de_barra()
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())

    def test_mandar_a_meta(self):
        """La ficha puede moverse a la meta (fuera del tablero)."""
        self.ficha.mandar_a_meta()
        self.assertTrue(self.ficha.esta_en_meta())
        self.assertFalse(self.ficha.esta_en_barra())

    def test_cambio_estado_barra_a_meta(self):
        """Si una ficha estaba en barra y va a meta, debe resetear barra."""
        self.ficha.mandar_a_barra()
        self.ficha.mandar_a_meta()
        self.assertTrue(self.ficha.esta_en_meta())
        self.assertFalse(self.ficha.esta_en_barra())

    def test_cambio_estado_meta_a_barra(self):
        """Si una ficha estaba en meta y vuelve a barra, debe resetear meta."""
        self.ficha.mandar_a_meta()
        self.ficha.mandar_a_barra()
        self.assertTrue(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())


if __name__ == "__main__":
    unittest.main()
