import unittest
from core import Dice 

class TestDice(unittest.TestCase):

    def test_roll_devuelve_lista(self):
        # Al tirar los dados devuelve una lista con 2 o 4 valores
        d = Dice()
        valores = d.roll()
        largo = len(valores)
        self.assertTrue(largo == 2 or largo == 4)

    def test_get_values(self):
        # get_values devuelve lo mismo que los valores guardados
        d = Dice()
        d.roll()
        valores = d.get_values()
        self.assertEqual(valores, d._Dice__valores__)

    def test_tirada_doble(self):
        # si hay 4 valores iguales debería ser una tirada doble
        d = Dice()
        d._Dice__valores__ = [4, 4, 4, 4]
        self.assertTrue(d.tirada_doble())
        # si hay solo 2 valores distintos, no es doble
        d._Dice__valores__ = [3, 5]
        self.assertFalse(d.tirada_doble())

    def test_individual_values(self):
        # si es doble tiene que devolver solo 2 valores (ej: [6, 6])
        d = Dice()
        d._Dice__valores__ = [6, 6, 6, 6]
        self.assertEqual(d.individual_values(), [6, 6])
        # si no es doble devuelve los valores normales
        d._Dice__valores__ = [2, 5]
        self.assertEqual(d.individual_values(), [2, 5])

    def test_usar_valor(self):
        # probar que al usar un valor se pasa a la lista de usados
        d = Dice()
        d._Dice__valores__ = [2, 5]
        usado = d.usar_valor(2)
        self.assertTrue(usado)
        self.assertTrue(2 in d._Dice__usados__)
        self.assertFalse(2 in d._Dice__valores__)

    def test_valores_usados(self):
        # al usar un valor debería aparecer en la lista de usados
        d = Dice()
        d._Dice__valores__ = [3, 4]
        d.usar_valor(3)
        self.assertEqual(d.valores_usados(), [3])

if __name__ == "__main__":
    unittest.main()
