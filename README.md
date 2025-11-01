BACKGAMMON COMPUTACIÓN 2025
Nombre: Lorenzo Giacomelli
Carrera: Ingeniería Informática
Año: 2025

Cómo poner en funcionamiento el juego de Backgammon (comandos a ingresar en la terminal):
Para modo juego:
- CLI: python -m CLI.CLI
- Pygame: python -m UI.PygameUI
Para modo testing:
- Para ejecutar todos los tests juntos: python -m unittest discover -v
- Player: python -m unittest tests.test_player.TestPlayer -v
- Checker: python -m unittest tests.tests_checker.TestChecker -v
- Dice: python -m unittest tests.test_dice.TestDice -v
- Board: python -m unittest tests.tests_board.TestBoard -v
- BackgammonGame: python -m unittest tests.test_backgammon.TestBackgammonGame -v
- CLI: python -m unittest tests.tests_cli.TestBackgammonCLI -v
