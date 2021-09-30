from main import pygame
from enum import Enum, unique
import level_loader
import draw


@unique
class Screen(Enum):
    MAIN_MENU = 0
    LEVEL_SELECT = 1
    LEVEL_PREVIEW = 2
    GAMEPLAY = 3


current_screen = Screen.MAIN_MENU


current_level = None
current_level_pos = None


def init_screen():
    print(pygame.event.set_blocked([pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN]))


def get_screen():
    return current_screen


def set_screen(screen):
    global current_screen
    current_screen = screen
    if screen == Screen.LEVEL_SELECT:
        level_map = level_loader.load_map()
        draw.prep_level_map(level_map)
    if screen == Screen.LEVEL_PREVIEW:
        draw.prep_level_preview(current_level)


def get_current_level():
    return current_level


def get_current_level_pos():
    return current_level_pos


def set_current_level(level_id):
    global current_level, current_level_pos
    current_level = level_id
    current_level_pos = tuple(level_loader.get_level_by_id(level_id)["position"])


set_current_level("T01")
