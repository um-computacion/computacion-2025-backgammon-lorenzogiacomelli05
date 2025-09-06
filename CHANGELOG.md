# Changelog
Todas las modificaciones importantes de este proyecto se documentarán en este archivo.

## [Unreleased]
- Pendiente: Seguir con la clase Checker y sus respectivos tests

## [2025-09-06]
### Added
- Clase `Checker`:
  - Atributos: `ficha` (representa el tipo de ficha) y `posicion` (posición actual en el tablero).
  - Métodos básicos:
    - `get_ficha()`: devuelve la ficha.
    - `get_posicion()`: devuelve la posición actual.
    - `set_posicion(posicion)`: actualiza la posición de la ficha.

## [2025-09-05]
### Added
- Tests unitarios para la clase `Player`:
  - `test_get_numero`: verifica que `get_numero()` devuelve correctamente el número del jugador.
  - `test_get_ficha`: verifica que `get_ficha()` devuelve correctamente la ficha del jugador.

## [2025-09-03]
### Added
- Clase `Player`:
  - Atributos: `numero` (1 o 2) y `ficha` ('X' u 'O').
  - Métodos: `get_numero()` y `get_ficha()`.

## [2025-09-01]
### Added
- Tests unitarios para la clase `Board`:
  - `test_get_position_valida`: verifica que `get_position()` devuelve una lista en una posición válida (forma simple, tipo principiante).
  - `test_get_position_invalida`: verifica que `get_position()` devuelve lista vacía si la posición es inválida.
  - `test_posicion_vacia`: verifica que `posicion_vacia()` devuelve True para posiciones vacías y False para ocupadas.
  - `test_contar_fichas`: verifica que `contar_fichas()` devuelve la cantidad correcta de fichas en la posición.
  - `test_añadir_ficha`: verifica que `añadir_ficha()` agrega correctamente una ficha.
  - `test_sacar_ficha`: verifica que `sacar_ficha()` elimina una ficha correctamente.
  - `test_sacar_ficha_vacio`: verifica que `sacar_ficha()` devuelve None si la posición está vacía.

## [2025-08-30]
### Added
- Clase `Board` (mejorada):
  - Métodos para consultar el tablero: `get_position(pos)`, `posicion_vacia(pos)`, `contar_fichas(pos)`.
  - Métodos para modificar el tablero: `añadir_ficha(pos, ficha)`, `sacar_ficha(pos)`.
  - Mantiene el método `display()` para mostrar el tablero en la terminal con posiciones y cantidad de fichas.

## [2025-08-29]
### Added
- Clase `Board`:
  - Representación del tablero en la terminal con las fichas en posiciones de inicio.
  - Método `display()` para mostrar tablero.

## [2025-08-28]
### Added
- Más tests unitarios para la clase `Dice`:
  - `test_individual_values`: verifica que `individual_values()` devuelve correctamente 2 valores en caso de tirada doble y los valores originales en tirada normal.
  - `test_usar_valor`: verifica que al usar un valor
