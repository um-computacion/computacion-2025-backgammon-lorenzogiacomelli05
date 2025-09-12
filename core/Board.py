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
        self.__bar__ = {"X": [], "O": []}  # Fichas capturadas
        self.__home__ = {"X": [], "O": []}  # Fichas que salieron del tablero

        # Configuración inicial
        self.__positions__[1] = ['X'] * 2
        self.__positions__[6] = ['O'] * 5
        self.__positions__[8] = ['O'] * 3
        self.__positions__[12] = ['X'] * 5
        self.__positions__[13] = ['O'] * 5
        self.__positions__[17] = ['X'] * 3
        self.__positions__[19] = ['X'] * 5
        self.__positions__[24] = ['O'] * 2

    def display(self):
        """
        Muestra el tablero en la terminal horizontalmente con posiciones 1 - 24.
        Cada posición muestra la ficha y cantidad como X(5) o O(3).
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
                ficha = self.__positions__[i][0]
                cantidad = len(self.__positions__[i])
                fila_top.append(f"{ficha}({cantidad})".center(col_width))
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
                ficha = self.__positions__[i][0]
                cantidad = len(self.__positions__[i])
                fila_bottom.append(f"{ficha}({cantidad})".center(col_width))
            else:
                fila_bottom.append(" ".center(col_width))
        print("        " + "".join(fila_bottom))

        # --- Barra ---
        print("\nBarra:")
        print(f"       X: {len(self.__bar__['X'])}".ljust(12) + f"O: {len(self.__bar__['O'])}".ljust(12))

        # --- Home ---
        print("\nHome:")
        print(f"       X: {len(self.__home__['X'])}".ljust(12) + f"O: {len(self.__home__['O'])}".ljust(12))

if __name__ == "__main__":
    board = Board()
    board.display()
