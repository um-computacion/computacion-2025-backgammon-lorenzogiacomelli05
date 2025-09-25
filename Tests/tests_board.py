import unittest
from core.Board import Board
from core.Checker import Checker
from core.Player import Player

class TestBoard(unittest.TestCase):
    """
    Tests unitarios para la clase Board.
    Se validan las operaciones principales del tablero de Backgammon.
    """

    def setUp(self):
        """Configura un tablero y jugadores antes de cada test."""
        self.board = Board()
        self.jugador1 = Player(1, "X")
        self.jugador2 = Player(2, "O")

    def test_inicializacion_tablero(self):
        """El tablero debe tener fichas en posiciones iniciales estándar."""
        self.assertEqual(len(self.board.get_position(1)), 2)
        self.assertEqual(len(self.board.get_position(6)), 5)
        self.assertEqual(len(self.board.get_position(8)), 3)
        self.assertEqual(len(self.board.get_position(12)), 5)
        self.assertEqual(len(self.board.get_position(13)), 5)
        self.assertEqual(len(self.board.get_position(17)), 3)
        self.assertEqual(len(self.board.get_position(19)), 5)
        self.assertEqual(len(self.board.get_position(24)), 2)

    def test_añadir_y_sacar_ficha(self):
        """Debe poder añadirse y retirarse fichas en posiciones válidas."""
        ficha = Checker(1)
        self.board.añadir_ficha(5, ficha)
        self.assertEqual(len(self.board.get_position(5)), 1)

        sacada = self.board.sacar_ficha(5)
        self.assertEqual(sacada, ficha)
        self.assertEqual(len(self.board.get_position(5)), 0)

    def test_sacar_ficha_vacia(self):
        """Si no hay fichas en una posición, debe devolver None."""
        resultado = self.board.sacar_ficha(10)
        self.assertEqual(resultado, None)

    def test_set_posicion(self):
        """Debe colocar correctamente la cantidad de fichas de un jugador."""
        self.board.set_posicion(4, self.jugador1, 3)
        self.assertEqual(len(self.board.get_position(4)), 3)
        self.assertEqual(self.board.get_position(4)[0].get_jugador(), 1)

    def test_mandar_y_sacar_de_barra(self):
        """Debe mandar fichas a la barra y poder sacarlas."""
        ficha = Checker(1)
        self.board.mandar_a_barra(1, ficha)
        self.assertEqual(len(self.board.get_bar(1)), 1)

        sacada = self.board.sacar_de_barra(1)
        self.assertEqual(sacada.get_jugador(), 1)
        self.assertEqual(len(self.board.get_bar(1)), 0)

    def test_mandar_a_meta(self):
        """Debe mandar fichas al home (meta) del jugador."""
        ficha = Checker(2)
        self.board.mandar_a_meta(2, ficha)
        self.assertEqual(len(self.board.get_home(2)), 1)
        self.assertTrue(ficha.esta_en_meta())

    def test_vaciar_fichas(self):
        """Debe mover todas las fichas de un jugador directamente al home."""
        self.board.vaciar_fichas(self.jugador1)
        self.assertEqual(len(self.board.get_home(1)), 15)
        for i in range(1, 25):
            for ficha in self.board.get_position(i):
                self.assertFalse(ficha.get_jugador() == 1)

if __name__ == "__main__":
    unittest.main()
