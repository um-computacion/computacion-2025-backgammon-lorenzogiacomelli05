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
    def test_sacar_ficha_posicion_vacia(self):
        """Cubre línea 51: return None cuando no hay fichas."""
        # Limpiar posición 10
        self.board.__positions__[10] = []
        
        # Intentar sacar ficha de posición vacía
        ficha = self.board.sacar_ficha(10)
        self.assertIsNone(ficha)

    def test_sacar_ficha_posicion_invalida(self):
        """Cubre línea 51: return None con posición inválida."""
        # Posiciones inválidas
        ficha = self.board.sacar_ficha(0)
        self.assertIsNone(ficha)
        
        ficha = self.board.sacar_ficha(25)
        self.assertIsNone(ficha)
        
        ficha = self.board.sacar_ficha(-1)
        self.assertIsNone(ficha)

    # ===== COBERTURA LÍNEAS 58-59: set_posicion =====
    def test_set_posicion_valida(self):
        """Cubre líneas 58-59: set_posicion con posición válida."""
        # Colocar 3 fichas del jugador 1 en posición 15
        self.board.set_posicion(15, self.jugador1, 3)
        
        fichas = self.board.get_position(15)
        self.assertEqual(len(fichas), 3)
        self.assertTrue(all(f.get_jugador() == 1 for f in fichas))

    def test_set_posicion_sobrescribe(self):
        """Verifica que set_posicion sobrescribe las fichas existentes."""
        # Hay fichas iniciales en posición 6
        self.assertGreater(len(self.board.get_position(6)), 0)
        
        # Sobrescribir con 2 fichas del jugador 2
        self.board.set_posicion(6, self.jugador2, 2)
        
        fichas = self.board.get_position(6)
        self.assertEqual(len(fichas), 2)
        self.assertTrue(all(f.get_jugador() == 2 for f in fichas))

    def test_set_posicion_invalida(self):
        """Cubre que set_posicion no hace nada con posición inválida."""
        # Intentar con posiciones inválidas (no entra al if de línea 57)
        self.board.set_posicion(0, self.jugador1, 3)
        self.board.set_posicion(25, self.jugador1, 3)
        self.board.set_posicion(-5, self.jugador1, 3)
        
        # No debe haber crash

    # ===== COBERTURA LÍNEAS 67-68: mandar_a_barra =====
    def test_mandar_a_barra_jugador_1(self):
        """Cubre líneas 67-68: mandar ficha a la barra."""
        ficha = Checker(1)
        
        self.assertEqual(len(self.board.get_bar(1)), 0)
        
        self.board.mandar_a_barra(1, ficha)
        
        self.assertEqual(len(self.board.get_bar(1)), 1)
        self.assertTrue(ficha.esta_en_barra())

    def test_mandar_a_barra_jugador_2(self):
        """Cubre líneas 67-68: mandar ficha a la barra jugador 2."""
        ficha = Checker(2)
        
        self.board.mandar_a_barra(2, ficha)
        
        self.assertEqual(len(self.board.get_bar(2)), 1)
        self.assertTrue(ficha.esta_en_barra())

    # ===== COBERTURA LÍNEAS 72-76: sacar_de_barra =====
    def test_sacar_de_barra_con_fichas(self):
        """Cubre líneas 72-76: sacar ficha de barra cuando hay fichas."""
        ficha = Checker(1)
        
        # Poner ficha en barra
        self.board.mandar_a_barra(1, ficha)
        self.assertEqual(len(self.board.get_bar(1)), 1)
        
        # Sacar de barra
        ficha_sacada = self.board.sacar_de_barra(1)
        
        self.assertIsNotNone(ficha_sacada)
        self.assertFalse(ficha_sacada.esta_en_barra())
        self.assertEqual(len(self.board.get_bar(1)), 0)

    def test_sacar_de_barra_vacia(self):
        """Cubre línea 76: return None cuando barra vacía."""
        # Barra vacía
        self.assertEqual(len(self.board.get_bar(1)), 0)
        
        # Intentar sacar
        ficha = self.board.sacar_de_barra(1)
        self.assertIsNone(ficha)

    # ===== COBERTURA LÍNEAS 80-81: mandar_a_meta =====
    def test_mandar_a_meta_jugador_1(self):
        """Cubre líneas 80-81: mandar ficha a meta."""
        ficha = Checker(1)
        
        self.assertEqual(len(self.board.get_home(1)), 0)
        
        self.board.mandar_a_meta(1, ficha)
        
        self.assertEqual(len(self.board.get_home(1)), 1)
        self.assertTrue(ficha.esta_en_meta())

    def test_mandar_a_meta_jugador_2(self):
        """Cubre líneas 80-81: mandar ficha a meta jugador 2."""
        ficha = Checker(2)
        
        self.board.mandar_a_meta(2, ficha)
        
        self.assertEqual(len(self.board.get_home(2)), 1)
        self.assertTrue(ficha.esta_en_meta())

    # ===== COBERTURA LÍNEAS 96-101: vaciar_fichas =====
    def test_vaciar_fichas_jugador_1(self):
        """Cubre líneas 96-101: vaciar fichas del tablero y llevar a home."""
        # Verificar que hay fichas del jugador 1 en el tablero
        fichas_iniciales = 0
        for pos in self.board.__positions__[1:25]:
            for ficha in pos:
                if ficha.get_jugador() == 1:
                    fichas_iniciales += 1
        
        self.assertGreater(fichas_iniciales, 0)
        
        # Vaciar fichas
        self.board.vaciar_fichas(self.jugador1)
        
        # Verificar que no quedan fichas del jugador 1 en tablero
        fichas_restantes = 0
        for pos in self.board.__positions__[1:25]:
            for ficha in pos:
                if ficha.get_jugador() == 1:
                    fichas_restantes += 1
        
        self.assertEqual(fichas_restantes, 0)
        
        # Verificar que hay 15 fichas en home
        self.assertEqual(len(self.board.get_home(1)), 15)

    def test_vaciar_fichas_jugador_2(self):
        """Cubre líneas 96-101: vaciar fichas jugador 2."""
        # Verificar fichas iniciales
        fichas_iniciales = sum(
            1 for pos in self.board.__positions__[1:25]
            for ficha in pos if ficha.get_jugador() == 2
        )
        self.assertGreater(fichas_iniciales, 0)
        
        self.board.vaciar_fichas(self.jugador2)
        
        # No deben quedar fichas en tablero
        fichas_restantes = sum(
            1 for pos in self.board.__positions__[1:25]
            for ficha in pos if ficha.get_jugador() == 2
        )
        self.assertEqual(fichas_restantes, 0)
        
        # 15 fichas en home
        self.assertEqual(len(self.board.get_home(2)), 15)

    def test_vaciar_fichas_no_afecta_otro_jugador(self):
        """Verifica que vaciar_fichas solo afecta al jugador indicado."""
        # Contar fichas del jugador 2
        fichas_j2_antes = sum(
            1 for pos in self.board.__positions__[1:25]
            for ficha in pos if ficha.get_jugador() == 2
        )
        
        # Vaciar jugador 1
        self.board.vaciar_fichas(self.jugador1)
        
        # Fichas del jugador 2 deben permanecer igual
        fichas_j2_despues = sum(
            1 for pos in self.board.__positions__[1:25]
            for ficha in pos if ficha.get_jugador() == 2
        )
        self.assertEqual(fichas_j2_antes, fichas_j2_despues)

    # ===== COBERTURA LÍNEAS 113-148: display =====
    def test_display_no_crash(self):
        """Cubre líneas 113-148: método display."""
        # Llamar display no debe causar error
        try:
            self.board.display()
        except Exception as e:
            self.fail(f"display() causó una excepción: {e}")

    def test_display_con_fichas_personalizadas(self):
        """Test display con configuración personalizada."""
        # Limpiar tablero
        for i in range(1, 25):
            self.board.__positions__[i] = []
        
        # Colocar fichas específicas
        self.board.añadir_ficha(13, Checker(1))
        self.board.añadir_ficha(13, Checker(1))
        self.board.añadir_ficha(24, Checker(2))
        
        # Agregar fichas en barra y home
        self.board.mandar_a_barra(1, Checker(1))
        self.board.mandar_a_meta(2, Checker(2))
        
        try:
            self.board.display()
        except Exception as e:
            self.fail(f"display() causó una excepción: {e}")

    def test_display_tablero_vacio(self):
        """Test display con tablero vacío."""
        # Vaciar completamente el tablero
        for i in range(1, 25):
            self.board.__positions__[i] = []
        
        try:
            self.board.display()
        except Exception as e:
            self.fail(f"display() causó una excepción: {e}")

    # ===== TESTS ADICIONALES PARA COMPLETAR COBERTURA =====
    def test_get_position_posicion_valida(self):
        """Test para get_position con posición válida."""
        # Posición 1 tiene 2 fichas inicialmente
        fichas = self.board.get_position(1)
        self.assertEqual(len(fichas), 2)
        self.assertTrue(all(f.get_jugador() == 1 for f in fichas))

    def test_get_position_posicion_invalida(self):
        """Test para get_position con posición inválida."""
        # Posiciones inválidas retornan lista vacía
        self.assertEqual(self.board.get_position(0), [])
        self.assertEqual(self.board.get_position(25), [])
        self.assertEqual(self.board.get_position(-1), [])

    def test_añadir_ficha_posicion_valida(self):
        """Test para añadir_ficha."""
        # Limpiar posición
        self.board.__positions__[15] = []
        
        # Añadir ficha
        ficha = Checker(1)
        self.board.añadir_ficha(15, ficha)
        
        self.assertEqual(len(self.board.get_position(15)), 1)

    def test_añadir_ficha_posicion_invalida(self):
        """Test añadir_ficha con posición inválida."""
        ficha = Checker(1)
        
        # No debe causar error
        try:
            self.board.añadir_ficha(0, ficha)
            self.board.añadir_ficha(25, ficha)
        except Exception as e:
            self.fail(f"añadir_ficha() causó una excepción: {e}")

    def test_sacar_ficha_exitoso(self):
        """Test sacar_ficha cuando hay fichas."""
        # Posición 1 tiene fichas
        ficha = self.board.sacar_ficha(1)
        
        self.assertIsNotNone(ficha)
        self.assertIsInstance(ficha, Checker)

    def test_inicializacion_completa(self):
        """Verifica que la inicialización coloca todas las fichas correctamente."""
        # Verificar configuración inicial
        self.assertEqual(len(self.board.get_position(1)), 2)
        self.assertEqual(len(self.board.get_position(6)), 5)
        self.assertEqual(len(self.board.get_position(8)), 3)
        self.assertEqual(len(self.board.get_position(12)), 5)
        self.assertEqual(len(self.board.get_position(13)), 5)
        self.assertEqual(len(self.board.get_position(17)), 3)
        self.assertEqual(len(self.board.get_position(19)), 5)
        self.assertEqual(len(self.board.get_position(24)), 2)
        
        # Verificar barras y homes vacías
        self.assertEqual(len(self.board.get_bar(1)), 0)
        self.assertEqual(len(self.board.get_bar(2)), 0)
        self.assertEqual(len(self.board.get_home(1)), 0)
        self.assertEqual(len(self.board.get_home(2)), 0)


if __name__ == "__main__":
    unittest.main()
