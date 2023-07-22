import pygame

from game_state import GameState
from components.buildings.house import House
from components.buildings.power_house import PowerHouse
from components.map import PowerMap
from components.power.pole import PowerPole
from utils import * 
from sound_controller import SoundController

class Game:
    # Initialize the class
    def __init__(self, screen: pygame.Surface):
        # Set up the display
        self.screen = screen
        background_image = pygame.image.load("assets/images/grass.png").convert()
        self.sound_controller = SoundController()
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
        self.sound_controller.stop_music()
        self.sound_controller.start_music()
        self.running = True 
        self.power_map.resize_image(self.screen)
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            self.power_map.draw()
            if self.pole_selection is not None:
                block_width = int(self.screen.get_width()/grid_width)
                block_height = int(self.screen.get_height()/grid_height)
                (x,y) = self.pole_selection.get_position()
                pygame.draw.rect(self.screen, (255, 255, 255), (x * block_width, y * block_height, block_width, block_height), 2)
                pygame.draw.circle(self.screen, (255, 255, 255), (x * block_width + int(block_width/2), y * block_height + int(block_height/2)), int(block_width/2), 2)


            # Get the mouse position
            #mouse_pos = pygame.mouse.get_pos()
            self.sprite_group.draw(self.screen)
            # Update the screen
            pygame.display.flip()
            
            if self.power_map.win_condition_met():
                self.power_map.flush()
                return GameState.GAME_OVER
        return GameState.EXIT
 
    def erect_hice(self, houses: list[House]):
        for house in houses:
            self.power_map.erect_pole(house)
    def flush(self):
        self.power_map.flush()

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            self.quit_game()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(event)
        elif event.type == pygame.VIDEORESIZE:
            self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            self.power_map.resize_image(self.screen)
    
    def handle_mouse_up(self, event: pygame.event.Event):
        mouse_pos = coordinates_to_index(self.screen, *pygame.mouse.get_pos())
        if event.button == 1:
            pole_at_pos = self.power_map.get_node_at(mouse_pos)
            if pole_at_pos is not None:
                if pole_at_pos == self.pole_selection:
                    self.pole_selection = None
                    return
                
                if self.pole_selection is not None:
                    if self.power_map.add_connection(self.pole_selection, pole_at_pos):
                        self.sound_controller.play_sound("connect")
                    else:
                        self.sound_controller.play_sound("fail")
                    self.pole_selection = None
                    return
                    
                self.pole_selection = pole_at_pos
                return
            
             
            new_pole = PowerPole(mouse_pos)
            self.power_map.erect_pole(new_pole)
            self.sound_controller.play_sound("place_pole")
            self.pole_selection = None    
        
        if event.button == 3:
            if self.power_map.remove_node_at(mouse_pos):
                self.sound_controller.play_sound("demolition")
            else:
                self.sound_controller.play_sound("fail")
    
    def quit_game(self):
        print("Goodbye!")
        self.running = False
        
    def get_sound_controller(self):
        return self.sound_controller
