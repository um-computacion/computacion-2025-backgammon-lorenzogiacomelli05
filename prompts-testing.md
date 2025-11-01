1. PROMPT PARA CREACION TESTS BOARD: 
- Herramienta: GPT-5
- Prompt: Necesito que me expliques qué tendria que testear de mi clase Board. 
- Respuesta: (cada test con sus respectivas explicaciones de para qué sirve y por qué se usa)
test_inicializacion_tablero
test_añadir_y_sacar_ficha
test_sacar_ficha_vacia
test_set_posicion
test_mandar_y_sacar_de_barra
test_mandar_a_meta
test_vaciar_fichas

- Se realizaron estos tests. (tests/tests_board.py)

2. PROMPT PARA CREACIÓN DE TESTS DE PLAYER
- Herramienta: GPT-5
- Prompt: Necesito que me expliques qué tengo que probar con los tests unitarios para mi clase Player (pego la clase en el chat)
- Respuesta: (Explicación de cada test unitario (qué prueba, por qué y cómo)) 
test_get_numero
test_get_ficha
test_jugadores_distintos
test_reutilizacion_numero_y_ficha

- Se realizaron esos mismos tests unitarios.  (tests/test_player.py)

3.  PROMPT PARA CREACIÓN DE TESTS DE CHECKER
- Herramienta: GPT-5
- Prompt: Necesito que me expliques qué y como testear mis funciones de Checker
- Respuesta: (Explicación de cada test unitario) 
test_jugador_asignado_correctamente
test_estado_inicial
test_mandar_a_barra
test_sacar_de_barra
test_mandar_a_meta
test_cambio_estado_barra_a_meta
test_cambio_estado_meta_a_barra

- Se realizaron esos mismos tests unitarios.  (tests/tests_checker.py)