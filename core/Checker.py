class Checker:
    def __init__(self, jugador):
        self.jugador = jugador   # Jugador dueño de la ficha (1 o 2)
        self.en_barra = False    # True si la ficha está en la barra
        self.en_meta = False     # True si la ficha ya salió del tablero

    def get_jugador(self):
        # Devuelve el jugador dueño de la ficha
        return self.jugador

    def esta_en_barra(self):
        # Devuelve True si la ficha está en la barra
        return self.en_barra

    def esta_en_meta(self):
        # Devuelve True si la ficha ya salió del tablero (meta)
        return self.en_meta

    def mandar_a_barra(self):
        # Manda la ficha a la barra
        self.en_barra = True
        self.en_meta = False

    def sacar_de_barra(self):
        # Saca la ficha de la barra
        self.en_barra = False

    def mandar_a_meta(self):
        # Manda la ficha a la meta (fuera del tablero)
        self.en_meta = True
        self.en_barra = False
