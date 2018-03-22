import sys

import pygame

import random

from colours import dark_blue


def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))


def get_cells(population=100):
    cells = {(c, r): False for c in range(columns) for r in range(rows)}
    for i in range(population):
        col = random.randint(0, columns)
        row = random.randint(0, rows)
        cells[col, row] = True
    return cells


pygame.init()

columns, rows = 100, 50
cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_grid()

    pygame.display.update()