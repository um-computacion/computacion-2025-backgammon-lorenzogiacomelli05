import unittest
from core.Checker import Checker

class TestChecker(unittest.TestCase):
    """
    Tests unitarios para la clase Checker.
    Verifican que una ficha (Checker) cumpla con sus responsabilidades:
    pertenencia a un jugador y control de estado (barra/meta).
    """

    def setUp(self):
        """Se crea una ficha de ejemplo antes de cada test."""
        self.ficha = Checker(1)  # ficha del jugador 1

    def test_jugador_asignado_correctamente(self):
        """La ficha debe recordar a qué jugador pertenece."""
        self.assertEqual(self.ficha.get_jugador(), 1)

    def test_estado_inicial(self):
        """Al crearse, la ficha no debe estar ni en barra ni en meta."""
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())

    def test_mandar_a_barra(self):
        """La ficha puede enviarse a la barra."""
        self.ficha.mandar_a_barra()
        self.assertTrue(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())

    def test_sacar_de_barra(self):
        """Una ficha en la barra puede salir de ella."""
        self.ficha.mandar_a_barra()
        self.ficha.sacar_de_barra()
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())

    def test_mandar_a_meta(self):
        """La ficha puede moverse a la meta (fuera del tablero)."""
        self.ficha.mandar_a_meta()
        self.assertTrue(self.ficha.esta_en_meta())
        self.assertFalse(self.ficha.esta_en_barra())

    def test_cambio_estado_barra_a_meta(self):
        """Si una ficha estaba en barra y va a meta, debe resetear barra."""
        self.ficha.mandar_a_barra()
        self.ficha.mandar_a_meta()
        self.assertTrue(self.ficha.esta_en_meta())
        self.assertFalse(self.ficha.esta_en_barra())

    def test_cambio_estado_meta_a_barra(self):
        """Si una ficha estaba en meta y vuelve a barra, debe resetear meta."""
        self.ficha.mandar_a_meta()
        self.ficha.mandar_a_barra()
        self.assertTrue(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())
    # ===== COBERTURA LÍNEA 14: ValueError cuando jugador inválido =====
    def test_init_jugador_invalido_0(self):
        """Cubre línea 14: raise ValueError cuando jugador no es 1 o 2."""
        with self.assertRaises(ValueError) as context:
            Checker(0)
        self.assertEqual(str(context.exception), "El jugador debe ser 1 o 2")

    def test_init_jugador_invalido_3(self):
        """Cubre línea 14: raise ValueError con jugador 3."""
        with self.assertRaises(ValueError):
            Checker(3)

    def test_init_jugador_invalido_negativo(self):
        """Cubre línea 14: raise ValueError con jugador negativo."""
        with self.assertRaises(ValueError):
            Checker(-1)

    def test_init_jugador_valido_1(self):
        """Test que jugador 1 es válido."""
        ficha = Checker(1)
        self.assertEqual(ficha.get_jugador(), 1)
        self.assertFalse(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_meta())

    def test_init_jugador_valido_2(self):
        """Test que jugador 2 es válido."""
        ficha = Checker(2)
        self.assertEqual(ficha.get_jugador(), 2)
        self.assertFalse(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_meta())

    # ===== COBERTURA LÍNEA 27: esta_en_barra =====
    def test_esta_en_barra_false_inicial(self):
        """Cubre línea 27: esta_en_barra retorna False inicialmente."""
        ficha = Checker(1)
        self.assertFalse(ficha.esta_en_barra())

    def test_esta_en_barra_true_despues_mandar(self):
        """Cubre línea 27: esta_en_barra retorna True después de mandar a barra."""
        ficha = Checker(1)
        ficha.mandar_a_barra()
        self.assertTrue(ficha.esta_en_barra())

    # ===== COBERTURA LÍNEA 31: esta_en_meta =====
    def test_esta_en_meta_false_inicial(self):
        """Cubre línea 31: esta_en_meta retorna False inicialmente."""
        ficha = Checker(1)
        self.assertFalse(ficha.esta_en_meta())

    def test_esta_en_meta_true_despues_mandar(self):
        """Cubre línea 31: esta_en_meta retorna True después de mandar a meta."""
        ficha = Checker(1)
        ficha.mandar_a_meta()
        self.assertTrue(ficha.esta_en_meta())

    # ===== COBERTURA LÍNEA 35: esta_en_tablero =====
    def test_esta_en_tablero_true_inicial(self):
        """Cubre línea 35: esta_en_tablero retorna True inicialmente."""
        ficha = Checker(1)
        self.assertTrue(ficha.esta_en_tablero())

    def test_esta_en_tablero_false_en_barra(self):
        """Cubre línea 35: esta_en_tablero retorna False cuando está en barra."""
        ficha = Checker(1)
        ficha.mandar_a_barra()
        self.assertFalse(ficha.esta_en_tablero())

    def test_esta_en_tablero_false_en_meta(self):
        """Cubre línea 35: esta_en_tablero retorna False cuando está en meta."""
        ficha = Checker(1)
        ficha.mandar_a_meta()
        self.assertFalse(ficha.esta_en_tablero())

    # ===== COBERTURA LÍNEAS 41-42: mandar_a_barra =====
    def test_mandar_a_barra_cambia_estado(self):
        """Cubre líneas 41-42: mandar_a_barra cambia los estados."""
        ficha = Checker(1)
        
        ficha.mandar_a_barra()
        
        self.assertTrue(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_meta())
        self.assertFalse(ficha.esta_en_tablero())

    def test_mandar_a_barra_desde_meta(self):
        """Cubre líneas 41-42: mandar_a_barra desde meta resetea en_meta."""
        ficha = Checker(1)
        ficha.mandar_a_meta()
        self.assertTrue(ficha.esta_en_meta())
        
        ficha.mandar_a_barra()
        
        self.assertTrue(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_meta())

    # ===== COBERTURA LÍNEA 46: sacar_de_barra =====
    def test_sacar_de_barra_cambia_estado(self):
        """Cubre línea 46: sacar_de_barra cambia en_barra a False."""
        ficha = Checker(1)
        ficha.mandar_a_barra()
        self.assertTrue(ficha.esta_en_barra())
        
        ficha.sacar_de_barra()
        
        self.assertFalse(ficha.esta_en_barra())
        self.assertTrue(ficha.esta_en_tablero())

    def test_sacar_de_barra_desde_tablero(self):
        """Test sacar_de_barra cuando ya está en tablero."""
        ficha = Checker(1)
        self.assertFalse(ficha.esta_en_barra())
        
        ficha.sacar_de_barra()
        
        self.assertFalse(ficha.esta_en_barra())
        self.assertTrue(ficha.esta_en_tablero())

    # ===== COBERTURA LÍNEAS 50-51: mandar_a_meta =====
    def test_mandar_a_meta_cambia_estado(self):
        """Cubre líneas 50-51: mandar_a_meta cambia los estados."""
        ficha = Checker(1)
        
        ficha.mandar_a_meta()
        
        self.assertTrue(ficha.esta_en_meta())
        self.assertFalse(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_tablero())

    def test_mandar_a_meta_desde_barra(self):
        """Cubre líneas 50-51: mandar_a_meta desde barra resetea en_barra."""
        ficha = Checker(1)
        ficha.mandar_a_barra()
        self.assertTrue(ficha.esta_en_barra())
        
        ficha.mandar_a_meta()
        
        self.assertTrue(ficha.esta_en_meta())
        self.assertFalse(ficha.esta_en_barra())
 # ===== COBERTURA LÍNEA 14: ValueError cuando jugador inválido =====
    def test_init_jugador_invalido_0(self):
        """Cubre línea 14: raise ValueError cuando jugador no es 1 o 2."""
        with self.assertRaises(ValueError) as context:
            Checker(0)
        self.assertEqual(str(context.exception), "El jugador debe ser 1 o 2")

    def test_init_jugador_invalido_3(self):
        """Cubre línea 14: raise ValueError con jugador 3."""
        with self.assertRaises(ValueError):
            Checker(3)

    def test_init_jugador_invalido_negativo(self):
        """Cubre línea 14: raise ValueError con jugador negativo."""
        with self.assertRaises(ValueError):
            Checker(-1)

    def test_init_jugador_valido_1(self):
        """Test que jugador 1 es válido."""
        ficha = Checker(1)
        self.assertEqual(ficha.get_jugador(), 1)
        self.assertFalse(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_meta())

    def test_init_jugador_valido_2(self):
        """Test que jugador 2 es válido."""
        ficha = Checker(2)
        self.assertEqual(ficha.get_jugador(), 2)
        self.assertFalse(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_meta())

    # ===== COBERTURA LÍNEA 27: esta_en_barra =====
    def test_esta_en_barra_false_inicial(self):
        """Cubre línea 27: esta_en_barra retorna False inicialmente."""
        ficha = Checker(1)
        self.assertFalse(ficha.esta_en_barra())

    def test_esta_en_barra_true_despues_mandar(self):
        """Cubre línea 27: esta_en_barra retorna True después de mandar a barra."""
        ficha = Checker(1)
        ficha.mandar_a_barra()
        self.assertTrue(ficha.esta_en_barra())

    # ===== COBERTURA LÍNEA 31: esta_en_meta =====
    def test_esta_en_meta_false_inicial(self):
        """Cubre línea 31: esta_en_meta retorna False inicialmente."""
        ficha = Checker(1)
        self.assertFalse(ficha.esta_en_meta())

    def test_esta_en_meta_true_despues_mandar(self):
        """Cubre línea 31: esta_en_meta retorna True después de mandar a meta."""
        ficha = Checker(1)
        ficha.mandar_a_meta()
        self.assertTrue(ficha.esta_en_meta())

    # ===== COBERTURA LÍNEA 35: esta_en_tablero =====
    def test_esta_en_tablero_true_inicial(self):
        """Cubre línea 35: esta_en_tablero retorna True inicialmente."""
        ficha = Checker(1)
        self.assertTrue(ficha.esta_en_tablero())

    def test_esta_en_tablero_false_en_barra(self):
        """Cubre línea 35: esta_en_tablero retorna False cuando está en barra."""
        ficha = Checker(1)
        ficha.mandar_a_barra()
        self.assertFalse(ficha.esta_en_tablero())

    def test_esta_en_tablero_false_en_meta(self):
        """Cubre línea 35: esta_en_tablero retorna False cuando está en meta."""
        ficha = Checker(1)
        ficha.mandar_a_meta()
        self.assertFalse(ficha.esta_en_tablero())

    # ===== COBERTURA LÍNEAS 41-42: mandar_a_barra =====
    def test_mandar_a_barra_cambia_estado(self):
        """Cubre líneas 41-42: mandar_a_barra cambia los estados."""
        ficha = Checker(1)
        
        ficha.mandar_a_barra()
        
        self.assertTrue(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_meta())
        self.assertFalse(ficha.esta_en_tablero())

    def test_mandar_a_barra_desde_meta(self):
        """Cubre líneas 41-42: mandar_a_barra desde meta resetea en_meta."""
        ficha = Checker(1)
        ficha.mandar_a_meta()
        self.assertTrue(ficha.esta_en_meta())
        
        ficha.mandar_a_barra()
        
        self.assertTrue(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_meta())

    # ===== COBERTURA LÍNEA 46: sacar_de_barra =====
    def test_sacar_de_barra_cambia_estado(self):
        """Cubre línea 46: sacar_de_barra cambia en_barra a False."""
        ficha = Checker(1)
        ficha.mandar_a_barra()
        self.assertTrue(ficha.esta_en_barra())
        
        ficha.sacar_de_barra()
        
        self.assertFalse(ficha.esta_en_barra())
        self.assertTrue(ficha.esta_en_tablero())

    def test_sacar_de_barra_desde_tablero(self):
        """Test sacar_de_barra cuando ya está en tablero."""
        ficha = Checker(1)
        self.assertFalse(ficha.esta_en_barra())
        
        ficha.sacar_de_barra()
        
        self.assertFalse(ficha.esta_en_barra())
        self.assertTrue(ficha.esta_en_tablero())

    # ===== COBERTURA LÍNEAS 50-51: mandar_a_meta =====
    def test_mandar_a_meta_cambia_estado(self):
        """Cubre líneas 50-51: mandar_a_meta cambia los estados."""
        ficha = Checker(1)
        
        ficha.mandar_a_meta()
        
        self.assertTrue(ficha.esta_en_meta())
        self.assertFalse(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_tablero())

    def test_mandar_a_meta_desde_barra(self):
        """Cubre líneas 50-51: mandar_a_meta desde barra resetea en_barra."""
        ficha = Checker(1)
        ficha.mandar_a_barra()
        self.assertTrue(ficha.esta_en_barra())
        
        ficha.mandar_a_meta()
        
        self.assertTrue(ficha.esta_en_meta())
        self.assertFalse(ficha.esta_en_barra())

    # ===== COBERTURA LÍNEAS 56-62: __repr__ =====
    def test_repr_en_barra(self):
        """Cubre líneas 56-57: __repr__ cuando está en barra."""
        ficha = Checker(1)
        ficha.mandar_a_barra()
        
        representacion = repr(ficha)
        
        self.assertIn("Checker", representacion)
        self.assertIn("jugador=1", representacion)
        self.assertIn("estado=barra", representacion)

    def test_repr_en_meta(self):
        """Cubre líneas 58-59: __repr__ cuando está en meta."""
        ficha = Checker(2)
        ficha.mandar_a_meta()
        
        representacion = repr(ficha)
        
        self.assertIn("Checker", representacion)
        self.assertIn("jugador=2", representacion)
        self.assertIn("estado=meta", representacion)

    def test_repr_en_tablero(self):
        """Cubre líneas 60-61: __repr__ cuando está en tablero."""
        ficha = Checker(1)
        
        representacion = repr(ficha)
        
        self.assertIn("Checker", representacion)
        self.assertIn("jugador=1", representacion)
        self.assertIn("estado=tablero", representacion)

    def test_repr_formato_completo(self):
        """Test formato completo de __repr__."""
        ficha = Checker(1)
        representacion = repr(ficha)
        
        # Línea 62: formato completo
        self.assertEqual(representacion, "<Checker jugador=1, estado=tablero>")

    # ===== TESTS ADICIONALES PARA TRANSICIONES DE ESTADO =====
    def test_ciclo_completo_estados(self):
        """Test ciclo completo: tablero -> barra -> tablero -> meta."""
        ficha = Checker(1)
        
        # Estado inicial: tablero
        self.assertTrue(ficha.esta_en_tablero())
        self.assertFalse(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_meta())
        
        # A barra
        ficha.mandar_a_barra()
        self.assertFalse(ficha.esta_en_tablero())
        self.assertTrue(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_meta())
        
        # De vuelta a tablero
        ficha.sacar_de_barra()
        self.assertTrue(ficha.esta_en_tablero())
        self.assertFalse(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_meta())
        
        # A meta
        ficha.mandar_a_meta()
        self.assertFalse(ficha.esta_en_tablero())
        self.assertFalse(ficha.esta_en_barra())
        self.assertTrue(ficha.esta_en_meta())

    def test_multiples_llamadas_mandar_a_barra(self):
        """Test múltiples llamadas a mandar_a_barra."""
        ficha = Checker(1)
        
        ficha.mandar_a_barra()
        ficha.mandar_a_barra()
        
        self.assertTrue(ficha.esta_en_barra())
        self.assertFalse(ficha.esta_en_meta())

    def test_multiples_llamadas_mandar_a_meta(self):
        """Test múltiples llamadas a mandar_a_meta."""
        ficha = Checker(1)
        
        ficha.mandar_a_meta()
        ficha.mandar_a_meta()
        
        self.assertTrue(ficha.esta_en_meta())
        self.assertFalse(ficha.esta_en_barra())


if __name__ == "__main__":
    unittest.main()
