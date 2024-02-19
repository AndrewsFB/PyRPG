import pygame
from scene import *
from area import *

class Scene1(Scene):
    def __init__(self, game):
        Scene.__init__(self, game)  
        self.tile_size = 16
        self.width = 1088
        self.height = 720

        self.map_bg = pygame.image.load("./levels/maps/png/test_map__tiles.png")
        self.map_elements = pygame.image.load("./levels/maps/png/test_map__elements.png")
        self.map_collisions = pygame.image.load("./levels/maps/png/test_map__collisions.png")

        self.map_assigns.append(((107, 107, 107, 255), Board("Isso é uma placa, ignore!", game), ObjectType.Unique))
        self.map_assigns.append(((62, 62, 62, 255), Board("Isso é outra placa, ignore!", game), ObjectType.Unique))
        self.map_assigns.append(((0, 14, 154, 255), Warp(game, self), ObjectType.Copy))

        self.prepare_map()

        self.sprites.add(game.player)

        for obstacle in self.obstacles:
           self.sprites.add(obstacle)
        
        self.mark_as_ready()