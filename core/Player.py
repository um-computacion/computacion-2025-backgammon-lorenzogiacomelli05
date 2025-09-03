class Jugador:
    def __init__(self, numero, ficha):
        self.numero = numero  # Jugador 1 o Jugador 2
        self.ficha = ficha    # 'X' o 'O'

    def get_numero(self):
        return self.numero

    def get_ficha(self):
        return self.ficha
