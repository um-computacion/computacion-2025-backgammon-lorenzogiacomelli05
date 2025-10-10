import unittest
from core.Dice import Dice

class TestDice(unittest.TestCase):
    """
    Tests unitarios para la clase Dice.
    """

    def setUp(self):
        """
        Inicializa un objeto Dice para cada test.
        """
        self.dice = Dice()

    def test_roll_devuelve_lista_no_vacia(self):
        """
        Verifica que roll() devuelve una lista con al menos 2 valores.
        """
        valores = self.dice.roll()
        self.assertTrue(len(valores) >= 2)

    def test_roll_valores_en_rango_correcto(self):
        """
        Verifica que los valores de los dados estén en el rango 1-6.
        """
        valores = self.dice.roll()
        for v in valores:
            self.assertTrue(1 <= v <= 6)

    def test_tirada_doble_devuelve_cuatro_valores(self):
        """
        Verifica que si la tirada es doble, haya exactamente 4 valores.
        """
        while True:
            valores = self.dice.roll()
            if valores[0] == valores[1]:
                self.assertEqual(len(valores), 4)
                self.assertTrue(self.dice.tirada_doble())
                break

    def test_tirada_no_doble_devuelve_dos_valores(self):
        """
        Verifica que si la tirada no es doble, haya exactamente 2 valores.
        """
        while True:
            valores = self.dice.roll()
            if valores[0] != valores[1]:
                self.assertEqual(len(valores), 2)
                self.assertFalse(self.dice.tirada_doble())
                break

    def test_individual_values_devuelve_dos_valores(self):
        """
        Verifica que individual_values() siempre devuelve dos valores.
        """
        self.dice.roll()
        valores = self.dice.individual_values()
        self.assertEqual(len(valores), 2)

    def test_usar_valor_disponible_devuelve_true(self):
        """
        Verifica que usar un valor disponible devuelve True y lo marca como usado.
        """
        valores = self.dice.roll()
        valor = valores[0]
        resultado = self.dice.usar_valor(valor)
        self.assertTrue(resultado)
        self.assertIn(valor, self.dice.valores_usados())

    def test_usar_valor_no_disponible_devuelve_false(self):
        """
        Verifica que usar un valor no disponible devuelve False.
        """
        self.dice.roll()
        resultado = self.dice.usar_valor(7)  # valor imposible
        self.assertFalse(resultado)

    def test_valores_usados_devuelve_lista_correcta(self):
        """
        Verifica que valores_usados() devuelve los valores que ya fueron usados.
        """
        valores = self.dice.roll()
        valor = valores[0]
        self.dice.usar_valor(valor)
        usados = self.dice.valores_usados()
        self.assertIn(valor, usados)

if __name__ == "__main__":
    unittest.main()
