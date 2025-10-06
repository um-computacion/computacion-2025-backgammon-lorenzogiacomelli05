from core.BackgammonGame import BackgammonGame

class BackgammonCLI:
    """
    Clase que representa la interfaz de línea de comandos (CLI) del juego de Backgammon.
    Se encarga de: Mostrar el estado del juego y los tableros. Recibir entradas del usuario desde la terminal. Delegar toda la lógica al núcleo del juego (BackgammonGame).
    """

    def __init__(self):
        """
        Constructor del CLI. Crea una nueva instancia del juego de Backgammon.
        Atributos:
            self.__game__ (BackgammonGame): instancia del núcleo del juego que 
            contiene toda la lógica interna del Backgammon.
        """
        self.__game__ = BackgammonGame()

    def mostrar_estado(self):
        """
        Muestra en la consola el estado actual del tablero del juego.
        Se invoca tras cada movimiento para que el jugador pueda visualizar 
        la distribución actual de las fichas en el tablero.
        """
        board = self.__game__.get_board()
        print("\n=== Estado del Tablero ===")
        board.display()
        print("==========================\n")

    def mostrar_ayuda(self):
        """
        Muestra las instrucciones básicas del juego y los comandos que el 
        usuario puede ingresar en la terminal.
        Es útil para jugadores nuevos o para recordar los movimientos válidos.
        """
        print("\n=== Guía rápida de comandos ===")
        print("Durante tu turno, deberás ingresar:")
        print(" - Origen: punto desde el que moverás tu ficha (1-24, o 0 si está en la barra).")
        print(" - Destino: punto al que querés moverla (1-24, o 25 si querés sacarla del tablero).")
        print(" - Dado: valor del dado que vas a usar para ese movimiento.")
        print("\nEjemplo: si tiraste [3, 5], podés mover desde el punto 12 al 9 (usando 3).")
        print("El sistema te avisará si un movimiento no es válido.")
        print("\nPodés escribir 'salir' en cualquier momento para terminar el juego.")
        print("===============================\n")

    def mostrar_resultado_final(self):
        """
        Muestra en consola el resultado final de la partida cuando hay un ganador.
        
        Se invoca automáticamente al finalizar el juego, mostrando qué jugador
        logró sacar todas sus fichas del tablero. Si por alguna razón no hay 
        un ganador (empate o interrupción), informa el estado correspondiente.
        """
        ganador = self.__game__.get_ganador()
        print("\n=== Resultado Final ===")
        if ganador:
            print(f"El Jugador {ganador.get_numero()} ({ganador.get_ficha()}) ganó.")
        else:
            print("No se pudo determinar un ganador.")
        print("========================\n")

    def ejecutar_turno(self):
        """
        Controla la ejecución completa de un turno del jugador actual.
        Incluye: Tirar los dados. Permitir al jugador mover fichas según los valores obtenidos. Validar que los movimientos sean correctos. Pasar el turno al siguiente jugador cuando se usen todos los dados.
        """
        jugador = self.__game__.get_jugador_actual()
        print("\n------------------------------------------")
        print(f"Turno del Jugador {jugador.get_numero()} ({jugador.get_ficha()})")
        print("------------------------------------------")

        # Tirar dados
        valores = self.__game__.tirar_dados()
        print(f"Dados obtenidos: {valores}")

        # Mientras haya dados disponibles
        while self.__game__.get_dados_actuales():
            self.mostrar_estado()
            try:
                origen_input = input("Origen (1-24, 0=barra): ").strip()
                if origen_input.lower() == "salir":
                    print("Juego interrumpido por el usuario.")
                    exit(0)
                origen = int(origen_input)

                destino_input = input("Destino (1-24, 0 o 25=meta): ").strip()
                if destino_input.lower() == "salir":
                    print("Juego interrumpido por el usuario.")
                    exit(0)
                destino = int(destino_input)

                dado_input = input(f"Elige dado {self.__game__.get_dados_actuales()}: ").strip()
                if dado_input.lower() == "salir":
                    print("Juego interrumpido por el usuario.")
                    exit(0)
                dado = int(dado_input)

                # Intentar realizar el movimiento
                if self.__game__.mover_ficha(origen, destino, dado):
                    print("Movimiento realizado correctamente.")
                    # Comprobación inmediata de victoria
                    if self.__game__.juego_terminado():
                        self.mostrar_resultado_final()
                        return
                else:
                    print("Movimiento inválido. Intenta de vuelta.")
            except ValueError:
                print("Entrada inválida. Ingresa solo números.")
            except Exception as e:
                print(f"Error: {str(e)}")

        # Cambiar turno al finalizar los movimientos
        self.__game__.cambiar_turno()
        input("Enter para siguiente turno...")

    def iniciar(self):
        """
        Inicia el ciclo principal del juego de Backgammon en la terminal.
        Permite al usuario elegir entre:
        1. Comenzar una partida.
        2. Ver la ayuda de comandos.
        3. Salir del juego.
        Cuando se selecciona “Jugar”, se ejecuta el bucle principal del juego
        hasta que uno de los jugadores cumple la condición de victoria.
        """
        print("=== Bienvenido al Backgammon ===")
        print("Este es un juego por turnos. Se alternan los jugadores hasta que uno gane.\n")

        while True:
            print("1: Jugar una partida")
            print("2: Ver ayuda")
            print("3: Salir")
            opcion = input("\nSelecciona una opción (1-3): ").strip()

            if opcion == "1":
                self.mostrar_estado()
                while not self.__game__.juego_terminado():
                    self.ejecutar_turno()
                self.mostrar_resultado_final()
                break
            elif opcion == "2":
                self.mostrar_ayuda()
            elif opcion == "3":
                print("Gracias por jugar al Backgammon.")
                break
            else:
                print("Opción inválida. Elige 1, 2 o 3.\n")

if __name__ == "__main__":
    cli = BackgammonCLI()
    cli.iniciar()