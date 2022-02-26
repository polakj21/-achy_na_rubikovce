import pygame,sys
from šipky import *
pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("¤šachy na rubikovce¤")
pygame.display.set_icon(d_)
screen = pygame.display.set_mode((1184,896))

set_position()

choise_tile = pygame.Surface((32,32))
choise_tile.fill("green")
choise_tile.set_alpha(200, pygame.RLEACCEL)

arrows = pygame.sprite.Group(horizontal_arrow((0,320),((0,0),(1,0),(4,0),(5,0)),2,1),horizontal_arrow((0,352),((0,1),(1,1),(4,1),(5,1)),None,None),
                             horizontal_arrow((0,384),((0,2),(1,2),(4,2),(5,2)),None,None),horizontal_arrow((0,416),((0,3),(1,3),(4,3),(5,3)),None,None),
                             horizontal_arrow((0,448),((0,4),(1,4),(4,4),(5,4)),None,None),horizontal_arrow((0,480),((0,5),(1,5),(4,5),(5,5)),None,None),
                             horizontal_arrow((0,512),((0,6),(1,6),(4,6),(5,6)),None,None),horizontal_arrow((0,544),((0,7),(1,7),(4,7),(5,7)),3,2),
                             
                             vertical_arrow((320,0),((2,0),(1,0),(3,0),(5,7)),0,1),vertical_arrow((352,0),((2,1),(1,1),(3,1),(5,6)),None,None),
                             vertical_arrow((384,0),((2,2),(1,2),(3,2),(5,5)),None,None),vertical_arrow((416,0),((2,3),(1,3),(3,3),(5,4)),None,None),
                             vertical_arrow((448,0),((2,4),(1,4),(3,4),(5,3)),None,None),vertical_arrow((480,0),((2,5),(1,5),(3,5),(5,2)),None,None),
                             vertical_arrow((512,0),((2,6),(1,6),(3,6),(5,1)),None,None),vertical_arrow((544,0),((2,7),(1,7),(3,7),(5,0)),4,2),
                             
                             nevim_arrow((288,32),((2,0),(4,7),(3,7),(0,0)),5,1),nevim_arrow((288,64),((2,1),(4,6),(3,6),(0,1)),None,None),
                             nevim_arrow((288,96),((2,2),(4,5),(3,5),(0,2)),None,None),nevim_arrow((288,128),((2,3),(4,4),(3,4),(0,3)),None,None),
                             nevim_arrow((288,160),((2,4),(4,3),(3,3),(0,4)),None,None),nevim_arrow((288,192),((2,5),(4,2),(3,2),(0,5)),None,None),
                             nevim_arrow((288,224),((2,6),(4,1),(3,1),(0,6)),None,None),nevim_arrow((288,256),((2,7),(4,0),(3,0),(0,7)),1,2)
                             )

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
                        if chosen_one.type == "P" or chosen_one.type == "P__":
                            dirs[chosen_one.ind][(mouse_pos[1]-poss[chosen_one.ind][1])//32][(mouse_pos[0]-poss[chosen_one.ind][0])//32] = chosen_one.rotation
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
                        for arrow in arrows:
                            arrow.refresh()
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
            arrows.update(mouse_pos,"black")
            arrows.draw(screen)
            black.draw(screen)
            white.draw(screen)
    else:
        if selected:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                try:
                    if chosen_one.moves[(mouse_pos[1]-poss[chosen_one.ind][1])//32][(mouse_pos[0]-poss[chosen_one.ind][0])//32] == "X":
                        positions[chosen_one.ind][(mouse_pos[1]-poss[chosen_one.ind][1])//32][(mouse_pos[0]-poss[chosen_one.ind][0])//32] = chosen_one.type
                        if chosen_one.type == "p" or chosen_one.type == "p__":
                            dirs[chosen_one.ind][(mouse_pos[1]-poss[chosen_one.ind][1])//32][(mouse_pos[0]-poss[chosen_one.ind][0])//32] = chosen_one.rotation
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
                        for arrow in arrows:
                            arrow.refresh()
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
            arrows.update(mouse_pos,"white")
            arrows.draw(screen)
            black.draw(screen)
            white.draw(screen)
    pygame.display.update()
    clock.tick(60)