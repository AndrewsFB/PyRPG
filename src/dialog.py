import pygame

class Dialog(pygame.sprite.Sprite):
    text = ""
    is_showing_dialog = False
    dialog_frames = 0
    dialog_cooldown = 0

    def __init__(self, game):
        self.width = 1000
        self.height = 200
        self.color = "black"
        self.image = pygame.rect.Rect(40, 500, 0, self.height)
        self.rect = self.image
        self.game = game
        self.font = pygame.font.SysFont("Monospace", 20, True, True)

    def update(self):
        if self.is_showing_dialog:
            self.dialog_frames += 1
            self.dialog_cooldown += 1

    def draw(self):
        if self.is_showing_dialog:
            if self.dialog_frames % 2 == 0:
                self.rect.width = self.dialog_frames*100
            if self.rect.width > self.width:
                self.rect.width = self.width
            self.rect.left = 550 - self.rect.width
            if self.rect.left <= 40:
                self.rect.left = 40
            pygame.draw.rect(self.game.screen, self.color, self) 
            if self.rect.width == self.width:
                self.format = self.font.render(self.text, False, (255, 255, 255))
                self.game.screen.blit(self.format, (50, 510))

    def show_dialog(self, text):
        self.text = text
        self.is_showing_dialog = True
    
    def interact(self):
        if self.is_showing_dialog and self.dialog_cooldown > 10:
            self.is_showing_dialog = False
            self.rect.width = 0
            self.dialog_cooldown = 0  
            self.dialog_frames = 0      
