from main import pygame
from screen import *
import level_loader


def key_down(event):
    current_screen = get_screen()
    if current_screen == Screen.MAIN_MENU:
        if event.key == pygame.K_RETURN:
            set_screen(Screen.LEVEL_SELECT)
    elif current_screen == Screen.LEVEL_SELECT:
        target_level = None
        if event.key == pygame.K_RIGHT:
            try:
                target_level = level_loader.get_level_by_id(get_current_level())["nav"]["right"]
            except KeyError:
                pass
        elif event.key == pygame.K_LEFT:
            try:
                target_level = level_loader.get_level_by_id(get_current_level())["nav"]["left"]
            except KeyError:
                pass
        elif event.key == pygame.K_UP:
            try:
                target_level = level_loader.get_level_by_id(get_current_level())["nav"]["up"]
            except KeyError:
                pass
        elif event.key == pygame.K_DOWN:
            try:
                target_level = level_loader.get_level_by_id(get_current_level())["nav"]["down"]
            except KeyError:
                pass
        if target_level:
            set_current_level(target_level)
            print(target_level)


def key_up(event):
    pass
