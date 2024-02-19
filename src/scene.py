import  pygame
from enum import Enum
from obstacles import *

class Scene():
    def __init__(self, game):
        self.areas = []
        self.obstacles = []
        self.map_bg = pygame.Surface((1080, 720))
        self.map_collisions = pygame.Surface((1080, 720))
        self.map_elements = pygame.Surface((1080, 720))
        self.map_assigns = []
        self.collisions = []
        self.tile_size = 0
        self.width = 0
        self.height = 0
        self.sprites = pygame.sprite.Group() 
        self.game = game
        self.fade_in_frames = 0   
        self.fade_out_frames = 0   
        self.is_fading_in = False    
        self.is_fading_out = False
        
    def update(self):       
        for area in self.areas:
            area.update()
    
    def draw(self):
        self.game.screen.blit(self.map_bg, (0,0))
        self.game.screen.blit(self.map_elements, (0,0))
        self.sprites.draw(self.game.screen)

        self.control_fade_out()
        self.control_fade_in()

    def prepare_map(self):
        for i in range(0, self.width, self.tile_size):
            for j in range(0, self.height, self.tile_size):
                color = self.map_collisions.get_at((i, j))
                for tuple in self.map_assigns:
                    if tuple[0] == color:
                        if(tuple[2] == ObjectType.Copy):
                            area = tuple[1].copy()
                            area.set_position(i, j)
                            self.areas.append(area)                            
                        elif(tuple[2] == ObjectType.Unique):
                            tuple[1].set_position(i, j)
                            self.obstacles.append(tuple[1])
                        break
                if color == (255, 0, 0, 255):
                    self.game.player.set_position((i, j))
                if color == (0, 0, 0, 255):
                    collision = pygame.rect.Rect(0, 0, self.tile_size, self.tile_size)
                    collision.x = i
                    collision.y = j
                    self.collisions.append(collision)
    
    def mark_as_ready(self):
        for area in self.areas:
            area.ready = True        

    def fade_in(self):
        self.is_fading_in = True
        self.fade_in_frames = 30

    def fade_out(self):
        self.is_fading_out = True
        self.fade_out_frames = 0

    def control_fade_in(self):
        if self.is_fading_in:
            if self.fade_in_frames <= 0:
                self.is_fading_in = False
                self.game.paused = False
                self.prepare_map()
            elif self.fade_in_frames >= 1:
                self.fade_in_frames -= 1
                pygame.draw.rect(self.game.screen, (self.fade_in_frames*8, self.fade_in_frames*8, self.fade_in_frames*8, self.fade_in_frames*8), pygame.rect.Rect(0, 0, self.width, self.height))

    def control_fade_out(self):
        if self.is_fading_out:
            if self.fade_out_frames >= 30:
                self.is_fading_out = False
                self.game.paused = False
            elif self.fade_out_frames <= 30:
                self.fade_out_frames += 1
                pygame.draw.rect(self.game.screen, (self.fade_out_frames*8, self.fade_out_frames*8, self.fade_out_frames*8, self.fade_out_frames*8), pygame.rect.Rect(0, 0, self.width, self.height))  

class ObjectType(Enum):
    Unique=0
    Copy=1