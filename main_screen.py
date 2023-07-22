from game_state import GameState
import pygame
import sys

class MainMenu:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        # Load the logo
        self.logo = pygame.image.load("assets/images/logo.png")

        # Load the font
        self.font = pygame.font.Font("assets/fonts/Planewalker.otf", 64)

        # Load the background animation
        self.background_image_original = pygame.image.load(f"assets/images/background.png")
        self.background_image = self.background_image_original

        # Set up the buttons
        self.resize_buttons()


    def open_menu(self):
        # Main game loop
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.resize_buttons() 
                    self.background_image = pygame.transform.scale(self.background_image_original, (event.w, event.h))
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.level_1_button.collidepoint(event.pos):
                        return GameState.LEVEL_1
                    if self.level_2_button.collidepoint(event.pos):
                        return GameState.LEVEL_2 
                    if self.exit_button.collidepoint(event.pos):
                        return GameState.EXIT
                    
            self.resize_buttons()
                    
            # Clear the screen
            self.screen.fill((0, 0, 0))

            # Draw the background
            self.screen.blit(self.background_image, (0, 0))

            # Draw the logo
            self.screen.blit(self.logo, (self.screen.get_width() // 2 - self.logo.get_width() // 2, 50))

            # Draw the buttons
            pygame.draw.rect(self.screen, (255, 255, 255), self.level_1_button)
            pygame.draw.rect(self.screen, (255, 255, 255), self.level_2_button)
            pygame.draw.rect(self.screen, (255, 255, 255), self.exit_button)
            level1_text = self.font.render("Level 1", True, (0, 0, 0))
            level2_text = self.font.render("Level 2", True, (0, 0, 0))
            exit_text = self.font.render("Exit", True, (0, 0, 0))
            self.screen.blit(level1_text, (self.level_1_button.centerx - level1_text.get_width() // 2, self.level_1_button.centery - level1_text.get_height() // 2))
            self.screen.blit(level2_text, (self.level_2_button.centerx - level2_text.get_width() // 2, self.level_2_button.centery - level2_text.get_height() // 2))
            self.screen.blit(exit_text, (self.exit_button.centerx - exit_text.get_width() // 2, self.exit_button.centery - exit_text.get_height() // 2))

            # Update the display
            pygame.display.update()

    def resize_buttons(self):
        self.level_1_button = pygame.Rect(self.screen.get_width() // 2 - 200, self.screen.get_height() - 450, 400, 100)
        self.level_2_button = pygame.Rect(self.screen.get_width() // 2 - 200, self.screen.get_height() - 325, 400, 100)
        self.exit_button = pygame.Rect(self.screen.get_width() // 2 - 200, self.screen.get_height() - 200, 400, 100)
