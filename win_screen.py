import pygame
import sys

class WinScreen:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        # Load the font
        self.font = pygame.font.Font("assets/fonts/Planewalker.otf", 64)

        self.score_font_org = pygame.font.Font("assets/fonts/Planewalker.otf", 16)
        self.score_font = self.score_font_org

        # Load the background animation
        self.background_image_original = pygame.image.load(f"assets/images/background2.jpg")
        self.background_image = self.background_image_original
        
        self.wiz_org = pygame.image.load("assets/images/wizard.png")
        self.wiz = self.wiz_org

        self.bubble_org = pygame.image.load("assets/images/speechbubble.png")
        self.bubble = self.bubble_org

        # Set up the buttons
        self.resize_elements()


    def open_win(self, max_towers: int, towers_left: int):
        # Main game loop


        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.resize_elements() 
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.main_menu_button.collidepoint(event.pos):
                        return 0
                    if self.exit_button.collidepoint(event.pos):
                        return -1
                    
            self.resize_elements()
                    
            

            # Draw the background
            self.screen.blit(self.background_image, (0, 0))

            # Draw the buttons
            pygame.draw.rect(self.screen, (255, 255, 255), self.main_menu_button)
            pygame.draw.rect(self.screen, (255, 255, 255), self.exit_button)
            if self.main_menu_button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, (0,0,0), self.main_menu_button,5)
                pygame.mouse.set_cursor(pygame.cursors.diamond)
            elif self.exit_button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, (0,0,0), self.exit_button,5)
                pygame.mouse.set_cursor(pygame.cursors.broken_x)
            else:
                pygame.mouse.set_cursor(pygame.cursors.arrow)

            win_text = self.font.render("You win!", True, (0, 0, 0))
            menu_text = self.font.render("Main menu", True, (0, 0, 0))
            exit_text = self.font.render("Exit", True, (0, 0, 0))
            score_text = self.score_font.render(f"You used {max_towers-towers_left}/{max_towers} towers.", True, (0, 0, 0))

            self.screen.blit(self.wiz, (self.screen.get_width()-self.wiz.get_width(), self.screen.get_height()-self.wiz.get_height()))
            bubble_rect = (self.screen.get_width()-self.bubble.get_width()-self.wiz.get_width()*7/12, self.screen.get_height() - self.wiz.get_height()*5/6 - self.bubble.get_height())
            self.screen.blit(self.bubble, bubble_rect)

            self.screen.blit(win_text, (self.screen.get_width() // 2 - win_text.get_width() // 2, 50))
            self.screen.blit(menu_text, (self.screen.get_width() // 2 - menu_text.get_width() // 2, self.screen.get_height() - 450))
            self.screen.blit(exit_text, (self.screen.get_width() // 2 - exit_text.get_width() // 2, self.screen.get_height() - 200))

            self.screen.blit(score_text,(self.screen.get_width()-self.bubble.get_width()+self.score_font.get_height()-self.wiz.get_width()*7/12, self.screen.get_height() - self.wiz.get_height()*5/6 - self.bubble.get_height()/2-self.score_font.get_height()/2))


            # Update the display
            pygame.display.update()

    def resize_elements(self):
        self.background_image = pygame.transform.scale(self.background_image_original, (self.screen.get_width(), int(self.screen.get_width() / self.background_image_original.get_width() * self.background_image_original.get_height())))
        self.main_menu_button = pygame.Rect(self.screen.get_width() // 2 - 200, self.screen.get_height() - 450, 400, 100)
        self.exit_button = pygame.Rect(self.screen.get_width() // 2 - 200, self.screen.get_height() - 200, 400, 100)
        
        wiz_width = self.screen.get_width()/6
        self.wiz_scaling = wiz_width / self.wiz_org.get_width()
        wiz_height = self.wiz_org.get_height() * self.wiz_scaling
        self.wiz = pygame.transform.scale(self.wiz_org, (int(wiz_width), int(wiz_height)))

        self.bubble = pygame.transform.scale(self.bubble_org, (int(self.screen.get_width()/4), int(self.screen.get_height()/6)))

        self.score_font = pygame.font.Font("assets/fonts/Planewalker.otf", int(self.wiz_scaling*self.score_font_org.get_height()))