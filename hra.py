import pygame,sys
from mapy import *
from figurky import *
pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("¤šachy na rubikovce¤")
pygame.display.set_icon(d_)
screen = pygame.display.set_mode((1258,952))

under_tile = pygame.Surface((272,272))
under_tile.fill((156,138,112))
tile = pygame.Surface((34,34))
tile.fill((69,60,50))

def boards():
    screen.blit(under_tile,(34,340))
    screen.blit(under_tile,(340,340))
    screen.blit(under_tile,(340,34))
    screen.blit(under_tile,(340,646))
    screen.blit(under_tile,(646,340))
    screen.blit(under_tile,(952,340))
    for line_ind,line in enumerate(board1):
        for sym_ind,sym in enumerate(line):
            if sym == "X":
                screen.blit(tile,(sym_ind*34+34,line_ind*34+340))
    for line_ind,line in enumerate(board2):
        for sym_ind,sym in enumerate(line):
            if sym == "X":
                screen.blit(tile,(sym_ind*34+340,line_ind*34+340))
    for line_ind,line in enumerate(board3):
        for sym_ind,sym in enumerate(line):
            if sym == "X":
                screen.blit(tile,(sym_ind*34+340,line_ind*34+34))
    for line_ind,line in enumerate(board4):
        for sym_ind,sym in enumerate(line):
            if sym == "X":
                screen.blit(tile,(sym_ind*34+340,line_ind*34+646))
    for line_ind,line in enumerate(board5):
        for sym_ind,sym in enumerate(line):
            if sym == "X":
                screen.blit(tile,(sym_ind*34+646,line_ind*34+340))
    for line_ind,line in enumerate(board6):
        for sym_ind,sym in enumerate(line):
            if sym == "X":
                screen.blit(tile,(sym_ind*34+952,line_ind*34+340))
    
            

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
    boards()
    pygame.display.update()
    clock.tick(60)