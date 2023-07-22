from enum import Enum, auto

class GameState(Enum):
    MAIN_MENU = auto()
    LEVEL_1 = auto()
    LEVEL_2 = auto()
    GAME_OVER = auto()
    EXIT = auto()
