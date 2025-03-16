import pygame
from constants import *
from player import Player
def main():
    pygame.init()
    clock = pygame.time.Clock() #My time clock object!!
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2,)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    running = True
    #GameLoop Starts Here!
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000 #using the clock object dynamically limit to capture  
                                 #the time between frames and update "dt" with it
        
   

if __name__ == "__main__":
    main()