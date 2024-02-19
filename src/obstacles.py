import pygame
from dialog import *

class Obstacle(pygame.sprite.Sprite) :
    width = 0
    height = 0        

    image = pygame.rect.Rect(0, 0, 0, 0)

    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)

    def _get_sprite(self):
        image = pygame.Surface((self.width, self.height))
        image.blit(self.image, (0,0), (0, 0, self.width, self.height))
        image = pygame.transform.scale(image, (self.width, self.height))
        return image

    def update(self):
        self.rect.width = self.width
        self.rect.height = self.height

    def draw(self):
        self.image = self._get_sprite()

    def action(self):
        pass 

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Tree(Obstacle):
    def __init__(self):
        Obstacle.__init__(self)
        self.width = 16
        self.height = 16
        self.image = pygame.image.load("./assets/tree-sprite.png")
        self.rect = self.image.get_rect()
    
    def action(self):
        print("Isso é uma arvore!")

class Board(Obstacle):
    def __init__(self, text, game):
        Obstacle.__init__(self)
        self.width = 16
        self.height = 16
        self.image = pygame.image.load("./assets/board-sprite.png")
        self.rect = self.image.get_rect()
        self.text = text
        self.game = game
    
    def action(self):
        self.game.dialog.show_dialog(self.text)