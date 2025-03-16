import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        for container in self.__class__.containers:
            container.add(self)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius)

    def handle_collision(self, asteroid):
        distance = self.position.distance_to(asteroid.position)
        if distance <= self.radius + asteroid.radius:
            self.kill()
            asteroid.kill()
            return True
        return False