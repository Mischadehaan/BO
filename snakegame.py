from microbit import *
import random

snake = [(2, 4)]
direction = 0
score = 1
food = (1,1)
delay = 1000
running = True

while running:
    # dit is de input
    direction = (direction + 4 - button_a.get_presses()) % 4
    direction = (direction + button_b.get_presses()) % 4

    # hier kijkt hij welke kant je op wil
    x, y = snake[0]

    if (direction == 0):
        if (y != 0):
            snake.insert(0, (x, y - 1))
        else:
            snake.insert(0, (x, 4))
    elif (direction == 1):
        if (x != 4):
            snake.insert(0, (x + 1, y))
        else:
            snake.insert(0, (0, y))
    elif (direction == 2):
        if (y != 4):
            snake.insert(0, (x, y + 1))
        else:
            snake.insert(0, (x, 0))
    elif (direction == 3):
        if (x != 0):
            snake.insert(0, (x - 1, y))
        else:
            snake.insert(0, (4, y))

    # hier checkt hij hoeveel van die bolletjes je eet
    if (food == (x, y)):
        score += 1
        food = (random.randrange(5), random.randrange(5))

        if (delay >= 500):
            delay = delay - 50
    else:
        snake.pop()

    # hier checkt hij of je botst
    for point in snake[1:]:
        if (point == snake[0]):
            running = False

    # hier reset hij de game als je dood bent
    display.clear()
    for point in snake:
        display.set_pixel(point[0], point[1], 9)

    display.set_pixel(food[0], food[1], 9)

    sleep(delay)
