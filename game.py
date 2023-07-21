import pygame

from components.power.map import PowerMap
from components.power.pole import PowerPole

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Watt Wizards - The Game")

background_image = pygame.image.load("assets/grass.png").convert() 

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font_path = "assets/fonts/Planewalker.otf"
font = pygame.font.Font(font_path, 24)
text_surface = font.render("Hello World", True, (255, 255, 255))
text_width, text_height = text_surface.get_size()

# Create a sprite group
sprite_group = pygame.sprite.Group()

power_map = PowerMap(background_image, screen)
old_pole = None
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    power_map.draw()

    screen.blit(text_surface, (screen_width - text_width, 0))
    
    # Handle mouse events
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            new_pole = PowerPole(*pygame.mouse.get_pos())
            power_map.add_pole(new_pole)
            if old_pole:
                power_map.grid.add_connection(old_pole, new_pole)
            old_pole = new_pole
            print("Left mouse button clicked at", event.pos)
        elif event.button == 2:  # Middle mouse button
            print("Middle mouse button clicked at", event.pos)
        elif event.button == 3:  # Right mouse button
            print("Right mouse button clicked at", event.pos)

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()
    sprite_group.draw(screen)
    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
