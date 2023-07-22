import pygame
from main_screen import MainMenu
from game import Game
from game_state import GameState
from components.buildings.house import House
from components.buildings.power_house import PowerHouse

state = GameState.MAIN_MENU

if __name__ == "__main__":
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Watt Wizards - The Game")

    game = Game(screen)
    power_hice_lvl1 = [PowerHouse((3,3)),PowerHouse((3,12)), PowerHouse((16,3)), PowerHouse((16,12))]
    #House((0,0)),House((19,0)),House((0,14)),House((19,14)),
    drain_hice_lvl1 = [
        House((6,0)),House((13,0)),
        House((0,5)),House((3,5)),House((6,5)),House((13,5)),House((16,5)),House((19,5)),
        House((0,9)),House((3,9)),House((6,9)),House((13,9)),House((16,9)),House((19,9)),
        House((6,14)),House((13,14)),
        ]

    power_hice_lvl2 = [PowerHouse((1,1)),PowerHouse((11,12)), PowerHouse((15,10))]
    drain_hice_lvl2 = [House((1,12)),House((11,1)),House((5,5)),House((10,2)),House((2,10)),House((4,9)),House((3,3)),House((9,12)),House((14,13)),House((17,7)),House((19,3))]

    menu = MainMenu(screen)
    sound_controller = game.get_sound_controller()
    

    while state != GameState.EXIT:
        if state == GameState.LEVEL_1:
            game.flush()
            game.erect_hice(power_hice_lvl1+drain_hice_lvl1)
            state = game.start_game_loop()
        elif state == GameState.LEVEL_2:
            game.flush()
            game.erect_hice(power_hice_lvl2+drain_hice_lvl2)
            state = game.start_game_loop()
        elif state == GameState.MAIN_MENU or state == GameState.GAME_OVER:
            sound_controller.stop_music()
            sound_controller.start_menu_music()
            state = menu.open_menu()
        else:
            break;

    pygame.quit()
