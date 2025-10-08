from core.BackgammonGame import BackgammonGame

class BackgammonCLI:
    """
    Clase que representa la interfaz de línea de comandos (CLI) del juego de Backgammon.
    Se encarga de gestionar toda la interacción con el usuario a través de la terminal,
    mostrando el tablero, procesando entradas y comunicando los resultados del juego.
    """

    def __init__(self):
        """
        Constructor del CLI. Crea una nueva instancia del juego de Backgammon.
        Atributos:
            self.__game__ (BackgammonGame): instancia principal del juego que
            contiene toda la lógica interna del Backgammon.
        """
        self.__game__ = BackgammonGame()

    # INTERFAZ

    def mostrar_estado(self):
        """
        Muestra en la consola el estado actual del tablero del juego.
        Incluye una vista clara de las posiciones y fichas actuales.
        """
        board = self.__game__.get_board()
        print("\n=== Estado del Tablero ===")
        board.display()
        print("==========================\n")

    def mostrar_ayuda(self):
        """
        Muestra las instrucciones básicas del juego y los comandos válidos.
        """
        print("\n=== Guía rápida de comandos ===")
        print("Durante tu turno, deberás ingresar:")
        print(" - Origen: punto desde el que moverás tu ficha (1-24, o 0 si está en la barra).")
        print(" - Destino: punto al que querés moverla (1-24, o 25 si querés sacarla del tablero).")
        print(" - Dado: valor del dado que vas a usar para ese movimiento.")
        print("\nEjemplo: si tiraste [3, 5], podés mover desde el punto 12 al 9 (usando 3).")
        print("El sistema te avisará si un movimiento no es válido.")
        print("\nComandos disponibles durante la partida:")
        print(" - 'salir': finaliza la partida inmediatamente.")
        print(" - 'ayuda': muestra nuevamente esta guía.")
        print("===============================\n")

    def mostrar_resultado_final(self):
        """
        Muestra en consola el resultado final de la partida cuando hay un ganador.
        """
        ganador = self.__game__.get_ganador()
        print("\n=== Resultado Final ===")
        if ganador:
            print(f"El Jugador {ganador.get_numero()} ({ganador.get_ficha()}) ganó.")
        else:
            print("La partida terminó sin ganador.")
        print("========================\n")

    def mostrar_dados(self, valores):
        """
        Muestra en consola los valores actuales de los dados.
        """
        print(f"\nDados obtenidos: {valores}\n")

    def mostrar_menu_principal(self):
        """
        Muestra el menú principal y devuelve la opción elegida por el usuario.
        """
        print("=== Menú Principal ===")
        print("1: Jugar")
        print("2: Ver ayuda")
        print("3: Salir")
        return input("\nSelecciona una opción (1-3): ").strip()

    # CONTROL DE FLUJO

    def procesar_comando(self, comando):
        """
        Procesa comandos de texto que el usuario puede ingresar en cualquier momento.
        Args:
            comando (str): texto ingresado por el usuario.
        Returns:
            bool: True si el programa debe continuar, False si debe finalizar.
        """
        if comando.lower() == "salir":
            print("\nJuego interrumpido por el usuario.")
            return False
        elif comando.lower() == "ayuda":
            self.mostrar_ayuda()
            return True
        return True

    def ejecutar_turno(self):
        """
        Ejecuta el turno completo del jugador actual: Lanza los dados, solicita los movimientos y los valida. Finaliza cuando se usan todos los dados o se gana la partida.
        """
        jugador = self.__game__.get_jugador_actual()
        print("\n------------------------------------------")
        print(f"Turno del Jugador {jugador.get_numero()} ({jugador.get_ficha()})")
        print("------------------------------------------")

        # Tirar los dados
        valores = self.__game__.tirar_dados()
        self.mostrar_dados(valores)

# Mientras haya dados disponibles, el jugador puede seguir moviendo fichas
        while self.__game__.get_dados_actuales():
# Mostrar el estado actual del tablero antes de cada movimiento
            self.mostrar_estado()

            try:
# --- Solicitar punto de origen ---
# El jugador indica desde qué punto quiere mover una ficha.
# Puede ser un número del 1 al 24, o 0 si está sacando desde la barra.
                origen_input = input("Origen (1-24, 0=barra, 'salir'=terminar): ").strip()
                if not self.procesar_comando(origen_input):
                    exit(0)
                origen = int(origen_input)

# --- Solicitar punto de destino ---
# El jugador indica a qué punto moverá la ficha.
# Puede ser un número del 1 al 24, o 25 si está sacando del tablero.
                destino_input = input("Destino (1-24, 25=meta, 'salir'=terminar): ").strip()
                if not self.procesar_comando(destino_input):
                    exit(0)
                destino = int(destino_input)

# --- Seleccionar el dado a usar ---
# Se muestran los dados disponibles y se pide cuál utilizar para este movimiento.
                dado_input = input(f"Selecciona dado {self.__game__.get_dados_actuales()}: ").strip()
                if not self.procesar_comando(dado_input):
                    exit(0)
                dado = int(dado_input)

# --- Intentar realizar el movimiento ---
# Se envían los valores al núcleo del juego, que valida y ejecuta el movimiento.
                if self.__game__.mover_ficha(origen, destino, dado):
                    print("Movimiento realizado correctamente.")

# Verificar si con este movimiento se completó la partida
                    if self.__game__.juego_terminado():
                        self.mostrar_resultado_final()
                        return
                else:
# Movimiento inválido por reglas del juego 
                    print("Movimiento inválido. Intenta nuevamente.")

# --- Manejo de errores comunes ---
            except ValueError:
# El jugador ingresó texto o un número inválido
                print("Entrada inválida. Solo se permiten números enteros.")
            except Exception as e:
# Captura cualquier otro error imprevisto sin romper el juego
                print(f"Error: {str(e)}")

        # Cambiar turno
        print("\nFin del turno.")
        self.__game__.cambiar_turno()
        input("Presiona Enter para continuar con el siguiente jugador...")

    def iniciar(self):
        """
        Inicia el ciclo principal del juego de Backgammon en la terminal.
        """
        print("=== Bienvenido al Backgammon ===")

        while True:
            opcion = self.mostrar_menu_principal()

            if opcion == "1":
                print("\n Iniciando...\n")
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
                print("Opción inválida. Elegí 1, 2 o 3.\n")

if __name__ == "__main__":
    cli = BackgammonCLI()
    cli.iniciar()