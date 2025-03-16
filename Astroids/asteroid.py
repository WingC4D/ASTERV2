import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def handle_collision(self, player):
        distance = self.position.distance_to(player.position)
        if distance <= self.radius + player.radius:
            print("Game Over! Player hit an asteroid.")
            pygame.quit()
            return True
        return False
    