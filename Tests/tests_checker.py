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

    # ===== Test de inicialización =====
    def test_jugador_asignado_correctamente(self):
        """La ficha debe recordar a qué jugador pertenece."""
        self.assertEqual(self.ficha.get_jugador(), 1)

    def test_estado_inicial(self):
        """Al crearse, la ficha no debe estar ni en barra ni en meta."""
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())
        self.assertTrue(self.ficha.esta_en_tablero())

    def test_init_jugador_invalido(self):
        """Cubre ValueError cuando jugador no es 1 o 2."""
        for jugador in [0, 3, -1]:
            with self.assertRaises(ValueError):
                Checker(jugador)

    def test_init_jugador_valido(self):
        """Test que jugadores 1 y 2 son válidos."""
        for jugador in [1, 2]:
            ficha = Checker(jugador)
            self.assertEqual(ficha.get_jugador(), jugador)
            self.assertFalse(ficha.esta_en_barra())
            self.assertFalse(ficha.esta_en_meta())

    # ===== Tests estado barra =====
    def test_mandar_a_barra(self):
        """La ficha puede enviarse a la barra."""
        self.ficha.mandar_a_barra()
        self.assertTrue(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())
        self.assertFalse(self.ficha.esta_en_tablero())

    def test_sacar_de_barra(self):
        """Una ficha en la barra puede salir de ella."""
        self.ficha.mandar_a_barra()
        self.ficha.sacar_de_barra()
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertTrue(self.ficha.esta_en_tablero())

    # ===== Tests estado meta =====
    def test_mandar_a_meta(self):
        """La ficha puede moverse a la meta."""
        self.ficha.mandar_a_meta()
        self.assertTrue(self.ficha.esta_en_meta())
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_tablero())

    # ===== Tests transiciones de estado =====
    def test_cambio_barra_a_meta(self):
        """Si una ficha estaba en barra y va a meta, debe resetear barra."""
        self.ficha.mandar_a_barra()
        self.ficha.mandar_a_meta()
        self.assertTrue(self.ficha.esta_en_meta())
        self.assertFalse(self.ficha.esta_en_barra())

    def test_cambio_meta_a_barra(self):
        """Si una ficha estaba en meta y vuelve a barra, debe resetear meta."""
        self.ficha.mandar_a_meta()
        self.ficha.mandar_a_barra()
        self.assertTrue(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())

    def test_ciclo_completo_estados(self):
        """Ciclo completo: tablero -> barra -> tablero -> meta."""
        # A barra
        self.ficha.mandar_a_barra()
        self.assertFalse(self.ficha.esta_en_tablero())
        self.assertTrue(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())

        # De vuelta a tablero
        self.ficha.sacar_de_barra()
        self.assertTrue(self.ficha.esta_en_tablero())
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertFalse(self.ficha.esta_en_meta())

        # A meta
        self.ficha.mandar_a_meta()
        self.assertFalse(self.ficha.esta_en_tablero())
        self.assertFalse(self.ficha.esta_en_barra())
        self.assertTrue(self.ficha.esta_en_meta())

    # ===== Tests __repr__ =====
    def test_repr(self):
        """Verifica la representación de la ficha según su estado."""
        # Tablero
        repr_tablero = repr(self.ficha)
        self.assertIn("Checker", repr_tablero)
        self.assertIn("jugador=1", repr_tablero)
        self.assertIn("estado=tablero", repr_tablero)
        self.assertEqual(repr_tablero, "<Checker jugador=1, estado=tablero>")

        # Barra
        self.ficha.mandar_a_barra()
        repr_barra = repr(self.ficha)
        self.assertIn("estado=barra", repr_barra)

        # Meta
        self.ficha.mandar_a_meta()
        repr_meta = repr(self.ficha)
        self.assertIn("estado=meta", repr_meta)

if __name__ == "__main__":
    unittest.main()
