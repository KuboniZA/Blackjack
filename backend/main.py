import pygame
from blackjack_engine import GameEngine

pygame.init()

game = GameEngine()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blackjack")
GREEN = (53, 101, 77)

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        WIN.fill(GREEN)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()