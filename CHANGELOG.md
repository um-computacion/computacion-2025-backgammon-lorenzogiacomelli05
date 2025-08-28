# Changelog
Todas las modificaciones importantes de este proyecto se documentarán en este archivo.

## [Unreleased]
- Pendiente: Seguir con las otras clases del proyecto y sus respectivos tests

## [2025-08-27]
### Added
- Primeros tests unitarios con `unittest` para la clase `Dice`:
  - `test_roll_devuelve_lista`: verifica que al tirar los dados se devuelva una lista con 2 o 4 valores.
  - `test_get_values`: verifica que `get_values()` devuelve lo mismo que los valores internos de la clase.
  - `test_tirada_doble`: verifica que `tirada_doble()` funciona correctamente para tiradas dobles y normales.

## [2025-08-28]
### Added
- Más tests unitarios para la clase `Dice`:
  - `test_individual_values`: verifica que `individual_values()` devuelve correctamente 2 valores en caso de tirada doble y los valores originales en tirada normal.
  - `test_usar_valor`: verifica que al usar un valor se mueva de la lista de valores disponibles a la lista de usados.
  - `test_valores_usados`: verifica que los valores usados se guarden correctamente.