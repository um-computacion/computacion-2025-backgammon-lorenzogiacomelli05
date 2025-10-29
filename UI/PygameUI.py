import pygame
from core.BackgammonGame import BackgammonGame

# --------------------------
# Configuración visual
# --------------------------
WIDTH, HEIGHT = 1000, 700
MARGIN_X, MARGIN_Y = 40, 40

BG_COLOR = (245, 239, 230)
BOARD_COLOR = (230, 220, 200)
TRI_A = (170, 120, 90)
TRI_B = (210, 170, 130)
LINE = (60, 60, 60)
WHITE = (245, 245, 245)
BLACK = (30, 30, 30)
TEXT = (25, 25, 25)
SELECT_COLOR = (255, 100, 100)
VALID_COLOR = (100, 255, 100)
MAX_VISIBLE_STACK = 5

# --------------------------
# Funciones auxiliares
# --------------------------

def point_index_to_display(idx):
    if 0 <= idx <= 11:
        return 'top', 11 - idx
    else:
        return 'bottom', idx - 12

def draw_triangle(surface, board_rect, col_vis, row, color):
    x0 = board_rect.left + col_vis * (board_rect.width / 12.0)
    x1 = x0 + (board_rect.width / 12.0)
    x_mid = (x0 + x1) / 2.0

    if row == 'top':
        tip_y = board_rect.top + board_rect.height * 0.42
        pts = [(x0, board_rect.top), (x1, board_rect.top), (x_mid, tip_y)]
    else:
        tip_y = board_rect.bottom - board_rect.height * 0.42
        pts = [(x0, board_rect.bottom), (x1, board_rect.bottom), (x_mid, tip_y)]
    pygame.draw.polygon(surface, color, pts)

def draw_checker(surface, center, radius, color_rgb, selected=False, valid=False, label=None, font=None):
    pygame.draw.circle(surface, color_rgb, center, radius)
    if selected:
        border_color = SELECT_COLOR
    elif valid:
        border_color = VALID_COLOR
    else:
        border_color = LINE
    pygame.draw.circle(surface, border_color, center, radius, 2)
    if label and font:
        txt = font.render(str(label), True, LINE if color_rgb == WHITE else WHITE)
        rect = txt.get_rect(center=center)
        surface.blit(txt, rect)

# --------------------------
# Clase PygameUI
# --------------------------
class PygameUI:
    def __init__(self, game: BackgammonGame):
        pygame.init()
        self.game = game
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Backgammon (Pygame)")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 20)
        self.hitmap = {}
        self.selected_idx = None
        self.valid_moves = []
        self.selected_dado = None

    # --------------------------
    # Renderizado del tablero
    # --------------------------
    def render_board(self):
        self.screen.fill(BG_COLOR)
        board_rect = pygame.Rect(MARGIN_X, MARGIN_Y + 20, WIDTH - 2 * MARGIN_X, HEIGHT - 2 * MARGIN_Y - 40)
        pygame.draw.rect(self.screen, BOARD_COLOR, board_rect, border_radius=12)
        pygame.draw.rect(self.screen, LINE, board_rect, 2, border_radius=12)

        # Triángulos
        for col_vis in range(12):
            draw_triangle(self.screen, board_rect, col_vis, 'top', TRI_A if col_vis % 2 == 0 else TRI_B)
            draw_triangle(self.screen, board_rect, col_vis, 'bottom', TRI_B if col_vis % 2 == 0 else TRI_A)

        # Fichas
        tri_w = board_rect.width / 12.0
        radius = max(12, min(int(tri_w * 0.38), 22))
        step = radius * 2 + 4

        # Etiquetas de puntos
        for col_vis, lbl in enumerate([str(i) for i in range(12, 0, -1)]):
            x = int(board_rect.left + col_vis * tri_w + tri_w / 2)
            y = board_rect.top - 14
            self.screen.blit(self.font.render(lbl, True, TEXT),
                            self.font.render(lbl, True, TEXT).get_rect(center=(x, y)))
        for col_vis, lbl in enumerate([str(i) for i in range(13, 25)]):
            x = int(board_rect.left + col_vis * tri_w + tri_w / 2)
            y = board_rect.bottom + 14
            self.screen.blit(self.font.render(lbl, True, TEXT),
                            self.font.render(lbl, True, TEXT).get_rect(center=(x, y)))

        pygame.draw.line(self.screen, LINE, (board_rect.left, board_rect.centery),
                        (board_rect.right, board_rect.centery), 1)

        # Dibujar fichas
        self.hitmap = {i: [] for i in range(24)}
        board = self.game.get_board()

        for idx in range(24):
            cell = board.get_position(idx + 1)
            if not cell:
                continue
            color_name = 'white' if cell[0].get_jugador() == 1 else 'black'
            count = len(cell)

            row, col_vis = point_index_to_display(idx)
            cx = int(board_rect.left + col_vis * tri_w + tri_w / 2)
            start_y = int(board_rect.top + radius + 6) if row == 'top' else int(board_rect.bottom - radius - 6)
            step_dir = step if row == 'top' else -step
            visibles = min(count, MAX_VISIBLE_STACK)
            extras = max(0, count - (MAX_VISIBLE_STACK - 1)) if count > MAX_VISIBLE_STACK else 0

            for i in range(visibles):
                cy = start_y + i * step_dir
                label = extras if (extras and i == visibles - 1) else None
                selected = (self.selected_idx == idx)
                valid = (idx in self.valid_moves)
                draw_checker(self.screen, (cx, cy), radius, WHITE if color_name == 'white' else BLACK,
                            selected=selected, valid=valid, label=label, font=self.font)
                self.hitmap[idx].append((cx, cy, radius))

        # Dibujar dados
        dados = self.game.get_dados_actuales()
        x_base, y_base = WIDTH - 140, HEIGHT - 50
        for i, val in enumerate(dados):
            rect = pygame.Rect(x_base + i * 50, y_base, 40, 40)
            color_rect = (150, 255, 150) if self.selected_dado == val else (200, 200, 200)
            pygame.draw.rect(self.screen, color_rect, rect, border_radius=6)
            txt = self.font.render(str(val), True, TEXT)
            self.screen.blit(txt, txt.get_rect(center=rect.center))

        # Mensaje de victoria
        winner = self.game.get_ganador()
        if winner:
            msg = f"Jugador {winner.get_numero()} ganó."
            surf = self.font.render(msg, True, (255, 0, 0))
            self.screen.blit(surf, surf.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

        pygame.display.flip()

    # --------------------------
    # Detección de clics sobre fichas
    # --------------------------
    def hit_test(self, pos):
        mx, my = pos
        for idx, circles in self.hitmap.items():
            for (cx, cy, r) in circles:
                if (mx - cx) ** 2 + (my - cy) ** 2 <= r ** 2:
                    return idx
        return None

    # --------------------------
    # Calcular destinos válidos
    # --------------------------
    def calcular_destinos_validos(self, idx):
        board = self.game.get_board()
        jugador = self.game.get_jugador_actual()
        num_j = jugador.get_numero()
        destinos = []

        origen = idx

        for dado in self.game.get_dados_actuales():
            destino = origen + dado if num_j == 1 else origen - dado
            if 0 <= destino <= 23:
                cell = board.get_position(destino + 1)
                if not cell or cell[0].get_jugador() == num_j or len(cell) == 1:
                    destinos.append(destino)
        return destinos