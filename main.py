import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True  # Control the loop with a variable
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.quit()  # After exiting the loop, quit Pygame

if __name__ == "__main__":
    main()

