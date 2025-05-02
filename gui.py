# ui.py
import pygame
from constants import* 
import sys

def draw_board(board, screen):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

def show_mode_selection():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Select Game Mode")

    font = pygame.font.SysFont("monospace", 50, bold=True)
    button_font = pygame.font.SysFont("monospace", 35)

    # Colors
    BG_COLOR = (30, 30, 30)
    BUTTON_COLOR = (70, 130, 180)
    HOVER_COLOR = (100, 149, 237)
    TEXT_COLOR = (255, 255, 255)

    # Button dimensions
    button_width = 300
    button_height = 80
    spacing = 40

    center_x = size[0] // 2
    center_y = size[1] // 2

    # Define buttons
    pvp_button = pygame.Rect(center_x - button_width // 2, center_y - button_height - spacing // 2, button_width, button_height)
    ai_button = pygame.Rect(center_x - button_width // 2, center_y + spacing // 2, button_width, button_height)

    while True:
        screen.fill(BG_COLOR)

        # Title
        title_text = font.render("Choose Game Mode", True, TEXT_COLOR)
        screen.blit(title_text, (center_x - title_text.get_width() // 2, 100))

        # Handle hover effect
        mouse_pos = pygame.mouse.get_pos()

        for button, text in [(pvp_button, "Player vs Player"), (ai_button, "Player vs AI")]:
            color = HOVER_COLOR if button.collidepoint(mouse_pos) else BUTTON_COLOR
            pygame.draw.rect(screen, color, button, border_radius=15)
            label = button_font.render(text, True, TEXT_COLOR)
            screen.blit(label, (button.centerx - label.get_width() // 2, button.centery - label.get_height() // 2))

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pvp_button.collidepoint(event.pos):
                    return "pvp"
                elif ai_button.collidepoint(event.pos):
                    return "ai"