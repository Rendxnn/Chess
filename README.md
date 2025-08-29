# Chess (Pygame)

Un juego de ajedrez simple hecho en Python con Pygame. Permite jugar con dos personas en la misma máquina, arrastrando y soltando las piezas sobre un tablero de 8x8. Implementa movimientos legales básicos, enroque y promoción.

<img width="478" height="480" alt="image" src="https://github.com/user-attachments/assets/4ff6618e-8cb8-46c7-8fb9-3b8ada39f005" />


---

## Requisitos

- Python 3.8+ (probado con Python 3.x)
- Pygame 2.x

Instalación de dependencias:

```bash
pip install pygame
```

## Cómo ejecutar

Desde la raíz del proyecto:

```bash
python main.py
```

Si usas un entorno virtual, actívalo antes de ejecutar.

## Controles

- Clic izquierdo sostenido sobre una pieza para seleccionarla y arrastrarla.
- Suelta el clic izquierdo sobre la casilla de destino para intentar mover.
- La ventana se puede cerrar con el botón de cerrar (evento `QUIT`).

## Reglas implementadas

- Movimientos de piezas estándar (peón, torre, caballo, alfil, dama, rey).
- Detección de jaque básico: se impide un movimiento que deje al propio rey en jaque (se revierte el tablero a su estado anterior).
- Enroque (si el rey y la torre no se han movido y no hay piezas entre medio).
- Promoción de peón: al llegar a la última fila aparece un selector para elegir la nueva pieza.

## Estado y limitaciones conocidas

- En passant: el esqueleto existe pero no está implementado completamente.
- No hay detección de jaque mate, tablas, ni fin automático de la partida.
- No se resaltan movimientos legales ni casillas seleccionadas.

## Estructura del código

- `main.py`: bucle principal del juego, entrada del usuario y turnos.
- `window.py`: creación de ventana y rutinas de render (tablero, arrastre, promoción).
- `pieces.py`: clases de piezas y cálculo de movimientos legales; el `King` incluye lógica de jaque.
- `movement.py`: aplica movimientos (incluye enroque y promoción) y valida que no se deje al propio rey en jaque.
- `player.py`: estado por jugador (color y posición del rey).
- `images/`: recursos gráficos (tablero, piezas, panel de promoción).

## Piezas (imágenes)

Imagen general de piezas:

![Piezas](<images/pieces.png>)

Piezas individuales (blancas):

![Rey blanco](<images/white king.png>)
![Dama blanca](<images/white queen.png>)
![Torre blanca](<images/white rook.png>)
![Alfil blanco](<images/white bishop.png>)
![Caballo blanco](<images/white knight.png>)
![Peón blanco](<images/white pawn.png>)

Piezas individuales (negras):

![Rey negro](<images/black king.png>)
![Dama negra](<images/black queen.png>)
![Torre negra](<images/black rook.png>)
![Alfil negro](<images/black bishop.png>)
![Caballo negro](<images/black knight.png>)
![Peón negro](<images/black pawn.png>)

## Detalles de implementación

- Render: se dibuja el fondo del tablero y luego las piezas por fila/columna en múltiplos de 60px.
- Selección/arrastre: al presionar clic izquierdo sobre una pieza del turno actual se quita del tablero temporalmente y se dibuja su sprite siguiendo el ratón hasta soltar.
- Promoción: al promover, se muestra una ventana temporal con 4 opciones (Dama, Torre, Alfil, Caballo) y se reemplaza el peón por la selección elegida.
- Validación de jaque: tras cada movimiento, si el rey del jugador que movió queda en jaque, se revierte el movimiento.
