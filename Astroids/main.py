import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def handle_collisions(player, asteroids, shots):
    for asteroid in asteroids:
        if asteroid.handle_collision(player):
            print("Game Over - Player hit by Asteroid!")
            return "GAME_OVER"  # Let the game loop know the player was hit
        
        for shot in shots:
            if shot.handle_collision(asteroid):
                print(f"Shot hit asteroid at position {asteroid.position}")
                if asteroid.radius > ASTEROID_MIN_RADIUS:
                    new_radius = asteroid.radius - ASTEROID_MIN_RADIUS
                    
                    child_1 = Asteroid(asteroid.position.x, asteroid.position.y, new_radius)
                    child_2 = Asteroid(asteroid.position.x, asteroid.position.y, new_radius)
                    
                    child_1.velocity = asteroid.velocity.rotate(45)
                    child_2.velocity = asteroid.velocity.rotate(-45)
                
                asteroid.kill()
                shot.kill()
    return None 

def main():
    pygame.init()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    clock = pygame.time.Clock() #My time clock object!!
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2,)     
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    running = True
    #GameLoop Starts Here!
    while running:
        dt = clock.tick(60)/1000 #using the clock object dynamically limit to capture  
                                 #the time between frames and update "dt" with it      
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                print("Game Over!")
                running =False
                
        if not running:
            break

        pygame.Surface.fill(screen, BLACK)
        updatable.update(dt)
        collison_result = handle_collisions(player, asteroids, shots)
        if collison_result == "GAME_OVER":
            print("You Suck An ASSteroid Killed you!")
            running = False
            continue
        
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()