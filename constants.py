# constants.py

import pygame

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Board dimensions
ROW_COUNT = 6
COLUMN_COUNT = 7

# Game pieces
PLAYER = 0
AI = 1
EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

# Scoring
WINDOW_LENGTH = 4

# Pygame settings
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)

# Fonts
pygame.font.init()
FONT = pygame.font.SysFont("monospace", 75)
