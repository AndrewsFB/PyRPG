import pygame

class Area():
    def __init__(self, objects, width, height):
        self.rect = pygame.rect.Rect(0, 0, width, height)
        self.objects = objects
        self.ready = False

    def update(self):
        if self.ready:
            self.check_collide()
    
    def check_collide(self):
        for object in self.objects:
            if self.rect.colliderect(object.rect):
                self.action()

    def action(self):
        pass

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y    
    
class Warp(Area):
    def __init__(self, game, scene):
        objects = []
        objects.append(game.player)
        Area.__init__(self, objects, 10, 10)
        self.scene = scene
        self.game = game
    
    def action(self):
        self.ready = False
        self.game.change_scene(self.scene)
    
    def copy(self):
        return Warp(self.game, self.scene)