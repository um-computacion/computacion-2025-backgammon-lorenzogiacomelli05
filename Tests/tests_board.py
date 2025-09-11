import unittest
from core.Board import Board

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
        self.assertEqual(len(self.board.positions[1]), 2)   # 2 fichas X en pos 1
        self.assertEqual(len(self.board.positions[6]), 5)   # 5 fichas O en pos 6
        self.assertEqual(len(self.board.positions[8]), 3)   # 3 fichas O en pos 8
        self.assertEqual(len(self.board.positions[12]), 5)  # 5 fichas X en pos 12
        self.assertEqual(len(self.board.positions[13]), 5)  # 5 fichas O en pos 13
        self.assertEqual(len(self.board.positions[17]), 3)  # 3 fichas X en pos 17
        self.assertEqual(len(self.board.positions[19]), 5)  # 5 fichas X en pos 19
        self.assertEqual(len(self.board.positions[24]), 2)  # 2 fichas O en pos 24

    def test_barra_vacia_al_inicio(self):
        """
        Verifica que la barra comience vacía.
        """
        self.assertEqual(len(self.board.bar["X"]), 0)
        self.assertEqual(len(self.board.bar["O"]), 0)

    def test_home_vacio_al_inicio(self):
        """
        Verifica que el home comience vacío.
        """
        self.assertEqual(len(self.board.home["X"]), 0)
        self.assertEqual(len(self.board.home["O"]), 0)

    def test_agregar_y_quitar_ficha(self):
        """
        Verifica que se puedan agregar y quitar fichas correctamente.
        """
        pos = 5
        self.board.positions[pos].append("X")
        self.assertEqual(len(self.board.positions[pos]), 1)

        ficha = self.board.positions[pos].pop()
        self.assertEqual(ficha, "X")
        self.assertEqual(len(self.board.positions[pos]), 0)

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
