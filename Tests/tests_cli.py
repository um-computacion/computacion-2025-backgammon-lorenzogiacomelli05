import unittest
from core.BackgammonGame import BackgammonGame
from CLI import BackgammonCLI

class TestBackgammonCLI(unittest.TestCase):
    """
    Tests unitarios básicos para la clase BackgammonCLI.
    """

    def setUp(self):
        """
        Se ejecuta antes de cada test.
        Crea una nueva instancia del CLI y del juego.
        """
        self.__cli__ = BackgammonCLI()
        self.__game__ = BackgammonGame()

    def test_instancia_cli(self):
        """
        Verifica que la instancia del CLI se cree correctamente.
        """
        self.assertIsInstance(self.__cli__, BackgammonCLI)

    def test_mostrar_estado(self):
        """
        Verifica que se pueda ejecutar mostrar_estado sin errores.
        """
        try:
            self.__cli__.mostrar_estado()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

    def test_mostrar_ayuda(self):
        """
        Verifica que se pueda ejecutar mostrar_ayuda sin errores.
        """
        try:
            self.__cli__.mostrar_ayuda()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

    def test_mostrar_dados(self):
        """
        Verifica que se pueda ejecutar mostrar_dados con una lista de valores.
        """
        try:
            self.__cli__.mostrar_dados([2, 5])
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

    def test_procesar_comando_ayuda(self):
        """
        Verifica que el comando 'ayuda' sea procesado correctamente.
        """
        resultado = self.__cli__.procesar_comando("ayuda")
        self.assertTrue(resultado)

    def test_procesar_comando_salir(self):
        """
        Verifica que el comando 'salir' retorne False.
        """
        resultado = self.__cli__.procesar_comando("salir")
        self.assertFalse(resultado)

    def test_procesar_comando_invalido(self):
        """
        Verifica que un comando desconocido no genere errores.
        """
        resultado = self.__cli__.procesar_comando("comando_invalido")
        self.assertTrue(resultado)

    def test_mostrar_resultado_final_sin_ganador(self):
        """
        Verifica que mostrar_resultado_final funcione incluso si no hay ganador.
        """
        try:
            self.__cli__.mostrar_resultado_final()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

    def test_reiniciar_partida(self):
        """
        Verifica que reiniciar_partida cree una nueva instancia de juego sin errores.
        """
        try:
            self.__cli__.reiniciar_partida()
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

if __name__ == "__main__":
    unittest.main()
