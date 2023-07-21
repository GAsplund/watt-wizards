import pygame

from components.buildings.house import House
from components.map import PowerMap
from components.power.pole import PowerPole
from utils import coordinates_to_index


class Game:
    # Initialize the class
    def __init__(self, screen: pygame.Surface):
        # Set up the display
        self.screen = screen
        background_image = pygame.image.load("assets/grass.png").convert() 

        # Set up the clock
        self.clock = pygame.time.Clock()

        # Set up the font
        font_path = "assets/fonts/Planewalker.otf"
        self.font = pygame.font.Font(font_path, 24)
        self.text_surface = self.font.render("Hello World", True, (255, 255, 255))
        self.text_width, self.text_height = self.text_surface.get_size()

        # Create a sprite group
        self.sprite_group = pygame.sprite.Group()

        self.power_map = PowerMap(background_image, screen)

    def start_game_loop(self):
        self.pole_selection = None
        
        self.running = True 
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            self.power_map.draw()

            # Get the mouse position
            #mouse_pos = pygame.mouse.get_pos()
            self.sprite_group.draw(self.screen)
            # Update the screen
            pygame.display.flip()
 
    def add_houses(self, houses: list[House]):
        self.power_map.add_houses(houses)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.quit_game()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(event)
        elif event.type == pygame.VIDEORESIZE:
            self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    
    def handle_mouse_up(self, event: pygame.event.Event):
        mouse_pos = coordinates_to_index(self.screen, *pygame.mouse.get_pos())
        if event.button == 1:
            pole_at_pos = self.power_map.get_pole_at(mouse_pos)
            if pole_at_pos is not None:
                print("Pole at pos")
                if pole_at_pos == self.pole_selection:
                    self.pole_selection = None
                    return
                
                if self.pole_selection is not None:
                    self.power_map.grid.add_connection(self.pole_selection, pole_at_pos)
                    self.pole_selection = None
                    return
                    
                self.pole_selection = pole_at_pos
                return
                
            new_pole = PowerPole(*mouse_pos)
            self.power_map.add_pole(new_pole)
            self.pole_selection = None    
        
        if event.button == 3:
            self.power_map.remove_pole_at(mouse_pos)
    
    def quit_game(self):
        print("Goodbye!")
        self.running = False

if __name__ == "__main__":
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Watt Wizards - The Game")

    game = Game(screen)

    houses = [House(5,5),House(10,2)]
    game.add_houses(houses)
    game.start_game_loop()

    pygame.quit()