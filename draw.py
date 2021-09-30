from main import pygame
from screen import *
import image_assets
import font_assets
import math


anim_time = {
    "menu_bg": 0,
    "text_flash": 0
}
anim_cycle_time = {
    "menu_bg": 10000,
    "text_flash": 2000
}


level_map_surf = None
level_preview_surf = None


def prep_level_map(level_map):
    bounds = level_loader.get_map_bounds()
    min_x = bounds["left"]
    max_x = bounds["right"]
    min_y = bounds["top"]
    max_y = bounds["bottom"]
    surf = pygame.Surface((80 * (max_x - min_x + 2), 80 * (max_y - min_y + 2))).convert_alpha()
    surf.fill((0, 0, 0, 0))
    for level in level_map["map"]:
        rank = level_loader.get_rank(level["id"])
        pos = tuple(level["position"])
        level_icon = image_assets.LEVEL_ICON[rank]
        pos_x = 80 * (1 + pos[0] - min_x) - level_icon.get_width() / 2
        pos_y = 80 * (1 + pos[1] - min_y) - level_icon.get_height() / 2
        surf.blit(level_icon, (pos_x, pos_y))
        level_symbol_text = level["head"]["symbol"] if rank >= 0 else "?"
        level_symbol = font_assets.MAIN_BOLD_LARGE.render(level_symbol_text, True, font_assets.LEVEL_ICON_COLOR[rank])
        pos_x = 80 * (1 + pos[0] - min_x) - level_symbol.get_width() / 2
        pos_y = 80 * (1.025 + pos[1] - min_y) - level_symbol.get_height() / 2
        surf.blit(level_symbol, (pos_x, pos_y))
    global level_map_surf
    level_map_surf = surf
    return surf


def prep_level_preview(level_id):
    level = level_loader.get_level_by_id(level_id)
    surf = pygame.Surface((960, 960)).convert_alpha()
    surf.fill((0, 0, 0, 0))
    surf.blit(image_assets.LEVEL_PREVIEW, (0, 0))
    level_name_text = level["head"]["name"] if level_loader.get_rank(level["id"]) >= 0 else "???"
    level_name = font_assets.MAIN_BOLD_LARGE.render(level_name_text, True, (255, 255, 255))
    surf.blit(level_name, (200, 300 - level_name.get_height() / 2))
    global level_preview_surf
    level_preview_surf = surf
    return surf


def update_anim(key, delta):
    anim_time[key] = (anim_time[key] + delta / anim_cycle_time[key]) % 1


def update(window, delta):
    global anim_time
    window.fill("#000000")
    screen = get_screen()
    if screen == Screen.MAIN_MENU:
        window.blit(image_assets.MENU_BACKGROUND, (0, -960 * anim_time["menu_bg"]))
        window.blit(image_assets.MENU_BACKGROUND, (0, 960 - 960 * anim_time["menu_bg"]))
        menu_flash = font_assets.flash_text("Press Enter to continue", (2 + math.sin(anim_time["text_flash"] * 2 * math.pi)) / 4)
        window.blit(menu_flash, (24, 936 - menu_flash.get_height()))
        update_anim("menu_bg", delta)
        update_anim("text_flash", delta)
    elif screen == Screen.LEVEL_SELECT or screen == Screen.LEVEL_PREVIEW:
        window.blit(image_assets.MENU_BACKGROUND, (0, -960 * anim_time["menu_bg"]))
        window.blit(image_assets.MENU_BACKGROUND, (0, 960 - 960 * anim_time["menu_bg"]))
        update_anim("menu_bg", delta)
        if level_map_surf:
            window.blit(level_map_surf, (0, 0))
            select_icon = image_assets.LEVEL_SELECT
            select_pos = get_current_level_pos()
            bounds = level_loader.get_map_bounds()
            pos_x = 80 * (1 + select_pos[0] - bounds["left"]) - select_icon.get_width() / 2
            pos_y = 80 * (1 + select_pos[1] - bounds["top"]) - select_icon.get_height() / 2
            window.blit(select_icon, (pos_x, pos_y))
        if screen == Screen.LEVEL_PREVIEW and level_preview_surf:
            window.blit(level_preview_surf, (0, 0))
    pygame.display.update()
