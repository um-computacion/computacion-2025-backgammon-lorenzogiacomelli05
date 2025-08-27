#Primeros tests 
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

if __name__ == "__main__":
    unittest.main()
