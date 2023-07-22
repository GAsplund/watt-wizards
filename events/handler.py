import sys

import pygame


class EventHandler:
    @staticmethod
    def handle_events():
        for event in pygame.event.get():
            EventHandler.__handle_event(event)

    @staticmethod
    def __handle_event(event):
        pass
    