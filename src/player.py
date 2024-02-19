import pygame

class Player(pygame.sprite.Sprite) :
    left_sprite_index = [(0, 1), (1, 1), (2, 1)]
    up_sprite_index = [(0, 3), (1, 3), (2, 3)]
    down_sprite_index = [(0, 0), (1, 0), (2, 0)]
    right_sprite_index = [(0, 2), (1, 2), (2, 2)]

    last_move = (0, 0)
    velocity = 5

    position_x = -100
    position_y = -100
    width = 32
    height = 32        

    is_walking = True

    anim_walk_frames = 0
    anim_walk_limit = 30
    anim_walk_pace = 10
    anim_walk_sprites = 3
    anim_walk_current_sprite = 1

    collision_rect = pygame.rect.Rect(0, 0, (width-10), (height-5))

    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = pygame.image.load("./assets/people-sheet-8-bits.png").convert_alpha()
        self.image = self._get_sprite(self.down_sprite_index[0])
        self.rect = self.image.get_rect()

    def _get_sprite(self, frame):
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        image.fill(0)
        image.blit(self.spritesheet, (0,0), (frame[0]*self.width, frame[1]*self.height, self.width, self.height))
        return image

    def update(self):
        self._animate()
        self.rect.x = self.position_x
        self.rect.y = self.position_y
        self.collision_rect.x = self.position_x + 10
        self.collision_rect.y = self.position_y +5
        self.is_walking = False

    def draw(self):
        pass        

    def _animate(self):
        sprite_frame = (0,0)
        if self.last_move == (1,0):
            sprite_frame = self.right_sprite_index[self.anim_walk_current_sprite-1]
        elif self.last_move == (-1,0):
            sprite_frame = self.left_sprite_index[self.anim_walk_current_sprite-1]
        elif self.last_move == (0,1):
            sprite_frame = self.down_sprite_index[self.anim_walk_current_sprite-1]
        elif self.last_move == (0,-1):
            sprite_frame = self.up_sprite_index[self.anim_walk_current_sprite-1]        

        if self.is_walking:
            self.anim_walk_frames += 1
            if self.anim_walk_frames % self.anim_walk_pace == 0 :
                self.anim_walk_current_sprite += 1
                if self.anim_walk_current_sprite >= self.anim_walk_sprites :
                    self.anim_walk_current_sprite = 0

        self.image = self._get_sprite(sprite_frame)
        self.rect = self.image.get_rect()   

    def _check_collide(self, move, obstacles):
        old_position = (self.collision_rect.x, self.collision_rect.y)
        self.collision_rect.x += move[0] 
        self.collision_rect.y += move[1]
        collides = []
        for obstacle in obstacles:
            if self.collision_rect.colliderect(obstacle):
                collides.append(obstacle)
        self.collision_rect.x = old_position[0]
        self.collision_rect.y = old_position[1]
        return collides

    def interact(self, scene):
        obstacles = self._check_collide((self.last_move[0] * self.velocity, self.last_move[1] * self.velocity), scene.obstacles)
        if len(obstacles) == 1:
            obstacles[0].action()

    def move(self, move, scene):
        velocity = self.velocity
        self.last_move = move
        obstacle_collides = self._check_collide((move[0] * velocity, move[1] * velocity), scene.obstacles)
        map_collides = self._check_collide((move[0] * velocity, move[1] * velocity), scene.collisions)
        if len(obstacle_collides) == 0 and len(map_collides) == 0:
            self.is_walking = True
            self.position_x += move[0] * velocity
            self.position_y += move[1] * velocity
    
    def set_position(self, position):
        self.position_x = position[0]
        self.position_y = position[1]        