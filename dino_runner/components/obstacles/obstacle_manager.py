import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Bird
from dino_runner.components.obstacles.death import Death
from dino_runner.components.obstacles.cranium import Cranium
import pygame


class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        self.sound = pygame.mixer.Sound("sounds/choque.mp3")
            
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacle_type_list = [Cactus(), Bird(), Death(), Cranium()]
            self.obstacles.append(random.choice(self.obstacle_type_list))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                if not game.player.shield:
                   if not game.player.has_lives:
                    game.player_heart_manager.reduce_heart_count() #vidas descontando

                    self.sound.play()
                    self.sound.set_volume(0.5)

                    if game.player_heart_manager.heart_count > 0:
                       game.player.has_lives = True
                       self.obstacles.pop()
                       start_transition_time = pygame.time.get_ticks()
                       game.player.lives_transition_time = start_transition_time + 1000

                    else:
                        # pygame.time.delay(1000)
                        game.playing = False 
                        game.death_count += 1# contador
                        game.player_heart_manager.heart_count = 6
                        break 

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
