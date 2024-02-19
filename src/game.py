import pygame
from player import *
from obstacles import *
from scenes.scene1 import *

class Game():
    running = True
    paused = False

    def __init__(self, debug_collisions, screen, width, height, clock):  
        self.clock = clock
        self.width = width
        self.height = height    
        self.screen = screen
        self.debug_collisions = debug_collisions     

        self.dialog = Dialog(self)
        self.player = Player()
        self.scene = Scene1(self)

    def update(self):
        if self.paused:
            return

        if not self.dialog.is_showing_dialog:        
            keys = pygame.key.get_pressed()
            self.input_pressed(keys)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.input(event.key)    

        self.scene.update()
        self.player.update()
        self.dialog.update()
    
    def draw(self):
        self.scene.draw()
        self.player.draw()  
        self.dialog.draw()

        if(self.debug_collisions):
            pygame.draw.rect(self.screen, "red", self.player.collision_rect)     
            for obstacle in self.scene.obstacles:
                pygame.draw.rect(self.screen, "blue", obstacle.rect)     
            for collision in self.scene.collisions:
                pygame.draw.rect(self.screen, "green", collision)        
            for area in self.scene.areas:
                pygame.draw.rect(self.screen, "black", area)   

    def input(self, key):
        if key == pygame.K_SPACE:
            self.player.interact(self.scene)
            self.dialog.interact()
    
    def input_pressed(self, keys):
        if keys[pygame.K_RIGHT]:
            self.player.move((1, 0), self.scene)
        elif keys[pygame.K_LEFT]:
            self.player.move((-1, 0), self.scene)
        elif keys[pygame.K_UP]:
            self.player.move((0, -1), self.scene)            
        elif keys[pygame.K_DOWN]:
            self.player.move((0, 1), self.scene)
    
    def change_scene(self, scene):
        self.paused = True
        self.scene.fade_out()
        self.scene = scene
        self.scene.fade_in()