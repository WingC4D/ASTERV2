from circleshape import CircleShape
from constants import *
from shot import *
import pygame
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.shots = []  # A list to keep track of shots
        timer = 0 
        self.timer = timer
    #in the Player class
    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius -right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(), width=2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2 (0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self,dt):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED  
            self.shots.append(shot)
            self.timer += 0.3    
    
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_a]:
            self.rotate(dt)
        
        if keys[pygame.K_d]:
            self.rotate(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
