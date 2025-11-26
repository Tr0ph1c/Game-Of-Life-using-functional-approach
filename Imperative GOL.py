import pygame
import time
import numpy as np

# constants
SIZE = 50
X_SIZE = 15
Y_SIZE = 15
TICKRATE = .5

# colors
COLOR_BG = (10, 10, 10)
COLOR_ALIVE = (250, 250, 250)
COLOR_DEAD = (30, 30, 30)
COLOR_GRID = (30, 30, 30)

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SIZE*X_SIZE, SIZE*Y_SIZE))
    running = False

    gol_board = np.zeros((X_SIZE, Y_SIZE))

    while True:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                cell_x = mouse_pos[0] // SIZE
                cell_y = mouse_pos[1] // SIZE
                gol_board[cell_x, cell_y] = 1 - gol_board[cell_x, cell_y] # flip 0 to 1 and 1 to 0
                update(gol_board, screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running

        if running:
            gol_board = update(gol_board, screen, True)

            time.sleep(TICKRATE)
        
        screen.fill(COLOR_BG)
        update(gol_board, screen)
        pygame.display.flip()

def update(board, screen, running=False):
    next_board = np.zeros((X_SIZE, Y_SIZE))

    for x, y in np.ndindex(next_board.shape):
        neighbors = np.sum(board[max(x-1,0):x+2, max(y-1,0):y+2]) - board[x][y]
        color = COLOR_ALIVE if board[x, y]==1 else COLOR_DEAD

        if board[x][y] == 1:
            if neighbors < 2 or neighbors > 3:
                if running:
                    color = COLOR_DEAD
                next_board[x][y] = 0
            else:
                if running:
                    color = COLOR_ALIVE
                next_board[x][y] = 1
        else:
            if neighbors == 3:
                if running:
                    color = COLOR_ALIVE
                next_board[x][y] = 1

        pygame.draw.rect(screen, color, (x*SIZE, y*SIZE, SIZE-1, SIZE-1))
        font = pygame.font.SysFont("courier", SIZE//3, bold=True)
        text = font.render(str(neighbors), 1, (50, 200, 200))
        screen.blit(text, (x*SIZE, y*SIZE))

    return next_board

if __name__ == '__main__':
    main()