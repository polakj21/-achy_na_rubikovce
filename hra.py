import pygame,sys
from mapy import *
from figurky import *
pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("¤šachy na rubikovce¤")
pygame.display.set_icon(d_)
screen = pygame.display.set_mode((1258,952))

set_position()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()  
            
    screen.fill((38,33,28))
    set_boards()
    black.draw(screen)
    white.draw(screen)
    pygame.display.update()
    clock.tick(60)