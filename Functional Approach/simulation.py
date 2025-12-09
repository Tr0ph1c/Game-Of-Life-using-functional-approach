import GOL
import pygame
import time

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

    gol_board = {(1,0), (2,1), (0,2), (1,2), (2,2)}

    while True:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                cell_x = mouse_pos[0] // SIZE
                cell_y = mouse_pos[1] // SIZE
                cell = (cell_x, cell_y)
                gol_board.discard(cell) if cell in gol_board else gol_board.add(cell)
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
    next_board = board

    if running:
        next_board = GOL.step(board)

    for (x,y) in next_board:
        pygame.draw.rect(screen, COLOR_ALIVE, (x*SIZE, y*SIZE, SIZE-1, SIZE-1))

    return next_board

if __name__ == '__main__':
    main()