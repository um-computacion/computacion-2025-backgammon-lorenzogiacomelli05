class Board:
    def __init__(self):
        # 24 posiciones del tablero
        self.positions = [[] for _ in range(24)]

        # Configuración inicial del backgammon (simplificada)
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
            pos = ''.join(self.positions[i]) if self.positions[i] else '.'
            print(f"{i:2}: {pos}")

if __name__ == "__main__":
    board = Board()
    board.display()

