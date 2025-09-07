import unittest
from core.Checker import Checker

class TestChecker(unittest.TestCase):

    # verifica que get_jugador devuelve el jugador correcto
    def test_get_jugador(self):
        c = Checker(1)
        self.assertEqual(c.get_jugador(), 1)

    # al crear la ficha no está en barra ni en meta
    def test_inicial_no_barra_meta(self):
        c = Checker(2)
        self.assertFalse(c.esta_en_barra())
        self.assertFalse(c.esta_en_meta())

    # probar que mandar_a_barra pone la ficha en barra y no en meta
    def test_mandar_a_barra(self):
        c = Checker(1)
        c.mandar_a_barra()
        self.assertTrue(c.esta_en_barra())
        self.assertFalse(c.esta_en_meta())

    # probar que sacar_de_barra saca la ficha de la barra
    def test_sacar_de_barra(self):
        c = Checker(1)
        c.mandar_a_barra()
        c.sacar_de_barra()
        self.assertFalse(c.esta_en_barra())

    # probar que mandar_a_meta pone la ficha en meta y no en barra
    def test_mandar_a_meta(self):
        c = Checker(2)
        c.mandar_a_meta()
        self.assertTrue(c.esta_en_meta())
        self.assertFalse(c.esta_en_barra())


if __name__ == "__main__":
    unittest.main()
