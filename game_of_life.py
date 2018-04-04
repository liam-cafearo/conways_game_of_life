import random
import sys

import pygame

from colours import dark_blue, green, black
# challenge module
from patterns import glider, rPentomino, dieHard


def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))

# challenge code
def getPatternCells(pattern):
    # set all to False
    cells = {(c, r): False for c in range(columns) for r in range(rows)}

    # print glider
    # print glider[0]

    # Loop through the pattern string
    for idx, g in enumerate(pattern):

        # print "Index: %s" % idx
        # print "Number: %s" % g
        # Then loop through 5 x 5 mini-grid
        # for col in range(5):
        if g == "1":
            cells[(idx % 5, idx // 5)] = True
    
    #for x in range(5):
        # for y in range(5)
            # print("(" + str(y) + ", " + str(x) + ") : "),
            # print cells[(y, x)]
    
    return cells


def draw_cells():
    for (x, y) in cells:
        colour = green if cells[x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, colour, rectangle)


def get_neighbours((x, y)):
    positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                 (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
    return [cells[r, c] for (r, c) in positions if 0 <= r < rows and 0 <= c < columns]


def evolve():
    global cells

    newCells = cells.copy()

    for position, alive in cells.items():
        live_neighbours = sum(get_neighbours(position))
        if alive:
            if live_neighbours < 2 or live_neighbours > 3:
                newCells[position] = False
        elif live_neighbours == 3:
            newCells[position] = True
    cells = newCells 


def get_cells(density=0.2):
    return {(c, r): random.random() < density for c in range(columns) for r in range(rows)}


pygame.init()

columns, rows = 50, 50
# cells = get_cells()
# cells = getPatternCells(glider)
cells = getPatternCells(dieHard)

cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

speed = 2
rate = 0.5

while True:
    # Check which keys are pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        # Increasing the clock tick speed moves the game faster
        speed += rate
    elif keys[pygame.K_DOWN]:
        # Reducing the clock tick speed moves the game slower
        speed -= rate

    print "Clock speed: %s" % speed
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_cells()
    evolve()
    draw_grid()

    pygame.display.update()