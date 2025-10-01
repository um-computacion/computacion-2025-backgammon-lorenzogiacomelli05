from core.BackgammonGame import BackgammonGame

class BackgammonCLI:
    """
    Interfaz de línea de comandos para jugar Backgammon.
    Maneja la interacción con el usuario y delega la lógica al juego.
    """

    def __init__(self):
        """
        Inicializa el CLI con una instancia de BackgammonGame.
        """
        self.__game__ = BackgammonGame()

    def mostrar_estado(self):
        """
        Muestra en consola el estado actual del tablero.
        """
        board = self.__game__.get_board()
        print("\n=== Estado del Tablero ===")
        board.display()
        print("==========================\n")

    def ejecutar_turno(self):
        """
        Ejecuta un turno del jugador actual.
        Permite tirar dados y mover fichas hasta usar todos los dados.
        """
        jugador = self.__game__.get_jugador_actual()
        print(f"\nTurno del Jugador {jugador.get_numero()} ({jugador.get_ficha()})")

        # Tirar dados
        valores = self.__game__.tirar_dados()
        print(f"Dados: {valores}")

        # Mientras haya dados disponibles
        while self.__game__.get_dados_actuales():
            try:
                origen = int(input("Origen (1-24, 0=barra): "))
                destino = int(input("Destino (1-24, 0 o 25=meta): "))
                dado = int(input(f"Elige dado {self.__game__.get_dados_actuales()}: "))

                if self.__game__.mover_ficha(origen, destino, dado):
                    print("Movimiento realizado.")
                else:
                    print("Movimiento inválido, intenta de nuevo.")
            except ValueError:
                print("Entrada inválida, ingresa solo números.")

            self.mostrar_estado()

        # Cambiar turno
        self.__game__.cambiar_turno()

    def iniciar(self):
        """
        Inicia el ciclo principal del juego en la terminal.
        """
        print("=== Bienvenido al Backgammon CLI ===")
        self.mostrar_estado()

        while not self.__game__.juego_terminado():
            self.ejecutar_turno()

        print("=== Fin del juego ===")

if __name__ == "__main__":
    cli = BackgammonCLI()
    cli.iniciar()
