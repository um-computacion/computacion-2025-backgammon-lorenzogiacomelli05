class Board:
    def __init__(self):
        # 24 posiciones del tablero
        self.positions = [[] for _ in range(24)]

        # Configuración inicial simplificada
        self.positions[0] = ['X', 'X']
        self.positions[11] = ['X'] * 5
        self.positions[16] = ['X'] * 3
        self.positions[18] = ['X'] * 5

        self.positions[23] = ['O', 'O']
        self.positions[12] = ['O'] * 5
        self.positions[7] = ['O'] * 3
        self.positions[5] = ['O'] * 5

    def display(self):
        print("=== TABLERO DE BACKGAMMON ===")
        for i in range(24):
            if self.positions[i]:
                ficha = self.positions[i][0]
                cantidad = len(self.positions[i])
                pos = f"{ficha}({cantidad})"
            else:
                pos = "."
            print(f"{i+1:2}: {pos}")
            if i == 11:
                print("-------- MITAD DEL TABLERO --------")

    # Métodos “simples” para manipular fichas
    def get_position(self, pos):
        """Devuelve las fichas en una posición (0-23)"""
        if 0 <= pos < 24:
            return self.positions[pos]
        return []

    def posicion_vacia(self, pos):
        """Devuelve True si la posición está vacía"""
        return len(self.get_position(pos)) == 0

    def contar_fichas(self, pos):
        """Cantidad de fichas en una posición"""
        return len(self.get_position(pos))

    def añadir_ficha(self, pos, ficha):
        """Agrega una ficha en una posición"""
        if 0 <= pos < 24:
            self.positions[pos].append(ficha)

    def sacar_ficha(self, pos):
        """Quita una ficha de una posición (si hay alguna)"""
        if 0 <= pos < 24 and self.positions[pos]:
            return self.positions[pos].pop()
        return None

if __name__ == "__main__":
    board = Board()
    board.display()