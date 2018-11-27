import pygame
from pygame.locals import *

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')


# classes for our game objects
class Tab(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Arrow(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


def main():

    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption('Star Search')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    if pygame.font:
        font = pygame.font.Font(None, 54)
        text = font.render("In a galaxy far far away...", 1, (210, 210, 255))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()

    going = True
    while going:
        clock.tick(100)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False

        screen.blit(background, (0, 0))
        pygame.display.flip()

    pygame.quit()


# this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()
