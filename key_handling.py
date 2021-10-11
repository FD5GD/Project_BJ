import sys

from main import pygame
import screen
import level_loader


def key_down(event):
    current_screen = screen.get_screen()
    if screen.QUIT:
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        else:
            screen.QUIT = False
    elif current_screen == screen.Screen.MAIN_MENU:
        if event.key == pygame.K_RETURN:
            screen.set_screen(screen.Screen.LEVEL_SELECT)
    elif current_screen == screen.Screen.LEVEL_SELECT:
        target_level = None
        if event.key == pygame.K_RIGHT:
            try:
                target_level = level_loader.get_level_by_id(screen.get_current_level())["nav"]["right"]
            except KeyError:
                pass
        elif event.key == pygame.K_LEFT:
            try:
                target_level = level_loader.get_level_by_id(screen.get_current_level())["nav"]["left"]
            except KeyError:
                pass
        elif event.key == pygame.K_UP:
            try:
                target_level = level_loader.get_level_by_id(screen.get_current_level())["nav"]["up"]
            except KeyError:
                pass
        elif event.key == pygame.K_DOWN:
            try:
                target_level = level_loader.get_level_by_id(screen.get_current_level())["nav"]["down"]
            except KeyError:
                pass
        elif event.key == pygame.K_RETURN:
            screen.set_screen(screen.Screen.LEVEL_PREVIEW)
        elif event.key == pygame.K_ESCAPE:
            screen.QUIT = True
        if target_level:
            screen.set_current_level(target_level)
            print(target_level)
    elif current_screen == screen.Screen.LEVEL_PREVIEW:
        if event.key == pygame.K_ESCAPE:
            screen.set_screen(screen.Screen.LEVEL_SELECT)
        elif event.key == pygame.K_RETURN:
            screen.set_screen(screen.Screen.GAMEPLAY) # very WIP


def key_up(event):
    pass
