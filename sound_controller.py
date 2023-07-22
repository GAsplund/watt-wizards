import pygame


class SoundController:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            "place_pole": pygame.mixer.Sound("assets/sfx/whoosh.mp3"),
            "connect":pygame.mixer.Sound("assets/sfx/zap.mp3"),
            "demolition":pygame.mixer.Sound("assets/sfx/demolition.wav"),
            "fail":pygame.mixer.Sound("assets/sfx/fail.mp3"),
        }
   
    def start_music(self):
        pygame.mixer.music.load("assets/music/Big_Mojo.mp3")
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()
    
    def start_menu_music(self):
        pygame.mixer.music.load("assets/music/Space_Jazz.mp3")
        pygame.mixer.music.play(-1)
    
    def add_sound(self, name: str, path: str):
        self.sounds[name] = pygame.mixer.Sound(path)

    def play_sound(self, sound: str):
        self.sounds[sound].play()