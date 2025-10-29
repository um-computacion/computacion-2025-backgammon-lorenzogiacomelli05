import pygame
from core.BackgammonGame import BackgammonGame

# Inicializar Pygame
pygame.init()

# Constantes
ANCHO = 1400
ALTO = 900
FPS = 60

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
MARRON_CLARO = (222, 184, 135)
MARRON_OSCURO = (139, 90, 43)
VERDE = (34, 139, 34)
ROJO = (220, 20, 60)
AZUL = (30, 144, 255)
AMARILLO = (255, 215, 0)
GRIS = (128, 128, 128)
GRIS_CLARO = (200, 200, 200)
VERDE_CLARO = (144, 238, 144)

class BackgammonPygame:
    def __init__(self):
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Backgammon")
        self.reloj = pygame.time.Clock()
        self.game = BackgammonGame()
        
        # Estado del juego
        self.estado = "MENU"  # MENU, JUGANDO, GANADOR
        self.origen_seleccionado = None
        self.destino_seleccionado = None
        self.dados_lanzados = False
        self.mensaje = ""
        self.tiempo_mensaje = 0
        
        # Fuentes
        self.fuente_grande = pygame.font.Font(None, 48)
        self.fuente_mediana = pygame.font.Font(None, 36)
        self.fuente_pequena = pygame.font.Font(None, 24)
        
    def dibujar_tablero(self):
        # Fondo
        self.pantalla.fill(MARRON_CLARO)
        
        # Bordes del tablero
        pygame.draw.rect(self.pantalla, MARRON_OSCURO, (200, 100, 1000, 700), 5)
        
        # Barra central
        pygame.draw.rect(self.pantalla, MARRON_OSCURO, (675, 100, 50, 700))
        
        # Dibujar triángulos (puntos del tablero)
        ancho_triangulo = 75
        alto_triangulo = 280
        
        # Parte superior (puntos 13-24)
        # Lado derecho superior: 13-18
        for i in range(6):
            x = 200 + i * ancho_triangulo
            color = MARRON_OSCURO if i % 2 == 0 else BLANCO
            puntos = [
                (x, 100),
                (x + ancho_triangulo, 100),
                (x + ancho_triangulo // 2, 100 + alto_triangulo)
            ]
            pygame.draw.polygon(self.pantalla, color, puntos)
            pygame.draw.polygon(self.pantalla, NEGRO, puntos, 2)
            
            # Número del punto
            num_punto = 13 + i
            texto = self.fuente_pequena.render(str(num_punto), True, NEGRO)
            self.pantalla.blit(texto, (x + ancho_triangulo // 2 - 8, 110))
        
        # Lado izquierdo superior: 19-24
        for i in range(6):
            x = 725 + i * ancho_triangulo
            color = MARRON_OSCURO if i % 2 == 1 else BLANCO
            puntos = [
                (x, 100),
                (x + ancho_triangulo, 100),
                (x + ancho_triangulo // 2, 100 + alto_triangulo)
            ]
            pygame.draw.polygon(self.pantalla, color, puntos)
            pygame.draw.polygon(self.pantalla, NEGRO, puntos, 2)
            
            # Número del punto
            num_punto = 19 + i
            texto = self.fuente_pequena.render(str(num_punto), True, NEGRO)
            self.pantalla.blit(texto, (x + ancho_triangulo // 2 - 8, 110))
        
        # Parte inferior (puntos 1-12)
        # Lado derecho inferior: 12-7
        for i in range(6):
            x = 200 + i * ancho_triangulo
            color = BLANCO if i % 2 == 0 else MARRON_OSCURO
            puntos = [
                (x, 800),
                (x + ancho_triangulo, 800),
                (x + ancho_triangulo // 2, 800 - alto_triangulo)
            ]
            pygame.draw.polygon(self.pantalla, color, puntos)
            pygame.draw.polygon(self.pantalla, NEGRO, puntos, 2)
            
            # Número del punto
            num_punto = 12 - i
            texto = self.fuente_pequena.render(str(num_punto), True, NEGRO)
            self.pantalla.blit(texto, (x + ancho_triangulo // 2 - 8, 770))
        
        # Lado izquierdo inferior: 6-1
        for i in range(6):
            x = 725 + i * ancho_triangulo
            color = BLANCO if i % 2 == 1 else MARRON_OSCURO
            puntos = [
                (x, 800),
                (x + ancho_triangulo, 800),
                (x + ancho_triangulo // 2, 800 - alto_triangulo)
            ]
            pygame.draw.polygon(self.pantalla, color, puntos)
            pygame.draw.polygon(self.pantalla, NEGRO, puntos, 2)
            
            # Número del punto
            num_punto = 6 - i
            texto = self.fuente_pequena.render(str(num_punto), True, NEGRO)
            self.pantalla.blit(texto, (x + ancho_triangulo // 2 - 8, 770))
        
        # Resaltar origen seleccionado
        if self.origen_seleccionado is not None:
            self.resaltar_punto(self.origen_seleccionado, VERDE_CLARO)
        
        # Resaltar destino seleccionado
        if self.destino_seleccionado is not None:
            self.resaltar_punto(self.destino_seleccionado, AMARILLO)
    
    def resaltar_punto(self, punto, color):
        """Resalta un punto del tablero"""
        if punto == 0 or punto == 25:
            return
            
        ancho_triangulo = 75
        alto_triangulo = 280
        
        # Determinar posición del punto
        if 13 <= punto <= 18:  # Lado derecho superior
            i = punto - 13
            x = 200 + i * ancho_triangulo
            puntos = [
                (x, 100),
                (x + ancho_triangulo, 100),
                (x + ancho_triangulo // 2, 100 + alto_triangulo)
            ]
        elif 19 <= punto <= 24:  # Lado izquierdo superior
            i = punto - 19
            x = 725 + i * ancho_triangulo
            puntos = [
                (x, 100),
                (x + ancho_triangulo, 100),
                (x + ancho_triangulo // 2, 100 + alto_triangulo)
            ]
        elif 7 <= punto <= 12:  # Lado derecho inferior
            i = 12 - punto
            x = 200 + i * ancho_triangulo
            puntos = [
                (x, 800),
                (x + ancho_triangulo, 800),
                (x + ancho_triangulo // 2, 800 - alto_triangulo)
            ]
        else:  # 1-6: Lado izquierdo inferior
            i = 6 - punto
            x = 725 + i * ancho_triangulo
            puntos = [
                (x, 800),
                (x + ancho_triangulo, 800),
                (x + ancho_triangulo // 2, 800 - alto_triangulo)
            ]
        
        pygame.draw.polygon(self.pantalla, color, puntos, 5)
    
    def obtener_posicion_ficha(self, punto, indice_ficha):
        """Calcula la posición x, y para dibujar una ficha"""
        ancho_triangulo = 75
        radio_ficha = 28
        
        if punto == 0:  # Barra
            return (700, 200 + indice_ficha * 45)
        elif punto == 25:  # Meta
            return (1250, 450)
            
        # Determinar posición según el punto
        if 13 <= punto <= 18:  # Lado derecho superior
            i = punto - 13
            x = 200 + i * ancho_triangulo + ancho_triangulo // 2
            y = 100 + 70 + indice_ficha * (radio_ficha * 2 + 3)
        elif 19 <= punto <= 24:  # Lado izquierdo superior
            i = punto - 19
            x = 725 + i * ancho_triangulo + ancho_triangulo // 2
            y = 100 + 70 + indice_ficha * (radio_ficha * 2 + 3)
        elif 7 <= punto <= 12:  # Lado derecho inferior
            i = 12 - punto
            x = 200 + i * ancho_triangulo + ancho_triangulo // 2
            y = 800 - 70 - indice_ficha * (radio_ficha * 2 + 3)
        else:  # 1-6: Lado izquierdo inferior
            i = 6 - punto
            x = 725 + i * ancho_triangulo + ancho_triangulo // 2
            y = 800 - 70 - indice_ficha * (radio_ficha * 2 + 3)
            
        return (x, y)
    
    def dibujar_fichas(self):
        board = self.game.get_board()
        radio = 28
        
        # Dibujar fichas en el tablero (puntos 1-24)
        for punto in range(1, 25):
            fichas = board.get_position(punto)
            for idx, ficha in enumerate(fichas):
                x, y = self.obtener_posicion_ficha(punto, idx)
                color = ROJO if ficha.get_jugador() == 1 else AZUL
                pygame.draw.circle(self.pantalla, color, (x, y), radio)
                pygame.draw.circle(self.pantalla, NEGRO, (x, y), radio, 2)
                
                # Símbolo del jugador
                simbolo_texto = "X" if ficha.get_jugador() == 1 else "O"
                simbolo = self.fuente_mediana.render(simbolo_texto, True, BLANCO)
                rect = simbolo.get_rect(center=(x, y))
                self.pantalla.blit(simbolo, rect)
        
        # Dibujar fichas en la barra
        for jugador_num in [1, 2]:
            fichas_barra = board.get_bar(jugador_num)
            for idx, ficha in enumerate(fichas_barra):
                color = ROJO if jugador_num == 1 else AZUL
                y = 200 + idx * 45 if jugador_num == 1 else 700 - idx * 45
                pygame.draw.circle(self.pantalla, color, (700, y), radio)
                pygame.draw.circle(self.pantalla, NEGRO, (700, y), radio, 2)
                simbolo_texto = "X" if jugador_num == 1 else "O"
                simbolo = self.fuente_mediana.render(simbolo_texto, True, BLANCO)
                rect = simbolo.get_rect(center=(700, y))
                self.pantalla.blit(simbolo, rect)
        
        # Dibujar fichas en la meta (lado derecho)
        for jugador_num in [1, 2]:
            fichas_meta = board.get_home(jugador_num)
            color = ROJO if jugador_num == 1 else AZUL
            y_base = 300 if jugador_num == 1 else 600
            
            # Área de meta
            pygame.draw.rect(self.pantalla, GRIS_CLARO, (1220, y_base - 40, 150, 100), 2)
            texto = self.fuente_mediana.render(f"Meta J{jugador_num}", True, color)
            self.pantalla.blit(texto, (1230, y_base - 35))
            texto_num = self.fuente_grande.render(str(len(fichas_meta)), True, color)
            self.pantalla.blit(texto_num, (1270, y_base + 5))
        
        # Texto de barra
        texto_barra = self.fuente_mediana.render("BARRA", True, BLANCO)
        rect = texto_barra.get_rect(center=(700, 450))
        pygame.draw.rect(self.pantalla, MARRON_OSCURO, rect.inflate(10, 5))
        self.pantalla.blit(texto_barra, rect)
    
    def dibujar_info_turno(self):
        jugador = self.game.get_jugador_actual()
        color = ROJO if jugador.get_numero() == 1 else AZUL
        
        texto = self.fuente_grande.render(
            f"Turno: Jugador {jugador.get_numero()} ({jugador.get_ficha()})",
            True, color
        )
        self.pantalla.blit(texto, (500, 30))
    
    def dibujar_dados(self):
        dados = self.game.get_dados_actuales()
        if not dados:
            return
            
        # Panel de dados (lado izquierdo)
        pygame.draw.rect(self.pantalla, GRIS_CLARO, (20, 350, 160, 200))
        pygame.draw.rect(self.pantalla, NEGRO, (20, 350, 160, 200), 3)
        
        # Título
        texto_titulo = self.fuente_mediana.render("Dados:", True, NEGRO)
        self.pantalla.blit(texto_titulo, (45, 360))
        
        # Dibujar dados en 2 columnas
        for idx, dado in enumerate(dados):
            fila = idx // 2
            col = idx % 2
            x = 35 + col * 70
            y = 410 + fila * 70
            
            # Fondo del dado
            pygame.draw.rect(self.pantalla, BLANCO, (x, y, 60, 60))
            pygame.draw.rect(self.pantalla, NEGRO, (x, y, 60, 60), 3)
            
            # Número del dado
            texto = self.fuente_grande.render(str(dado), True, NEGRO)
            rect = texto.get_rect(center=(x + 30, y + 30))
            self.pantalla.blit(texto, rect)
    
    def dibujar_botones(self):
        # Panel de botones (lado izquierdo)
        y_base = 580
        
        # Botón de tirar dados
        if not self.dados_lanzados:
            boton_dados = pygame.Rect(20, 150, 160, 60)
            pygame.draw.rect(self.pantalla, VERDE, boton_dados)
            pygame.draw.rect(self.pantalla, NEGRO, boton_dados, 3)
            texto = self.fuente_mediana.render("Tirar Dados", True, BLANCO)
            rect = texto.get_rect(center=boton_dados.center)
            self.pantalla.blit(texto, rect)
        
        # Botón de pasar turno
        boton_pasar = pygame.Rect(20, y_base, 160, 60)
        pygame.draw.rect(self.pantalla, AMARILLO, boton_pasar)
        pygame.draw.rect(self.pantalla, NEGRO, boton_pasar, 3)
        texto = self.fuente_mediana.render("Pasar", True, NEGRO)
        rect = texto.get_rect(center=boton_pasar.center)
        self.pantalla.blit(texto, rect)
        
        # Botón de limpiar selección
        boton_reset = pygame.Rect(20, y_base + 80, 160, 60)
        pygame.draw.rect(self.pantalla, GRIS, boton_reset)
        pygame.draw.rect(self.pantalla, NEGRO, boton_reset, 3)
        texto = self.fuente_pequena.render("Limpiar", True, BLANCO)
        rect = texto.get_rect(center=boton_reset.center)
        self.pantalla.blit(texto, rect)
        
        # Botón de menú
        boton_menu = pygame.Rect(20, y_base + 160, 160, 60)
        pygame.draw.rect(self.pantalla, ROJO, boton_menu)
        pygame.draw.rect(self.pantalla, NEGRO, boton_menu, 3)
        texto = self.fuente_mediana.render("Menú", True, BLANCO)
        rect = texto.get_rect(center=boton_menu.center)
        self.pantalla.blit(texto, rect)
    
    def dibujar_mensaje(self):
        if self.mensaje and pygame.time.get_ticks() - self.tiempo_mensaje < 3000:
            # Dividir mensaje en líneas
            palabras = self.mensaje.split()
            lineas = []
            linea_actual = ""
            
            for palabra in palabras:
                test_linea = linea_actual + " " + palabra if linea_actual else palabra
                if len(test_linea) > 60:
                    lineas.append(linea_actual)
                    linea_actual = palabra
                else:
                    linea_actual = test_linea
            if linea_actual:
                lineas.append(linea_actual)
            
            # Dibujar fondo
            altura_total = len(lineas) * 35 + 20
            pygame.draw.rect(self.pantalla, GRIS_CLARO, 
                           (ANCHO // 2 - 350, ALTO - altura_total - 20, 700, altura_total))
            pygame.draw.rect(self.pantalla, NEGRO, 
                           (ANCHO // 2 - 350, ALTO - altura_total - 20, 700, altura_total), 3)
            
            # Dibujar líneas
            for i, linea in enumerate(lineas):
                texto = self.fuente_pequena.render(linea, True, NEGRO)
                rect = texto.get_rect(center=(ANCHO // 2, ALTO - altura_total + 10 + i * 35))
                self.pantalla.blit(texto, rect)
    
    def dibujar_menu(self):
        self.pantalla.fill(MARRON_CLARO)
        
        titulo = self.fuente_grande.render("BACKGAMMON", True, NEGRO)
        rect_titulo = titulo.get_rect(center=(ANCHO // 2, 200))
        self.pantalla.blit(titulo, rect_titulo)
        
        # Botón jugar
        boton_jugar = pygame.Rect(ANCHO // 2 - 150, 320, 300, 80)
        pygame.draw.rect(self.pantalla, VERDE, boton_jugar)
        pygame.draw.rect(self.pantalla, NEGRO, boton_jugar, 3)
        texto = self.fuente_grande.render("JUGAR", True, BLANCO)
        rect = texto.get_rect(center=boton_jugar.center)
        self.pantalla.blit(texto, rect)
        
        # Botón ayuda
        boton_ayuda = pygame.Rect(ANCHO // 2 - 150, 440, 300, 80)
        pygame.draw.rect(self.pantalla, AZUL, boton_ayuda)
        pygame.draw.rect(self.pantalla, NEGRO, boton_ayuda, 3)
        texto = self.fuente_grande.render("AYUDA", True, BLANCO)
        rect = texto.get_rect(center=boton_ayuda.center)
        self.pantalla.blit(texto, rect)
        
        # Botón salir
        boton_salir = pygame.Rect(ANCHO // 2 - 150, 560, 300, 80)
        pygame.draw.rect(self.pantalla, ROJO, boton_salir)
        pygame.draw.rect(self.pantalla, NEGRO, boton_salir, 3)
        texto = self.fuente_grande.render("SALIR", True, BLANCO)
        rect = texto.get_rect(center=boton_salir.center)
        self.pantalla.blit(texto, rect)
    
    def dibujar_ayuda(self):
        self.pantalla.fill(MARRON_CLARO)
        
        titulo = self.fuente_grande.render("AYUDA - BACKGAMMON", True, NEGRO)
        self.pantalla.blit(titulo, (ANCHO // 2 - 280, 50))
        
        instrucciones = [
            "OBJETIVO: Mover todas tus fichas a la meta antes que tu oponente",
            "",
            "CONTROLES:",
            "1. Clic en 'Tirar Dados' para comenzar tu turno",
            "2. Clic en un punto para seleccionar ORIGEN (verde)",
            "   - Debe tener tus fichas",
            "   - Si tienes fichas en la barra, debes sacarlas primero (clic en barra)",
            "3. Clic en otro punto para seleccionar DESTINO (amarillo)",
            "   - Punto 25 = sacar ficha del tablero (bearing off)",
            "4. Clic en un DADO disponible para ejecutar el movimiento",
            "",
            "REGLAS:",
            "- Jugador 1 (X/Rojo) avanza de 1 → 24",
            "- Jugador 2 (O/Azul) avanza de 24 → 1",
            "- Puedes capturar fichas enemigas solitarias",
            "- Para sacar fichas (bearing off), todas deben estar en tu casa",
            "  Casa J1: puntos 19-24 | Casa J2: puntos 1-6",
            "- Si sacas dobles (ej: 3-3), tienes 4 movimientos",
        ]
        
        y = 160
        for linea in instrucciones:
            texto = self.fuente_pequena.render(linea, True, NEGRO)
            self.pantalla.blit(texto, (120, y))
            y += 38
        
        # Botón volver
        boton_volver = pygame.Rect(ANCHO // 2 - 120, 780, 240, 70)
        pygame.draw.rect(self.pantalla, VERDE, boton_volver)
        pygame.draw.rect(self.pantalla, NEGRO, boton_volver, 3)
        texto = self.fuente_grande.render("VOLVER", True, BLANCO)
        rect = texto.get_rect(center=boton_volver.center)
        self.pantalla.blit(texto, rect)
    
    def dibujar_ganador(self):
        self.pantalla.fill(MARRON_CLARO)
        
        ganador = self.game.get_ganador()
        color = ROJO if ganador.get_numero() == 1 else AZUL
        
        titulo = self.fuente_grande.render("¡JUEGO TERMINADO!", True, NEGRO)
        rect_titulo = titulo.get_rect(center=(ANCHO // 2, 250))
        self.pantalla.blit(titulo, rect_titulo)
        
        texto_ganador = self.fuente_grande.render(
            f"Ganador: Jugador {ganador.get_numero()} ({ganador.get_ficha()})",
            True, color
        )
        rect_ganador = texto_ganador.get_rect(center=(ANCHO // 2, 350))
        self.pantalla.blit(texto_ganador, rect_ganador)
        
        # Botón volver al menú
        boton_menu = pygame.Rect(ANCHO // 2 - 150, 480, 300, 80)
        pygame.draw.rect(self.pantalla, VERDE, boton_menu)
        pygame.draw.rect(self.pantalla, NEGRO, boton_menu, 3)
        texto = self.fuente_grande.render("MENÚ", True, BLANCO)
        rect = texto.get_rect(center=boton_menu.center)
        self.pantalla.blit(texto, rect)
    
    def obtener_punto_click(self, pos):
        """Determina qué punto del tablero fue clickeado"""
        x, y = pos
        ancho_triangulo = 75
        
        # Verificar barra
        if 675 <= x <= 725 and 100 <= y <= 800:
            return 0
        
        # Parte superior
        if 100 <= y <= 380:
            # Lado derecho: puntos 13-18
            if 200 <= x <= 650:
                i = int((x - 200) / ancho_triangulo)
                if 0 <= i < 6:
                    return 13 + i
            # Lado izquierdo: puntos 19-24
            elif 725 <= x <= 1175:
                i = int((x - 725) / ancho_triangulo)
                if 0 <= i < 6:
                    return 19 + i
        
        # Parte inferior
        elif 520 <= y <= 800:
            # Lado derecho: puntos 12-7
            if 200 <= x <= 650:
                i = int((x - 200) / ancho_triangulo)
                if 0 <= i < 6:
                    return 12 - i
            # Lado izquierdo: puntos 6-1
            elif 725 <= x <= 1175:
                i = int((x - 725) / ancho_triangulo)
                if 0 <= i < 6:
                    return 6 - i
        
        return None
    
    def manejar_click_juego(self, pos):
        # Verificar botón tirar dados
        if pygame.Rect(20, 150, 160, 60).collidepoint(pos) and not self.dados_lanzados:
            valores = self.game.tirar_dados()
            self.dados_lanzados = True
            self.origen_seleccionado = None
            self.destino_seleccionado = None
            self.mensaje = f"Dados lanzados: {valores}"
            self.tiempo_mensaje = pygame.time.get_ticks()
            return
        
        # Verificar botón pasar turno
        if pygame.Rect(20, 580, 160, 60).collidepoint(pos):
            self.game.cambiar_turno()
            self.dados_lanzados = False
            self.origen_seleccionado = None
            self.destino_seleccionado = None
            self.mensaje = "Turno cambiado"
            self.tiempo_mensaje = pygame.time.get_ticks()
            return
        
        # Verificar botón limpiar selección
        if pygame.Rect(20, 660, 160, 60).collidepoint(pos):
            self.origen_seleccionado = None
            self.destino_seleccionado = None
            self.mensaje = "Selección limpiada"
            self.tiempo_mensaje = pygame.time.get_ticks()
            return
        
        # Verificar botón menú
        if pygame.Rect(20, 740, 160, 60).collidepoint(pos):
            self.estado = "MENU"
            self.game = BackgammonGame()
            self.dados_lanzados = False
            self.origen_seleccionado = None
            self.destino_seleccionado = None
            return
        
        if not self.dados_lanzados:
            self.mensaje = "Debes tirar los dados primero"
            self.tiempo_mensaje = pygame.time.get_ticks()
            return
        
        # Verificar si se clickeó un dado
        dados = self.game.get_dados_actuales()
        for idx, dado in enumerate(dados):
            fila = idx // 2
            col = idx % 2
            x = 35 + col * 70
            y = 410 + fila * 70
            rect_dado = pygame.Rect(x, y, 60, 60)
            
            if rect_dado.collidepoint(pos):
                if self.origen_seleccionado is not None and self.destino_seleccionado is not None:
                    try:
                        # Validar dirección del movimiento según el jugador
                        jugador = self.game.get_jugador_actual()
                        origen = self.origen_seleccionado
                        destino = self.destino_seleccionado
                        
                        # Validar dirección según jugador
                        movimiento_valido_direccion = True
                        if origen != 0 and destino != 25:  # No validar si es desde barra o a meta
                            if jugador.get_numero() == 1:
                                # Jugador 1 avanza de menor a mayor (1 → 24)
                                if destino <= origen:
                                    movimiento_valido_direccion = False
                                    self.mensaje = "Jugador 1 (X) debe mover hacia adelante: de puntos menores a mayores (1 → 24)"
                                    self.tiempo_mensaje = pygame.time.get_ticks()
                            else:
                                # Jugador 2 avanza de mayor a menor (24 → 1)
                                if destino >= origen:
                                    movimiento_valido_direccion = False
                                    self.mensaje = "Jugador 2 (O) debe mover hacia adelante: de puntos mayores a menores (24 → 1)"
                                    self.tiempo_mensaje = pygame.time.get_ticks()
                        
                        if not movimiento_valido_direccion:
                            self.origen_seleccionado = None
                            self.destino_seleccionado = None
                            return
                        
                        # Intentar movimiento
                        if self.game.mover_ficha(self.origen_seleccionado, self.destino_seleccionado, dado):
                            self.mensaje = f"Movimiento exitoso: {self.origen_seleccionado} → {self.destino_seleccionado} (dado {dado})"
                            self.tiempo_mensaje = pygame.time.get_ticks()
                            self.origen_seleccionado = None
                            self.destino_seleccionado = None
                            
                            if self.game.juego_terminado():
                                self.estado = "GANADOR"
                            
                            # Verificar si no quedan más dados
                            elif len(self.game.get_dados_actuales()) == 0:
                                self.game.cambiar_turno()
                                self.dados_lanzados = False
                                self.mensaje = "No quedan dados disponibles. Turno cambiado automáticamente."
                                self.tiempo_mensaje = pygame.time.get_ticks()
                        else:
                            self.mensaje = "Movimiento inválido. Verifica las reglas del juego."
                            self.tiempo_mensaje = pygame.time.get_ticks()
                    
                    except Exception as e:
                        self.mensaje = f"Error al realizar movimiento: {str(e)}"
                        self.tiempo_mensaje = pygame.time.get_ticks()
                        self.origen_seleccionado = None
                        self.destino_seleccionado = None
                else:
                    self.mensaje = "Debes seleccionar origen y destino primero"
                    self.tiempo_mensaje = pygame.time.get_ticks()
                return
        
        # Verificar click en punto del tablero
        punto = self.obtener_punto_click(pos)
        
        if punto is not None:
            if self.origen_seleccionado is None:
                # Seleccionar origen
                board = self.game.get_board()
                jugador = self.game.get_jugador_actual()
                
                # Verificar si hay fichas en la barra
                if len(board.get_bar(jugador.get_numero())) > 0:
                    if punto == 0:
                        self.origen_seleccionado = punto
                        self.mensaje = f"Origen seleccionado: BARRA. Ahora selecciona destino"
                        self.tiempo_mensaje = pygame.time.get_ticks()
                    else:
                        self.mensaje = "Tienes fichas en la barra. Debes sacarlas primero (clic en barra)"
                        self.tiempo_mensaje = pygame.time.get_ticks()
                else:
                    # Verificar que el punto tenga fichas del jugador actual
                    fichas = board.get_position(punto)
                    if fichas and fichas[0].get_jugador() == jugador.get_numero():
                        self.origen_seleccionado = punto
                        self.mensaje = f"Origen seleccionado: {punto}. Ahora selecciona destino"
                        self.tiempo_mensaje = pygame.time.get_ticks()
                    else:
                        self.mensaje = f"El punto {punto} no tiene tus fichas"
                        self.tiempo_mensaje = pygame.time.get_ticks()
            
            elif self.destino_seleccionado is None:
                # Seleccionar destino
                self.destino_seleccionado = punto
                self.mensaje = f"Destino seleccionado: {punto}. Ahora selecciona un dado"
                self.tiempo_mensaje = pygame.time.get_ticks()
        
        # Verificar click en zona de meta (bearing off)
        if 1220 <= pos[0] <= 1370 and 100 <= pos[1] <= 800:
            if self.origen_seleccionado is not None and self.destino_seleccionado is None:
                self.destino_seleccionado = 25
                self.mensaje = "Destino: META (bearing off). Ahora selecciona un dado"
                self.tiempo_mensaje = pygame.time.get_ticks()
    
    def ejecutar(self):
        ejecutando = True
        estado_anterior = None
        
        while ejecutando:
            self.reloj.tick(FPS)
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False
                
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    
                    if self.estado == "MENU":
                        if pygame.Rect(ANCHO // 2 - 150, 320, 300, 80).collidepoint(pos):
                            self.estado = "JUGANDO"
                            self.game = BackgammonGame()
                            self.dados_lanzados = False
                            self.origen_seleccionado = None
                            self.destino_seleccionado = None
                        elif pygame.Rect(ANCHO // 2 - 150, 440, 300, 80).collidepoint(pos):
                            estado_anterior = "MENU"
                            self.estado = "AYUDA"
                        elif pygame.Rect(ANCHO // 2 - 150, 560, 300, 80).collidepoint(pos):
                            ejecutando = False
                    
                    elif self.estado == "AYUDA":
                        if pygame.Rect(ANCHO // 2 - 120, 780, 240, 70).collidepoint(pos):
                            self.estado = estado_anterior if estado_anterior else "MENU"
                    
                    elif self.estado == "JUGANDO":
                        self.manejar_click_juego(pos)
                    
                    elif self.estado == "GANADOR":
                        if pygame.Rect(ANCHO // 2 - 150, 480, 300, 80).collidepoint(pos):
                            self.estado = "MENU"
                            self.game = BackgammonGame()
                            self.dados_lanzados = False
                            self.origen_seleccionado = None
                            self.destino_seleccionado = None
            
            # Dibujar según el estado
            if self.estado == "MENU":
                self.dibujar_menu()
            elif self.estado == "AYUDA":
                self.dibujar_ayuda()
            elif self.estado == "JUGANDO":
                self.dibujar_tablero()
                self.dibujar_fichas()
                self.dibujar_info_turno()
                self.dibujar_dados()
                self.dibujar_botones()
                self.dibujar_mensaje()
            elif self.estado == "GANADOR":
                self.dibujar_ganador()
            
            pygame.display.flip()
        
        pygame.quit()

if __name__ == "__main__":
    juego = BackgammonPygame()
    juego.ejecutar()