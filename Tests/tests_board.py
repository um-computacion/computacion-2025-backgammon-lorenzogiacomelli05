import unittest
from core.Board import Board
from core.Checker import Checker

class TestBoard(unittest.TestCase):
    """
    Pruebas unitarias para la clase Board de Backgammon.
    """

    def setUp(self):
        """
        Se ejecuta antes de cada test. Crea un tablero nuevo.
        """
        self.board = Board()

    def test_configuracion_inicial(self):
        """
        Verifica que la configuración inicial del tablero sea la correcta.
        """
        # Posición 1 debería tener 2 fichas del jugador 1 (X)
        self.assertEqual(len(self.board._Board__positions__[1]), 2)
        self.assertTrue(all(isinstance(chk, Checker) for chk in self.board._Board__positions__[1]))

        # Posición 6 debería tener 5 fichas del jugador 2 (O)
        self.assertEqual(len(self.board._Board__positions__[6]), 5)
        self.assertTrue(all(chk.get_jugador() == 2 for chk in self.board._Board__positions__[6]))

    def test_barra_vacia_al_inicio(self):
        """
        Verifica que la barra comience vacía.
        """
        self.assertEqual(len(self.board._Board__bar__["X"]), 0)
        self.assertEqual(len(self.board._Board__bar__["O"]), 0)

    def test_home_vacio_al_inicio(self):
        """
        Verifica que el home comience vacío.
        """
        self.assertEqual(len(self.board._Board__home__["X"]), 0)
        self.assertEqual(len(self.board._Board__home__["O"]), 0)

    def test_agregar_y_quitar_checker(self):
        """
        Verifica que se puedan agregar y quitar fichas (Checker) correctamente.
        """
        pos = 5
        ficha = Checker(1)  # jugador 1 => 'X'
        self.board._Board__positions__[pos].append(ficha)
        self.assertEqual(len(self.board._Board__positions__[pos]), 1)

        quitada = self.board._Board__positions__[pos].pop()
        self.assertIsInstance(quitada, Checker)
        self.assertEqual(quitada.get_jugador(), 1)
        self.assertEqual(len(self.board._Board__positions__[pos]), 0)

    def test_display_no_rompe(self):
        """
        Verifica que el método display se ejecute sin errores.
        (No valida la salida en consola).
        """
        try:
            self.board.display()
        except Exception as e:
            self.fail(f"display lanzó una excepción: {e}")

if __name__ == "__main__":
    unittest.main()
