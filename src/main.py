import pygame
from pygame.locals import *
from game import *

pygame.init()

debug_collisions = False
clock = pygame.time.Clock()
width = 1080
height = 720    
screen = pygame.display.set_mode((width,height))
game = Game(debug_collisions, screen, width, height, clock)

while game.running:

    game.screen.fill("black")      
    game.update()
    game.draw()
    game.clock.tick(60)

    pygame.display.flip()

pygame.quit()
exit()