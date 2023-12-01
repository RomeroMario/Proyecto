# Proyecto
Proyecto de fase 1

Juego simple donde se controla un jugador con WASD y se tiene que esquivar obstáculos que van cayendo de forma aleatoria.

Se implementó un menú principal con 2 opciones, botón para jugar donde se selecciona la dificultad y otra opcion con los controles del juego.

La funcionalidad general del juego se basa en un ciclo While en el que se limitan la cantidad de ticks por una variable de FPS, en cada pasada se actualiza la posicion del jugador y de los enemigos según los parámetros que tiene cada uno.

Se implementa un nivel de dificultad que genera más enemigos y les da más velocidad.

Tambien se guarda el score máximo registrado, este valor se resetea a 0 cada vez que se ejecuta el programa.

Se usan los modulos de sys para cerrar la ventana y random para generar aleatoriamente los enemigos.


