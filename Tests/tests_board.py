import unittest
from core import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_get_position_valida(self):
        # Verifica que devuelve una lista en una posición válida
        pos = self.board.get_position(0)
        self.assertTrue(len(pos) >= 0)  # Si devuelve una lista, su longitud siempre es >= 0

    def test_get_position_invalida(self):
        # Verifica que devuelve [] en posición inválida
        self.assertEqual(self.board.get_position(30), [])

    def test_posicion_vacia(self):
        # Verifica que una posición vacía se detecta correctamente
        self.assertTrue(self.board.posicion_vacia(2))   # Vacía
        self.assertFalse(self.board.posicion_vacia(0))  # Con fichas

    def test_contar_fichas(self):
        # Verifica que cuenta fichas correctamente
        self.assertEqual(self.board.contar_fichas(0), 2)   # 2 fichas X en inicio
        self.assertEqual(self.board.contar_fichas(23), 2)  # 2 fichas O en inicio

    def test_añadir_ficha(self):
        # Verifica que añadir ficha incrementa la cantidad
        self.board.añadir_ficha(0, 'X')
        self.assertEqual(self.board.contar_fichas(0), 3)

    def test_sacar_ficha(self):
        # Verifica que sacar ficha la elimina de la posición
        ficha = self.board.sacar_ficha(0)
        self.assertEqual(ficha, 'X')
        self.assertEqual(self.board.contar_fichas(0), 1)

    def test_sacar_ficha_vacio(self):
        # Verifica que sacar_ficha devuelve None si la posición está vacía
        result = self.board.sacar_ficha(2)  # Posición 2 vacía
        self.assertEqual(result, None)
        self.assertEqual(self.board.contar_fichas(2), 0)

if __name__ == "__main__":
    unittest.main()
