import pygame
from core.BackgammonGame import BackgammonGame
from UI.PygameUI import PygameUI

# Cómo funciona:
# Click en dado: selecciona qué dado usar para mover.
# Click en ficha: selecciona la ficha a mover y muestra destinos válidos.
# Click en destino válido: mueve la ficha según el dado seleccionado.
# Espacio: tira nuevos dados.

def main():
    game = BackgammonGame()
    ui = PygameUI(game)

    # Tirar dados inicial
    game.tirar_dados()
    ui.valid_moves = []

    running = True
    while running:
        ui.render_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                # Selección de dado
                x_base, y_base = 860, 650
                dados = game.get_dados_actuales()
                for i, dado in enumerate(dados):
                    rect = pygame.Rect(x_base + i * 50, y_base, 40, 40)
                    if rect.collidepoint(pos):
                        ui.selected_dado = dado
                        break
                else:
                    # Selección de ficha
                    idx = ui.hit_test(pos)
                    if idx is not None:
                        ui.selected_idx = idx
                        ui.valid_moves = ui.calcular_destinos_validos(idx)
                    else:
                        # Selección de destino válido
                        for dest in ui.valid_moves:
                            for (cx, cy, r) in ui.hitmap[dest]:
                                mx, my = pos
                                if (mx - cx) ** 2 + (my - cy) ** 2 <= r ** 2:
                                    if ui.selected_dado is not None and ui.selected_idx is not None:
                                        try:
                                            game.mover_ficha(ui.selected_idx + 1, dest + 1, ui.selected_dado)
                                        except Exception as e:
                                            print(f"No se puede mover: {e}")
                                        ui.selected_idx = None
                                        ui.valid_moves = []
                                        ui.selected_dado = None
                                    break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Tirar dados nuevos
                    game.tirar_dados()
                    ui.selected_idx = None
                    ui.valid_moves = []
                    ui.selected_dado = None

        ui.clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()