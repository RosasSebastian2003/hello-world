from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

global counter 
counter = 0

screen = Screen()
screen.bgcolor('Black')

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

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

#2o lapicero
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

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()