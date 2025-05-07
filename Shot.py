from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.shot_radius = SHOT_RADIUS
        #Speed of the shot in pixels per second
        

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.shot_radius)

    def update(self, dt):
        # Update the position of the shot
        self.position += self.velocity * dt