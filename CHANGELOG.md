# Changelog
Todas las modificaciones importantes de este proyecto se documentarán en este archivo.

## [Unreleased]
- Pendiente: Implementar CLI completo y gráficos con Pygame.
- Pendiente: Refactorizar el resto de clases y sus tests de acuerdo con los principios SOLID

## [2025-09-26]
### Refactorización de Dice
- Se refactorizó la clase `Dice` siguiendo los principios SOLID. 
### Tests de Dice
- Se validan tiradas dobles y no dobles.  
- Se prueba el uso correcto e incorrecto de valores (`usar_valor`).  
- Se comprueba que `individual_values()` siempre devuelva exactamente dos valores.  
- Se asegura que `valores_usados()` refleje correctamente los valores utilizados.  


## [2025-09-25]
### Added
- Refactorización y Tests: Player y Board: Refactorizada la clase `Board` y `Player`, siguiendo los principios SOLID.
- Implementados tests unitarios para `Board`y `Player`

## [2025-09-24]
### Added
- Refactorización y Tests: Checker: Refactorizada la clase `Checker`, siguiendo los principios SOLID.
- Implementados tests unitarios para `Checker`:
  - Verificación del jugador asignado.
  - Estados iniciales correctos (ni en barra ni en meta).
  - Métodos de cambio de estado (`mandar_a_barra`, `sacar_de_barra`, `mandar_a_meta`).
  - Casos de transición entre barra y meta.

## [2025-09-23]
### Added
- Nuevos tests de integración en `test_backgammon`:
  - `test_tirar_y_mover_ficha_integra`: simula una tirada y movimiento válido consumiendo un dado.
  - `test_cambiar_turno_y_tirar_dados`: verifica que el cambio de turno y nueva tirada funcionen correctamente.
  - `test_estado_juego_no_rompe`: asegura que `estado_juego()` no arroje excepciones al ejecutarse.

## [2025-09-22]
### Added
- Cambios y modificaciones de clases Board y BackgammonGame y sus respectivas clases de tests unitarios.

## [2025-09-21]
### Added
- Tests unitarios básicos de la clase `BackgammonGame`:
  - `test_turno_inicial`: verifica que el juego inicia con el turno del jugador 1.
  - `test_cambiar_turno`: verifica que el turno cambia correctamente entre jugadores.
  - `test_tirar_dados_devuelve_valores`: verifica que los dados devuelven valores válidos (1–6).
  - `test_direccion_movimiento`: verifica que cada jugador tiene la dirección correcta.
  - `test_posicion_casa`: verifica que la casa de cada jugador esté en el rango correcto.

## [2025-09-19]
### Updated
- Clase `BackgammonGame`:
  - Se completó la implementación de la lógica general del juego.
  - Ahora controla todas las reglas base de Backgammon (turnos entre jugadores, movimiento de fichas, reentrada desde la barra obligatoria, lógica de dados, incluyendo tiradas dobles).
    - Condiciones de victoria (todas las fichas en casa y metidas en meta).
  - Métodos principales finalizados: `jugar_turno()`, `mover_ficha()`, `tirar_dados()`, `estado_juego()`, `juego_terminado()`.

## [2025-09-18]
### Updated
- Arreglos en clase BackgammonGame

## [2025-09-16]
### Updated
- Arreglos en clase Board y BackgammonGame

## [2025-09-13]
### Updated
- Integración de la clase `Checker` en el proyecto:
  - Clase `Board`:
    - Las fichas ahora son objetos `Checker` en lugar de strings `'X'` / `'O'`.
    - `__positions__` almacena listas de `Checker`.
    - `__bar__` y `__home__` se organizan por jugador (1 y 2) y contienen `Checker`.
    - Método `display()` actualizado para mostrar `jugador(cantidad)` usando `Checker.get_jugador()`.
  - Se asegura que todos los atributos internos usan prefijo y sufijo doble `__atributo__`.
  - Métodos de `Board` y `display()` ajustados para trabajar con objetos `Checker`.

## [2025-09-12]
### Updated
- Arreglos generales de todas las clases y algunas clases de tests (`Board`, `Dice`, `Player`, `Checker`, `BackgammonGame`):
  - Todos los atributos internos ahora usan prefijo y sufijo doble guion bajo `__atributo__`.
  - Se asegura que los atributos solo se accedan mediante `self`.
- Clase `BackgammonGame`:
  - Se ajustaron los atributos internos: `__board__`, `__players__`, `__dice__`, `__turno__`, `__dados_actuales__`.
  - Se agregó método `jugar_turno()` para manejar un turno completo de jugador (tirar dados, mover ficha, cambiar turno).
  - Se agregaron docstrings completos para todos los métodos.

## [2025-09-11]
### Updated
- Tests unitarios de la clase `Board`:
  - Se actualizaron para reflejar la nueva forma de mostrar las fichas (`X(n)` / `O(n)`).
  - Se agregaron docstrings y comentarios aclaratorios en los tests.

## [2025-09-10]
### Updated
- Clase `Board`:
  - Se corrigió el método `display()`:
    - Ahora las fichas se muestran en formato compacto `X(n)` / `O(n)`.
    - Se ajustó la alineación horizontal para que cada posición quede directamente debajo de su número, sin corrimientos.
  - Se simplificó la impresión del tablero en la terminal para mejorar la lectura durante el juego y las pruebas.

## [2025-09-08]
### Added
- Clase `BackgammonGame` (esqueleto inicial):
  - Controla flujo general del juego: tablero (`Board`), jugadores (`Player`), dados (`Dice`) y turnos.
  - Métodos principales:
    - `get_jugador_actual()`: devuelve el jugador actual según el turno.
    - `cambiar_turno()`: cambia el turno al otro jugador.
    - `tirar_dados()`: tira los dados y muestra resultados.
    - `mover_ficha(origen, destino)`: mueve una ficha en el tablero.
    - `estado_juego()`: muestra el estado actual del tablero.
    - `juego_terminado()`: Acá va a ir la condición de victoria.

## [2025-09-07]
### Added
- Tests unitarios para la clase `Checker`:
  - `test_get_jugador`: verifica que `get_jugador()` devuelve el jugador correcto.
  - `test_inicial_no_barra_meta`: verifica que al crear una ficha no está en barra ni en meta.
  - `test_mandar_a_barra`: verifica que `mandar_a_barra()` pone la ficha en la barra y no en la meta.
  - `test_sacar_de_barra`: verifica que `sacar_de_barra()` saca la ficha de la barra.
  - `test_mandar_a_meta`: verifica que `mandar_a_meta()` pone la ficha en la meta y no en la barra.

## [2025-09-06]
### Added
- Clase `Checker`:
  - Atributos: `jugador`, `en_barra`, `en_meta`.
  - Métodos: `get_jugador()`, `esta_en_barra()`, `esta_en_meta()`, `mandar_a_barra()`, `sacar_de_barra()`, `mandar_a_meta()`.

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
  - `test_usar_valor`: verifica que al usar un valor se mueva de la lista de valores disponibles a la lista de usados.
  - `test_valores_usados`: verifica que los valores usados se guarden correctamente.
  - `test_str`: verifica que `__str__` devuelve el string esperado de los valores de los dados.

## [2025-08-27]
### Added
- Primeros tests unitarios con `unittest` para la clase `Dice`:
  - `test_roll_devuelve_lista`: verifica que al tirar los dados se devuelva una lista con 2 o 4 valores.
  - `test_get_values`: verifica que `get_values()` devuelve lo mismo que los valores internos de la clase.
  - `test_tirada_doble`: verifica que `tirada_doble()` funciona correctamente para tiradas dobles y normales.
