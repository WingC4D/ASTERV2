import pygame
from constants import *
from player import *
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Initialize pygame once
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # Initialize delta time
    # Create player ONCE here
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Game logic (will add more later)

        # Draw everything
        screen.fill((0, 0, 0))  # Black color
        player.draw(screen)
        pygame.display.flip()
        
        # Control frame rate and get dt
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
    
    # Quit pygame properly
    pygame.quit()

if __name__ == "__main__":
    main()