import pygame
import sys

width = 640
haight = 480

screen = pygame.display.set_mode((width, haight))
screen.fill((246, 147, 48))
pygame.display.set_caption("Bucle básico")

pygame.init()

gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    pygame.display.flip() # refrescar imagen

pygame.quit()