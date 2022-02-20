import pygame,sys
from mapy import *
from figurky import *
from figurky2 import *
pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("¤šachy na rubikovce¤")
pygame.display.set_icon(d_)
screen = pygame.display.set_mode((1184,896))

set_position()

choise_tile = pygame.Surface((32,32))
choise_tile.fill("green")
choise_tile.set_alpha(200, pygame.RLEACCEL)

def get_options(moves,board_ind):
    for line_ind,line in enumerate(moves):
        for sym_ind,sym in enumerate(line):
            if sym == "X":
                screen.blit(choise_tile,(sym_ind*32+poss[board_ind][0],line_ind*32+poss[board_ind][1]))                

selected = False
color = white
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
    if color == black:   
        if selected:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                try:
                    if chosen_one.moves[(mouse_pos[1]-poss[chosen_one.ind][1])//32][(mouse_pos[0]-poss[chosen_one.ind][0])//32] == "X":
                        positions[chosen_one.ind][(mouse_pos[1]-poss[chosen_one.ind][1])//32][(mouse_pos[0]-poss[chosen_one.ind][0])//32] = chosen_one.type
                        positions[chosen_one.ind][chosen_one.board[1]][chosen_one.board[0]] = " "
                        set_position()
                        black.empty()
                        white.empty()
                        kings.empty()
                        set_position()
                        pygame.time.wait(100)
                        selected = False
                        color = white
                        if figure.type == "P" or figure.type == "P__":
                            screen.fill((38,33,28))
                            set_boards()
                            black.draw(screen)
                            white.draw(screen)
                            pygame.display.flip()
                    else:
                        pygame.time.wait(100)
                        selected = False
                except:
                    pygame.time.wait(100)
                    selected = False
            
            screen.fill((38,33,28))
            set_boards()
            get_options(chosen_one.moves,chosen_one.ind)
            black.draw(screen)
            white.draw(screen)
            pygame.display.flip()
        else:
            for figure in black:
                mouse_pos = pygame.mouse.get_pos()
                if figure.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                    chosen_one = figure
                    pygame.time.wait(100)
                    selected = True
                    
            screen.fill((38,33,28))
            set_boards()
            black.draw(screen)
            white.draw(screen)
    else:
        if selected:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                try:
                    if chosen_one.moves[(mouse_pos[1]-poss[chosen_one.ind][1])//32][(mouse_pos[0]-poss[chosen_one.ind][0])//32] == "X":
                        positions[chosen_one.ind][(mouse_pos[1]-poss[chosen_one.ind][1])//32][(mouse_pos[0]-poss[chosen_one.ind][0])//32] = chosen_one.type
                        positions[chosen_one.ind][chosen_one.board[1]][chosen_one.board[0]] = " "
                        set_position()
                        black.empty()
                        white.empty()
                        kings.empty()
                        set_position()
                        pygame.time.wait(100)
                        selected = False
                        color = black
                        if figure.type == "p" or figure.type == "p__":
                            screen.fill((38,33,28))
                            set_boards()
                            black.draw(screen)
                            white.draw(screen)
                            pygame.display.flip()
                    else:
                        pygame.time.wait(100)
                        selected = False
                except:
                    pygame.time.wait(100)
                    selected = False
                
            
            screen.fill((38,33,28))
            set_boards()
            get_options(chosen_one.moves,chosen_one.ind)
            black.draw(screen)
            white.draw(screen)
            pygame.display.flip()
        else:
            for figure in white:
                mouse_pos = pygame.mouse.get_pos()
                if figure.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                    chosen_one = figure
                    pygame.time.wait(100)
                    selected = True
                    
            screen.fill((38,33,28))
            set_boards()
            black.draw(screen)
            white.draw(screen)
    pygame.display.update()
    clock.tick(60)