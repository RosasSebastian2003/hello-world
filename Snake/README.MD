---
# Snake Game

Juego sencillo de snake implementado con la libreria turtle, la serpiente es el cuadro de color azul marino, y su comida es el cuadro de color verde, mientras mas comida atrape la serpiente, mas larga se vuelve. El juego terminara si la serpiente choca con la pared, o consigo misma
---
## Controles

Puedes controlar la dirección de la serpiente con las teclas de flecha:

- **Derecha**: Mueve la serpiente hacia la derecha.
- **Izquierda**: Mueve la serpiente hacia la izquierda.
- **Arriba**: Mueve la serpiente hacia arriba.
- **Abajo**: Mueve la serpiente hacia abajo.
---

### Información del Alumno

En la pantalla se mostrará la información del alumno en la posición actual de la cabeza de la serpiente. La información incluye el nombre del alumno y su número de estudiante.


```Python
writer = Turtle()
tracer(False)

def maya():
    pass

def info_alumnos(posX, posY):
    maya()
    writer.clear()
    writer.hideturtle()
    writer.up()
    writer.goto(posX, posY)
    writer.color('#fffae6')
    writer.write('Sebastian Rosas Maciel A01233989', align='left', font=('Arial', 15, 'normal'))


```
---

### Mover a la Serpiente

La serpiente se mueve mediante la funcion move, esta cambia su posicion mediante la funcion change, la cual cambia las coordenadas x e y mediante entradas recibidas desde las teclas de flecha del teclado

```Python
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y
```

Simpultaneamente, se revisa si la serpiemte colisiona con los limites del canvas, consigo misma, o con la comida 
```Python
def move():
    """
    Move the snake forward one segment.

    If the snake's head is outside the game area or collides with its body, the game ends.
    If the snake's head collides with the food, the snake grows and the food is placed in a new location.
    """
    
    head = snake[-1].copy()
    head.move(aim)
    
    global counter
    counter += 1
    
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        moveFood()
    else:
        snake.pop(0)
    
    if counter % 10 == 0:
        moveFood()
    
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'white')

    square(food.x, food.y, 9, '#ffb90f')
    
    info_alumnos(head.x, head.y)
    update()
    ontimer(move, 100)
```
---
### Cambiar la Posicion de la Comida

La comida se mueve aleatoriamente en la pantalla, y cada 10 movimientos de la serpiente, se coloca en una nueva ubicación.
- Se crea una copia de la posición actual de la comida utilizando el método `copy()`
- Se elige aleatoriamente un número entre 0 y 3, estos numeros decidiran si la comida se movera hacia arriba, abajo, izquierda, o derecha
- Dependiendo de la salida, se le suma o resta a la propiedad .x e .y de la posicion de la comida
- Se verifica que la comida no se genere dentro de la serpiente, o fuera de el canvas
- Cambia la posicion de la comida

```Python
def moveFood():
    while True:
        food_aux = food.copy()
        move_direction = randrange(0, 4)  

        if move_direction == 0:
            food_aux.x += 10
        elif move_direction == 1:
            food_aux.x -= 10
        elif move_direction == 2:
            food_aux.y += 10
        elif move_direction == 3:
            food_aux.y -= 10

        if inside(food_aux) and food_aux not in snake:
            break

    food.x = food_aux.x
    food.y = food_aux.y
```
---
### Funciones de Turtle

## bgcolor()

Se utiliza para cambiar el color del fondo del canvas generado, para poder utilizarlo, necesitamos crear un objeto de tipo Scree(), despues de esto, podremos utilizar el metodo bgcolor, este recibe como parametro un string el cual debe de contener el nombre de un color predefinido dentro de turtle, o un codigo hexagecimal.
```Python
#Creamos un objeto Screen() al asignarlo a una variable
screen = Screen()

#Llamamos al metodo bgcolor() sobre el objeto screen que creamos
screen.bgcolor('Black')
```

## clear()

Se utiliza para eliminar objetos dentro canvas creado, este es un metodo de los objetos Turlte(), un ejemplo de su uso se encuentra dentro de la funcion info_alumnos(), esta se utiliza al inicio de la funcion para eliminar el tag (texto con los datos del alumno) anterior con el fin de el tag pueda seguir a la serpiente sin que se acomulen un monton de lineas en el canvas

```Python
def info_alumnos(posX, posY):
    maya()
    writer.clear()
    writer.hideturtle()
    writer.up()
    writer.goto(posX, posY)
    writer.color('#fffae6')
    writer.write('Sebastian Rosas Maciel A01233989', align='left', font=('Arial', 15, 'normal'))

```
---
![](https://github.com/RosasSebastian2003/EntregaST12_23/blob/main/Gifs/ezgif.com-video-to-gif-2.gif)
