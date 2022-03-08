import pygame,sys
from šipky import *
#základní věci
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("¤šachy na rubikovce¤")
pygame.display.set_icon(d_)
screen = pygame.display.set_mode((1184,896))

set_position()

choise_tile = pygame.Surface((32,32))
choise_tile.fill("green")
choise_tile.set_alpha(200, pygame.RLEACCEL)
#umístění šipek
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
#kontroluje zda někdo vyhrál
def end_check():
    global selected,colour,rounds,played_at,black,white,kings
    win_check = 0
    for king in kings:
        if king in white:
            win_check += 1
    if win_check < 4:
        game_end(comic_sans.render("!!!BLACK HAVE WON THE GAME!!!",False,("gold")).convert_alpha())
        selected = False
        colour = "white"
        rounds = 3
        played_at = []
        black.empty()
        white.empty()
        kings.empty()
        set_position()
    win_check = 0
    for king in kings:
        if king in black:
            win_check += 1
    if win_check < 4:
        game_end(comic_sans.render("!!!WHITE HAVE WON THE GAME!!!",False,("gold")).convert_alpha())
        selected = False
        colour = "white"
        rounds = 3
        played_at = []
        black.empty()
        white.empty()
        kings.empty()
        set_position()
#zobrazuje kam lze figurku pohnout
def get_options(moves,board_ind):
    for line_ind,line in enumerate(moves):
        for sym_ind,sym in enumerate(line):
            if sym == "X":
                screen.blit(choise_tile,(sym_ind*32+poss[board_ind][0],line_ind*32+poss[board_ind][1]))                
#další hodnoty
txt_colour = (69,60,50)
selected = False
colour = "white"
rounds = 3
played_at = []
#main loop
while True:
    #exit
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    #kolo černého
    if colour == "black": 
        #pohyb figurkou
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
                        rounds -= 1
                        played_at.append(chosen_one.pos)
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
            screen.blit(player_text,(608,64))
            screen.blit(rounds_text,(608,96))
            screen.blit(rolls_text,(608,128))
            pygame.display.flip()
        else:
            #výběr figurky
            from šipky import roll
            mouse_pos = pygame.mouse.get_pos()
            if rounds == 0 and roll:
                colour = "white"
                antiroll()
                rounds = 3
                played_at = []
                for arrow in arrows:
                    arrow.refresh()
            if rounds != 0:
                for figure in black:
                    if figure.rect.collidepoint(mouse_pos) and figure.pos not in played_at and pygame.mouse.get_pressed()[0]:
                        chosen_one = figure
                        pygame.time.wait(100)
                        selected = True
                    
            screen.fill((38,33,28))
            set_boards()
            if not roll:
                arrows.update(mouse_pos,"black")
            arrows.draw(screen)
            black.draw(screen)
            white.draw(screen)
            end_check()
    #kolo bílého
    else:
        #pohyb figurkou
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
                        rounds -= 1
                        played_at.append(chosen_one.pos)
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
            screen.blit(player_text,(608,64))
            screen.blit(rounds_text,(608,96))
            screen.blit(rolls_text,(608,128))
            pygame.display.flip()
        else:
            #výběr figurky
            from šipky import roll
            mouse_pos = pygame.mouse.get_pos()
            if rounds == 0 and roll:
                colour = "black"
                antiroll()
                rounds = 3
                played_at = []
                for arrow in arrows:
                    arrow.refresh()
            if rounds != 0:
                for figure in white:
                    if figure.rect.collidepoint(mouse_pos) and figure.pos not in played_at and pygame.mouse.get_pressed()[0]:
                        chosen_one = figure
                        pygame.time.wait(100)
                        selected = True   
            screen.fill((38,33,28))
            set_boards()
            if not roll:
                arrows.update(mouse_pos,"white")
            arrows.draw(screen)
            black.draw(screen)
            white.draw(screen)
            end_check()
    #text       
    player_text = comic_sans.render("CURENTLY PLAYNG: " + colour.upper(), False, (txt_colour)).convert_alpha()
    rounds_text = comic_sans.render("TURNS LEFT: " + str(rounds), False, (txt_colour)).convert_alpha()
    if roll:
        rolls_text = comic_sans.render("SPINS LEFT: 0", False, (txt_colour)).convert_alpha()
    else:
        rolls_text = comic_sans.render("SPINS LEFT: 1", False, (txt_colour)).convert_alpha()
    screen.blit(player_text,(608,64))
    screen.blit(rounds_text,(608,96))
    screen.blit(rolls_text,(608,128))
    pygame.display.update()
    clock.tick(60)