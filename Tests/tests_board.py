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

    # Configuración inicial

    def test_configuracion_inicial(self):
        """
        Verifica que la configuración inicial del tablero sea la correcta.
        """
        # Posición 1 debería tener 2 fichas del jugador 1
        self.assertEqual(len(self.board._Board__positions__[1]), 2)
        self.assertTrue(all(chk.get_jugador() == 1 for chk in self.board._Board__positions__[1]))

        # Posición 6 debería tener 5 fichas del jugador 2
        self.assertEqual(len(self.board._Board__positions__[6]), 5)
        self.assertTrue(all(chk.get_jugador() == 2 for chk in self.board._Board__positions__[6]))

    def test_barra_vacia_al_inicio(self):
        """
        Verifica que la barra comience vacía.
        """
        self.assertEqual(len(self.board._Board__bar__[1]), 0)
        self.assertEqual(len(self.board._Board__bar__[2]), 0)

    def test_home_vacio_al_inicio(self):
        """
        Verifica que el home comience vacío.
        """
        self.assertEqual(len(self.board._Board__home__[1]), 0)
        self.assertEqual(len(self.board._Board__home__[2]), 0)

    # Métodos principales

    def test_añadir_y_sacar_checker(self):
        """
        Verifica que se puedan añadir y quitar fichas correctamente.
        """
        pos = 5
        ficha = Checker(1)
        self.board.añadir_ficha(pos, ficha)
        self.assertEqual(len(self.board.get_position(pos)), 1)

        quitada = self.board.sacar_ficha(pos)
        self.assertIsInstance(quitada, Checker)
        self.assertEqual(quitada.get_jugador(), 1)
        self.assertEqual(len(self.board.get_position(pos)), 0)

    def test_sacar_de_posicion_vacia(self):
        """
        Verifica que sacar ficha de una posición vacía devuelva None.
        """
        resultado = self.board.sacar_ficha(4)  # posición vacía
        self.assertIsNone(resultado)

    def test_get_position_valida(self):
        """
        Verifica que get_position devuelve la lista de fichas correcta.
        """
        ficha = Checker(2)
        self.board.añadir_ficha(10, ficha)
        pos = self.board.get_position(10)
        self.assertEqual(len(pos), 1)
        self.assertEqual(pos[0].get_jugador(), 2)

    def test_get_position_invalida(self):
        """
        Verifica que get_position con posición fuera de rango devuelve lista vacía.
        """
        self.assertEqual(self.board.get_position(0), [])
        self.assertEqual(self.board.get_position(25), [])

    # Display

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
