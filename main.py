import pygame
from main_screen import MainMenu
from win_screen import WinScreen
from game import Game
from components.buildings.house import House
from components.buildings.power_house import PowerHouse
from components.boulder import Boulder

state = 0

if __name__ == "__main__":
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Watt Wizards - The Game")

    game = Game(screen)
    
    ### LEVELS ###
    stons = [Boulder((5,5)),Boulder((3,2)),Boulder((7,12))]


    power_hice_lvl1 = PowerHouse.create_power_houses([(3,3),(3,12),(16,3),(16,12)])
    drain_hice_lvl1 = House.create_houses([(6,0),(13,0),(0,5),(3,5),(6,5),(13,5),(16,5),(19,5),(0,9),(3,9),(6,9),(13,9),(16,9),(19,9),(6,14),(13,14)])

    power_hice_lvl2 = PowerHouse.create_power_houses([(1,1),(11,12), (15,10)])
    drain_hice_lvl2 = House.create_houses([(1,12),(11,1),(5,5),(10,2),(2,10),(4,9),(3,3),(9,12),(14,13),(17,7),(19,3)])
    
    levels = {
        1: power_hice_lvl1+drain_hice_lvl1+stons,
        2: power_hice_lvl2+drain_hice_lvl2+stons
    }

    menu = MainMenu(screen)
    win = WinScreen(screen)
    sound_controller = game.get_sound_controller()
    

    while state != -1:
        if state == -1:
            break
        elif state == -2:
            (max_towers, towers_left) = game.get_towers_used()
            state = win.open_win(max_towers, towers_left)
        elif state == 0:
            sound_controller.stop_music()
            sound_controller.start_menu_music()
            state = menu.open_menu()
            sound_controller.play_sound("click")
        else:
            game.flush()
            game.erect_hice(levels[state])
            state = game.start_game_loop()

    pygame.quit()
