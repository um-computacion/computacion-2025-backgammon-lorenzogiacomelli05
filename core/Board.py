from core.Checker import Checker

class Board:
    """
    Clase que representa el tablero de Backgammon.
    Maneja las posiciones de las fichas, la barra y el home.
    """

    def __init__(self):
        """
        Inicializa el tablero con 24 posiciones (1 - 24), la barra y el home.
        Coloca las fichas en la configuración inicial.
        """
        self.__positions__ = [[] for _ in range(25)]  # Índices 1–24
        self.__bar__ = {1: [], 2: []}   # fichas en la barra, por jugador
        self.__home__ = {1: [], 2: []}  # fichas que llegaron a la meta

        # Configuración inicial
        self.__positions__[1]  = [Checker(1) for _ in range(2)]
        self.__positions__[6]  = [Checker(2) for _ in range(5)]
        self.__positions__[8]  = [Checker(2) for _ in range(3)]
        self.__positions__[12] = [Checker(1) for _ in range(5)]
        self.__positions__[13] = [Checker(2) for _ in range(5)]
        self.__positions__[17] = [Checker(1) for _ in range(3)]
        self.__positions__[19] = [Checker(1) for _ in range(5)]
        self.__positions__[24] = [Checker(2) for _ in range(2)]

    def get_position(self, pos: int):
        """Devuelve la lista de fichas en una posición del tablero."""
        if 1 <= pos <= 24:
            return self.__positions__[pos]
        return []

    def añadir_ficha(self, pos: int, ficha: Checker):
        """Añade una ficha (Checker) en una posición válida del tablero."""
        if 1 <= pos <= 24:
            self.__positions__[pos].append(ficha)

    def sacar_ficha(self, pos: int):
        """
        Saca y devuelve la última ficha de una posición.
        Si no hay fichas, devuelve None.
        """
        if 1 <= pos <= 24 and self.__positions__[pos]:
            return self.__positions__[pos].pop()
        return None

    def mandar_a_barra(self, jugador: int, ficha: Checker):
        """Manda una ficha a la barra del jugador indicado."""
        ficha.mandar_a_barra()
        self.__bar__[jugador].append(ficha)

    def sacar_de_barra(self, jugador: int):
        """Saca y devuelve una ficha de la barra del jugador (si hay)."""
        if self.__bar__[jugador]:
            ficha = self.__bar__[jugador].pop()
            ficha.sacar_de_barra()
            return ficha
        return None

    def mandar_a_meta(self, jugador: int, ficha: Checker):
        """Manda una ficha al home (meta) del jugador."""
        ficha.mandar_a_meta()
        self.__home__[jugador].append(ficha)

    def get_bar(self, jugador: int):
        """Devuelve las fichas en la barra de un jugador."""
        return self.__bar__[jugador]

    def get_home(self, jugador: int):
        """Devuelve las fichas en la meta de un jugador."""
        return self.__home__[jugador]

    def set_posicion(self, pos: int, jugador, cantidad: int):
        """
        Coloca 'cantidad' de fichas de un jugador en una posición.
        Sobrescribe lo que hubiera en esa posición.
        """
        if 1 <= pos <= 24:
            self.__positions__[pos] = [Checker(jugador.get_numero()) for _ in range(cantidad)]

    def vaciar_fichas(self, jugador):
        """
        Elimina todas las fichas de un jugador del tablero
        y las coloca directamente en el home.
        """
        for i in range(1, 25):
            self.__positions__[i] = [c for c in self.__positions__[i] if c.get_jugador() != jugador.get_numero()]
        self.__home__[jugador.get_numero()] = [Checker(jugador.get_numero()) for _ in range(15)]

    # ==============================
    # Representación del tablero
    # ==============================

    def display(self):
        """
        Muestra el tablero en la terminal horizontalmente con posiciones 1 - 24.
        Cada posición muestra la ficha y cantidad como 1(5) o 2(3).
        Incluye Barra y Home.
        """
        col_width = 6  # ancho fijo de cada columna

        print("\n=== TABLERO DE BACKGAMMON ===\n")

        # --- Parte superior (posiciones 13–24) ---
        top_range = range(13, 25)
        print("Arriba: ", "".join([f"{i:2}".center(col_width) for i in top_range]))
        fila_top = []
        for i in top_range:
            if self.__positions__[i]:
                jugador = self.__positions__[i][0].get_jugador()
                cantidad = len(self.__positions__[i])
                fila_top.append(f"{jugador}({cantidad})".center(col_width))
            else:
                fila_top.append(" ".center(col_width))
        print("        " + "".join(fila_top))

        print("-" * (col_width * 12 + 8))  # separación

        # --- Parte inferior (posiciones 12–1) ---
        bottom_range = range(12, 0, -1)
        print("Abajo : ", "".join([f"{i:2}".center(col_width) for i in bottom_range]))
        fila_bottom = []
        for i in bottom_range:
            if self.__positions__[i]:
                jugador = self.__positions__[i][0].get_jugador()
                cantidad = len(self.__positions__[i])
                fila_bottom.append(f"{jugador}({cantidad})".center(col_width))
            else:
                fila_bottom.append(" ".center(col_width))
        print("        " + "".join(fila_bottom))

        # --- Barra ---
        print("\nBarra:")
        print(f"       J1: {len(self.__bar__[1])}".ljust(12) + f"J2: {len(self.__bar__[2])}".ljust(12))

        # --- Home ---
        print("\nHome:")
        print(f"       J1: {len(self.__home__[1])}".ljust(12) + f"J2: {len(self.__home__[2])}".ljust(12))


if __name__ == "__main__":
    board = Board()
    board.display()

