JUSTIFICACIÓN BACKGAMMON COMPUTACIÓN 2025

1. Resumen del diseño general

- El proyecto implementa un juego de Backgammon completo en Python siguiendo principios de diseño orientado a objetos y arquitectura modular. El sistema está estructurado en seis clases principales que se distribuyen en dos capas bien diferenciadas:
- Capa de lógica del juego (Core): BackgammonGame: Maneja flujo principal del juego. Board: Gestión del tablero y posiciones. Checker: Representación de fichas individuales. Dice: Manejo de dados y tiradas. Player: Representación de jugadores

- CLI: Interfaz de línea de comandos
- También se añadió una interfaz gráfica jugable con Pygame

Esta separación permite que la lógica del juego sea completamente independiente de la interfaz. El diseño aplica el patrón de separación de responsabilidades donde cada clase tiene un propósito único y bien definido, comunicándose a través de interfaces públicas claras.

2. Justificación de clases y responsabilidades

- BackgammonGame. Responsabilidad: Actúa como controlador central del juego, coordinando todos los componentes y validando las reglas de Backgammon. Justificación: Esta clase es necesaria como punto de orquestación porque el Backgammon requiere validaciones complejas que involucran múltiples componentes (tablero, dados, jugadores). Por ejemplo, la validación de un movimiento debe verificar:. disponibilidad de dados, fichas en la barra (prioridad obligatoria), posiciones válidas según el jugador, condiciones de bearing off (todas las fichas en casa) y capturas de fichas oponentes

- Board. Responsabilidad: Gestión de la estructura física del tablero, incluyendo las 24 posiciones, barra y home de cada jugador. Justificación: El tablero es una estructura de datos que requiere: Inicialización con configuración estándar (8 posiciones específicas con cantidades variables de fichas), manipulación atómica de fichas (añadir/sacar sin inconsistencias), gestión de tres zonas diferentes: tablero, barra y home. Método display() para visualización que recorre 24 posiciones en dos direcciones

- Checker. Responsabilidad: Representar una ficha individual y su estado (tablero/barra/meta). Justificación: Modelarla como objeto aporta ventajas cruciales: Validación de integridad: El constructor valida que solo existan fichas de jugador 1 o 2. Máquina de estados: Una ficha tiene tres estados mutuamente excluyentes que deben mantenerse consistentes (los métodos mandar_a_barra() y mandar_a_meta() garantizan esta exclusividad). Trazabilidad: Los métodos esta_en_barra(), esta_en_meta(), esta_en_tablero() permiten consultas claras sin exponer la implementación interna. Sin esta clase, tendríamos que gestionar estados booleanos dispersos o usar estructuras de datos menos expresivas, aumentando la posibilidad de errores.

- Dice. Responsabilidad: Gestionar las tiradas de dados y la lógica de dobles.
Justificación: Los dados en Backgammon tienen comportamiento especial que justifica una clase dedicada: Regla de dobles: Cuando ambos dados muestran el mismo valor, el jugador puede usar ese valor cuatro veces (no dos). Gestión de valores usados: Necesario para validar que no se use el mismo dado dos veces. La aleatoriedad y lógica de dados está aislada del resto del juego. El método get_values() retorna una lista que puede tener 2 o 4 elementos según si hay doble, lo cual es fundamental para BackgammonGame que itera sobre estos valores. Sin Dice, tendríamos código de generación aleatoria y validación de dobles disperso en BackgammonGame, violando el principio de responsabilidad única.

- Player. Responsabilidad: Almacenar información básica de un jugador (número y símbolo de ficha). Justificación: Aunque es la clase más simple del sistema, Player es necesaria por: Inmutabilidad: Los atributos de un jugador no cambian durante el juego. Identificación única: Proporciona un identificador consistente (1 o 2) usado en todo el sistema. Extensibilidad: Facilita agregar atributos futuros (nombre, puntuación, estadísticas) sin modificar otras clases. Los métodos direccion_movimiento() y posicion_casa() en BackgammonGame reciben objetos Player, lo que hace el código más legible que recibir enteros.

- CLI. Responsabilidad: Gestionar toda la interacción con el usuario a través de la terminal. Justificación: La separación de la interfaz es fundamental por: Testabilidad: Permite probar la lógica del juego sin interacción humana usando mocks. Centraliza el manejo de errores de entrada (valores no numéricos, comandos inválidos). Todos los mensajes y formatos de visualización están en un solo lugar. El método ejecutar_turno() implementa un ciclo complejo de solicitud de entrada, validación y retroalimentación que sería imposible de probar eficientemente si estuviera mezclado con la lógica del juego.

3. Justificación de atributos

- BackgammonGame: 

__board__: Board. Almacena el estado completo del tablero (24 posiciones + barra + home)
Necesario porque cada operación de movimiento debe consultar y modificar múltiples posiciones. Evita pasar el tablero como parámetro en cada método

__players__: list[Player]. Lista de exactamente dos jugadores. Permite alternar turnos con aritmética simple: 1 - self.__turno__. 

__dice__: Dice. Gestiona tiradas y valores disponibles. Centraliza la lógica de dobles que afecta el número de movimientos posibles. Mantiene estado entre llamadas (valores disponibles vs usados)

__turno__: int. Índice (0 o 1) que indica el jugador actual. Más eficiente que almacenar referencia al jugador. Facilita cambio de turno con operación simple

__dados_actuales__: list[int]. Lista mutable que se reduce a medida que se usan dados. Permite validar en mover_ficha() si un dado está disponible. Longitud de la lista indica cuántos movimientos quedan

__dados_usados__: list[int]. Historial de dados ya utilizados en el turno actual. Se reinicia en cambiar_turno() junto con __dados_actuales__

- Board
__positions__: list[list[Checker]]. Lista de 25 elementos (índice 0 sin usar, 1-24 son posiciones válidas). Cada posición es una lista de fichas. Estructura permite operaciones O(1) para acceso por posición. La última ficha en cada lista (pos[-1]) es la que está "arriba" y puede moverse

__bar__: dict[int, list[Checker]]. Diccionario con claves 1 y 2 (jugadores)
Cada jugador tiene su propia barra independiente. Usar diccionario (no lista) hace más expresivo el código: self.__bar__[jugador]

__home__: dict[int, list[Checker]]. Análogo a __bar__, almacena fichas que salieron del tablero. La condición de victoria es len(self.__home__[jugador]) == 15. Separar home de posiciones normales evita confusiones (home no es una posición jugable)

- Checker
__jugador__: int. Identifica al propietario de la ficha (1 o 2). Validado en __init__ para garantizar solo valores 1 o 2

__en_barra__: bool. Indica si la ficha está capturada. Necesario porque las fichas en barra tienen reglas especiales (deben reentrar antes de otros movimientos). Mutuamente excluyente con __en_meta__

__en_meta__: bool. Indica si la ficha salió del juego (bearing off exitoso). Las fichas en meta no pueden moverse nuevamente. Parte de la condición de victoria

- Dice. 
__valores__: list[int]. Valores actuales disponibles de los dados. Puede tener longitud 2 (tirada normal) o 4 (doble). Se reduce con remove() cuando se usa un valor

__usados__: list[int]. Registro de valores ya consumidos. Permite reconstruir la secuencia de movimientos. Se reinicia en cada nueva tirada

- Player
__numero__: int. Identificador único (1 o 2). Usado en todo el sistema para indexar estructuras (__bar__[numero], __home__[numero]). Define dirección de movimiento y posiciones de casa

__ficha__: str. Símbolo visual para el jugador ("X" o "O"). Usado en display() para mostrar a quién pertenece cada posición. Mejora legibilidad de la salida del CLI

- CLI
__game__: BackgammonGame. Referencia a la instancia del juego. El CLI solo se comunica con el juego a través de esta referencia. Permite reiniciar el juego creando una nueva instancia (self.__game__ = BackgammonGame())

4. Excepciones y manejo de errores

- Validación en construcción
Checker.__init__

if jugador not in (1, 2):
    raise ValueError("El jugador debe ser 1 o 2")
Justificación: El constructor es el punto de entrada único para crear fichas. Validar aquí garantiza que nunca exista una ficha inválida en el sistema. ValueError es apropiado porque el error está en el valor del parámetro, no en el estado del sistema.

- Manejo de entrada inválida
BackgammonCLI.ejecutar_turno
try:
    origen = int(origen_input)
    destino = int(destino_input)
    dado = int(dado_input)
except ValueError:
    print("Entrada inválida. Solo se permiten números enteros.")
    continue
except Exception as e:
    print(f"Error: {str(e)}")
Justificación: ValueError captura específicamente errores de conversión de string a int. Exception genérico captura errores inesperados sin crashear el juego. El continue permite reintentar sin perder el turno. 

- Validación de movimientos
BackgammonGame.mover_ficha
El método retorna bool en lugar de lanzar excepciones. Justificación: Los movimientos inválidos son parte del flujo normal del juego (no son excepcionales). Las validaciones son múltiples y secuenciales: Fichas en barra → movimiento obligatorio desde barra. Dado no disponible → movimiento inválido. Posición origen vacía o con fichas enemigas → inválido. Destino bloqueado → inválido. Bearing off sin permiso → inválido. Cada validación fallida ejecuta un return False

- Operaciones seguras
Board.sacar_ficha
if 1 <= pos <= 24 and self.__positions__[pos]:
    return self.__positions__[pos].pop()
return None
Justificación: En lugar de lanzar IndexError o ValueError, retorna None para indicar ausencia de fichas.

- Manejo de comandos especiales
BackgammonCLI.procesar_comando
if comando == "salir":
    print("\nJuego interrumpido por el usuario.")
    return False
El retorno de False señala al que debe terminar el programa. Esto evita usar sys.exit() directamente, facilitando testing (ver test_turno_salir que verifica SystemExit).


5. Estrategias de testing y cobertura

- Arquitectura de testing
El proyecto implementa testing unitario con 150+ tests distribuidos en 6 archivos de test, uno por cada clase principal. La estrategia sigue estos principios:
Aislamiento con Mocks: TestBackgammonCLI usa unittest.mock extensivamente:
def setUp(self):
    self.cli = BackgammonCLI()
    self.cli.__game__ = MagicMock()  # Mock del juego completo
Justificación: El CLI debe probarse sin ejecutar juegos reales. Los mocks permiten simular cualquier estado del juego (victoria, empate, fichas en barra). Verificar que el CLI llame a los métodos correctos del juego. Probar manejo de errores sin generar errores reales. Tests extremadamente rápidos (no hay I/O real ni lógica de juego)

- Cobertura de estados: TestChecker prueba la máquina de estados completa: Estado inicial (tablero). Transición a barra. Transición de barra a tablero. Transición a meta. Transiciones cruzadas (barra → meta, meta → barra). Múltiples transiciones al mismo estado. Cada test verifica los tres estados booleanos (esta_en_barra(), esta_en_meta(), esta_en_tablero()) para garantizar exclusividad mutua.

- Cobertura de reglas de negocio

TestBackgammonGame incluye tests específicos para cada regla de Backgammon:
Prioridad de barra:
def test_mover_ficha_con_fichas_en_barra_intento_desde_tablero(self):
    board.mandar_a_barra(1, Checker(1))
    board.añadir_ficha(8, Checker(1))
    resultado = game.mover_ficha(8, 11, 3)
    assert resultado == False  # No puede mover desde tablero si hay fichas en barra
Bearing off:
def test_bear_off_sin_poder_hacerlo(self):
    board.añadir_ficha(20, Checker(1))  # En casa
    board.añadir_ficha(10, Checker(1))  # Fuera de casa
    resultado = game.mover_ficha(20, 25, 5)
    assert resultado == False  # No puede hacer bearing off
Capturas:
def test_mover_ficha_captura(self):
    # Setup: ficha oponente sola en destino
    # Assert: ficha oponente va a barra

- Cobertura de límites y casos extremos
TestBoard:
def test_get_position_posicion_invalida(self):
    self.assertEqual(self.board.get_position(0), [])   # Índice 0
    self.assertEqual(self.board.get_position(25), [])  # Fuera de rango
    self.assertEqual(self.board.get_position(-1), [])  # Negativo
TestDice fuerza condiciones específicas:
def test_tirada_doble_devuelve_cuatro_valores(self):
    while True:
        valores = self.dice.roll()
        if valores[0] == valores[1]:  # Forzar doble
            self.assertEqual(len(valores), 4)
            break
Justificación: Los dados son aleatorios, pero las reglas no lo son. El while loop garantiza probar el caso de doble aunque tome múltiples iteraciones.

- Cobertura de entrada de usuario: TestBackgammonCLI usa @patch para simular entrada:

@patch("builtins.input", side_effect=["1","6","3",""])
def test_turno_valido(self, mock_input):
    # Simula: origen=1, destino=6, dado=3, Enter para continuar

También prueba comandos especiales:
@patch("builtins.input", side_effect=["salir"])
def test_turno_salir(self, mock_input):
    with self.assertRaises(SystemExit):
        self.cli.ejecutar_turno()

- Testing de inicialización
TestBoard.test_inicializacion_tablero verifica las 8 posiciones con fichas:
self.assertEqual(len(self.board.get_position(1)), 2)   # 2 fichas en 1
self.assertEqual(len(self.board.get_position(6)), 5)   # 5 fichas en 6
... etc para todas las posiciones iniciales
Justificación: La configuración inicial es crítica. Un error aquí invalida todo el juego.

- Testing de métodos de visualización
TestBoard incluye tests para display():
def test_display_no_crash(self):
    try:
        self.board.display()
    except Exception as e:
        self.fail(f"display() causó una excepción: {e}")
Justificación: Aunque display() solo imprime, es importante verificar que no crashea con ninguna configuración del tablero.

- Estrategias avanzadas
Testing de integraciones: Aunque la mayoría de tests son unitarios, algunos tests de BackgammonGame son de integración porque prueban la interacción entre Game, Board y Checker:
def test_mover_ficha_desde_barra_jugador_1(self):
    game = BackgammonGame()
    board = game.get_board()
    board.mandar_a_barra(1, Checker(1))  # Afecta Board
    game.__dados_actuales__ = [3]  # Afecta Game
    resultado = game.mover_ficha(0, 22, 3)  # Integración
    assert resultado == True

- Testing con fixtures: setUp() en cada clase de test crea objetos limpios para cada test, garantizando independencia (un test no puede afectar a otro).

- Testing de representación:
def test_repr_en_barra(self):
    ficha = Checker(1)
    ficha.mandar_a_barra()
    representacion = repr(ficha)
    self.assertIn("estado=barra", representacion)
Prueba que __repr__() ayude en debugging.

6. Cumplimiento de principios SOLID

- S - Single Responsibility Principle (Principio de Responsabilidad Única). Definición: Una clase debe tener una sola razón para cambiar. Implementación en el proyecto: BackgammonGame - Su única responsabilidad es orquestar el flujo del juego y validar reglas. No se encarga de: Renderizar la interfaz (delegado a CLI). Gestionar posiciones del tablero (delegado a Board). Generar números aleatorios (delegado a Dice). Ejemplo concreto: Si cambian las reglas de bearing off, solo se modifica BackgammonGame.puede_bear_off() y mover_ficha(). No afecta a otras clases. Board - Única responsabilidad: gestionar la estructura de datos del tablero. No valida si un movimiento es legal (eso es de BackgammonGame). No decide turnos. No interactúa con el usuario Checker - Única responsabilidad: mantener el estado de una ficha individual. Los métodos son puramente sobre estado interno. Violación evitada: Sin este principio, podríamos tener un método Board.es_movimiento_valido() que mezclaría lógica de estructura de datos con reglas de juego.

- O - Open/Closed Principle (Abierto/Cerrado). Definición: Las entidades de software deben estar abiertas para extensión, cerradas para modificación. Implementación en el proyecto:
Extensión de Dice sin modificación: Supongamos que queremos agregar dados de 8 caras para una variante:
class Dice8Sides(Dice):
    def roll(self):
        d1 = random.randint(1, 8)
        d2 = random.randint(1, 8)
        # Resto igual...
No necesitamos modificar la clase base Dice. Los métodos get_values(), usar_valor(), etc. siguen funcionando.
Extensión de Player sin modificación:
Podemos agregar un jugador con IA sin cambiar Player:
class AIPlayer(Player):
    def __init__(self, numero, ficha, difficulty):
        super().__init__(numero, ficha)
        self.difficulty = difficulty
    
    def choose_move(self, board, dados):
        # Lógica de IA
Protección contra modificación: Los atributos privados (con __) impiden que código externo modifique el estado interno de forma inconsistente. Por ejemplo, no se puede hacer: checker.__en_barra__ = True  # AttributeError. Se debe usar: checker.mandar_a_barra()  # Método público que mantiene consistencia. 

- L - Liskov Substitution Principle (Sustitución de Liskov)
Definición: Los objetos de una subclase deben poder reemplazar a los de la superclase sin alterar el comportamiento del programa. Implementación en el proyecto: Aunque el proyecto no usa herencia extensivamente, el principio se cumple en el diseño de interfaces:
Player es intercambiable:
def direccion_movimiento(self, jugador: Player) -> int:
    return 1 if jugador.get_numero() == 1 else -1
Este método funciona con cualquier objeto que implemente get_numero(). Si creáramos AIPlayer(Player) o RemotePlayer(Player), funcionaría sin cambios.
Checker es intercambiable:
board.añadir_ficha(pos, ficha: Checker)
Cualquier objeto Checker funciona en esta operación, independientemente de su estado interno (__en_barra__, __en_meta__).
Cumplimiento implícito: El sistema usa composición más que herencia (Board tiene Checkers, no es un tipo de Checker), lo cual reduce riesgos de violación de Liskov.

- I - Interface Segregation Principle (Segregación de Interfaces). Definición: Los clientes no deben depender de interfaces que no usan. Implementación en el proyecto: Interfaces mínimas por clase, Checker expone solo lo necesario:
get_jugador() - Para identificación. esta_en_barra(), esta_en_meta(), esta_en_tablero() - Para consultas de estado. mandar_a_barra(), sacar_de_barra(), mandar_a_meta() - Para cambios de estado. No hay métodos innecesarios. Board tiene dos interfaces conceptuales: Para manipulación de fichas: añadir_ficha(), sacar_ficha(), get_position(). Para operaciones especiales: mandar_a_barra(), sacar_de_barra(), mandar_a_meta(). Para visualización: display()
Cada cliente usa solo lo que necesita. Por ejemplo, BackgammonGame.mover_ficha() nunca llama a display().
Evita interfaces gordas:
No existe una clase TableroCompleto con métodos como: Violación de ISP
class TableroCompleto:
    def mover_y_visualizar_y_validar_y_contar_y_estadisticas(...)
En su lugar, cada responsabilidad está en su clase apropiada.

- D - Dependency Inversion Principle (Inversión de Dependencias). Definición: Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones. Implementación en el proyecto: CLI depende de abstracción (BackgammonGame), no de implementaciones:
class BackgammonCLI:
    def __init__(self):
        self.__game__ = BackgammonGame()  # Depende de la interfaz pública
El CLI nunca accede directamente a: Board.__positions__ . Checker.__en_barra__ . Dice.__valores__ . Solo usa métodos públicos: game.get_board(). game.mover_ficha(). game.tirar_dados()

