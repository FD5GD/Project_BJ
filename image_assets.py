from main import pygame


MENU_BACKGROUND = pygame.transform.scale(pygame.image.load("Assets/images/menu-bg.png"), (960, 960))
LEVEL_ICON = {
    -1: pygame.image.load("Assets/images/level-icon-locked.png"),
    0: pygame.image.load("Assets/images/level-icon-default.png"),
    1: pygame.image.load("Assets/images/level-icon-e.png"),
    2: pygame.image.load("Assets/images/level-icon-d.png"),
    3: pygame.image.load("Assets/images/level-icon-c.png"),
    4: pygame.image.load("Assets/images/level-icon-b.png"),
    5: pygame.image.load("Assets/images/level-icon-a.png"),
    6: pygame.image.load("Assets/images/level-icon-s.png"),
    7: pygame.image.load("Assets/images/level-icon-ss.png")
}
RANK_ICON = {
    0: pygame.image.load("Assets/images/rank-icon-f.png"),
    1: pygame.image.load("Assets/images/rank-icon-e.png"),
    2: pygame.image.load("Assets/images/rank-icon-d.png"),
    3: pygame.image.load("Assets/images/rank-icon-c.png"),
    4: pygame.image.load("Assets/images/rank-icon-b.png"),
    5: pygame.image.load("Assets/images/rank-icon-a.png"),
    6: pygame.image.load("Assets/images/rank-icon-s.png"),
    7: pygame.image.load("Assets/images/rank-icon-ss.png")
}
RANK_ICON_SMALL = {k: pygame.transform.scale(v, (40, 40)) for k, v in RANK_ICON.items()}
MENU_RANK_ICON = dict(RANK_ICON)
MENU_RANK_ICON[0] = pygame.image.load("Assets/images/rank-icon-unlocked.png")
MENU_RANK_ICON[-1] = pygame.image.load("Assets/images/rank-icon-locked.png")
LEVEL_SELECT = pygame.image.load("Assets/images/level-select-outline.png")
LEVEL_PREVIEW = pygame.image.load("Assets/images/menu-level-preview.png")
