import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import DEATH


class Death(Obstacle):
    def __init__(self):
        self.type = 0
        self.float = 0 
        super().__init__(DEATH, self.type)
        self.rect.y = random.randint(295, 300)


    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed 
        self.obs_to_draw = DEATH[0] if self.float < 5 else DEATH[1] 
        self.float += 1
        if self.float >= 5:
            self.float = 0
        
        if self.rect.x < -self.rect.width:
            obstacles.pop() 