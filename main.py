# main.py
import pygame
import sys
import numpy as np
from board import *
from game_logic import winning_move
from ai import minimax
from constants import* 
from ui import draw_board, show_mode_selection

# Main function to run the game
def main():
    pygame.init()
    screen = pygame.display.set_mode(size)  # Use the updated screen size
    draw_board(np.zeros((ROW_COUNT, COLUMN_COUNT)), screen)
    pygame.display.update()

    mode = show_mode_selection()  # Get the game mode
    board = create_board()
    game_over = False
    turn = 0

    draw_board(board, screen)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                color = RED if turn == 0 else YELLOW
                pygame.draw.circle(screen, color, (posx, int(SQUARESIZE / 2)), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                col = int(posx / SQUARESIZE)

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)

                    if mode == "pvp" or (mode == "ai" and turn == 0):
                        drop_piece(board, row, col, PLAYER_PIECE if turn == 0 else AI_PIECE)

                        if winning_move(board, PLAYER_PIECE if turn == 0 else AI_PIECE):
                            label = FONT.render("Player {} wins!".format(1 if turn == 0 else 2), True, RED if turn == 0 else YELLOW)
                            screen.blit(label, (40, 10))
                            game_over = True

                    draw_board(board, screen)

                    turn += 1
                    turn %= 2

        # AI Turn
        if mode == "ai" and turn == 1 and not game_over:
            col, _ = minimax(board, 4, -np.inf, np.inf, True)
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    label = FONT.render("AI wins!", True, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

                draw_board(board, screen)

                turn = 0

        if game_over:
            pygame.display.update()
            pygame.time.wait(3000)

if __name__ == "__main__":
    main()
