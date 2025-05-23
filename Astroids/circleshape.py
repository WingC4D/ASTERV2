import pygame
#Base Class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        #for later
        if hasattr (self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
    
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
    #OverRide This!!!!
        pass

    def update(self, dt):
    #OverRide This!!!
        pass
    
    def handle_collision(self, other):
        distance = self.position.distance_to(other.position)
        if distance <= self.radius + other.radius:
            print("Collision Detected!")
            return True 
        return False