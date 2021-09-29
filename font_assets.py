from main import pygame
import math


pygame.font.init()
MAIN_REGULAR = pygame.font.Font("Assets/font/LT Reponse.otf", 24)
MAIN_BOLD = pygame.font.Font("Assets/font/LT Reponse Bold.otf", 24)
MAIN_ITALIC = pygame.font.Font("Assets/font/LT Reponse Italic.otf", 24)
MAIN_BOLD_ITALIC = pygame.font.Font("Assets/font/LT Reponse Bold Italic.otf", 24)


MAIN_BOLD_LARGE = pygame.font.Font("Assets/font/LT Reponse Bold.otf", 36)


LEVEL_ICON_COLOR = {
    -1: "#000000",
    0: "#000000",
    1: "#ffffff",
    2: "#ffffff",
    3: "#000000",
    4: "#000000",
    5: "#000000",
    6: "#000000",
    7: "#000000",
}


def flash_text(text, opac):
    surf = MAIN_BOLD.render(text, True, "#ffffff")
    surf.set_alpha(math.floor(256 * opac))
    return surf
