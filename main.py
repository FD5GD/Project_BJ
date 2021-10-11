import sys
import pygame
import os


import draw
import screen
import key_handling


def main():
    print(sys.path)
    pygame.init()
    screen.init_screen()
    window = pygame.display.set_mode(size=(960, 960))
    pygame.display.set_caption("Project BJ")
    draw.prep_static()
    fps_clock = pygame.time.Clock()
    while True:
        delta = fps_clock.tick(60)
        events = pygame.event.get()
        for event in events:
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key_handling.key_down(event)
            elif event.type == pygame.KEYUP:
                key_handling.key_up(event)

        draw.update(window, delta)


if __name__ == '__main__':
    main()
