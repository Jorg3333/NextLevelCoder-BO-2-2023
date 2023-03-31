from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING
import pygame 


class Dinosaur(Sprite): 
    
    POS_x = 80
    POS_y = 310
    DUCK_POS = 350
    JUMP_VEL = 8.5
    
    
    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.POS_y
        self.step_index = 0
        self.runnig = True
        self.ducking = False
        self.jumping = False
        self.jump_vel = self.JUMP_VEL
    
    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.POS_y
        self.step_index += 1
    
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.DUCK_POS_Y
        self.step_index += 1
    
    def jump(self): 
        self.image = JUMPING 
        if self.jumping: 
            self.rect.y -= self.jump_vel * 4 
            self.jump_vel -= 0.8 
            if self.jump_vel < -self.JUMP_VEL: 
                self.rect.y = self.POS_Y 
                self.jumping = False 
                self.jump_vel = self.JUMP_VEL
    
    def update(self, user_input):
        if self.jumping:
            self.jump()
        if self.ducking:
            self.duck()
        if self.runnig:
            self.run()
 
        if user_input[pygame.K_DOWN] and not self.jumping:
            self.runnig = False
            self.ducking = False
            self.jumping = True
        elif user_input[pygame.K_UP] and not self.jumping:
            self.running = False
            self.ducking = False
            self.jumping = True
        elif not self.jumping:
            self.running = True
            self.ducking = False
            self.jumping = False
               
        if self.step_index >= 10:
            self.step_index = 0
        
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        