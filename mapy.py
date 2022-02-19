import pygame
pygame.init()

board1 = [" X X X X",
          "X X X X ",
          " X X X X",
          "X X X X ",
          " X X X X",
          "X X X X ",
          " X X X X",
          "X X X X ",]
board2 = board3 = board4 = board5 = board6 = board1
boards = (board1,board2,board3,board4,board5,board6)
position1 = [("V","J","S","D","K","S","J","V"),
             ("P","P","P","P","P","P","P","P"),
             (" "," "," "," "," "," "," "," "),
             (" "," "," "," "," "," "," "," "),
             (" "," "," "," "," "," "," "," "),
             (" "," "," "," "," "," "," "," "),
             ("p","p","p","p","p","p","p","p"),
             ("v","j","s","d","k","s","j","v")]
position2 = position3 = position4 = position5 = position6 = position1
positions = (position1,position2,position3,position4,position5,position6)

moves1 = [" "," "," "," "," "," "," "," ",
         " "," "," "," "," "," "," "," ",
         " "," "," "," "," "," "," "," ",
         " "," "," "," "," "," "," "," ",
         " "," "," "," "," "," "," "," ",
         " "," "," "," "," "," "," "," ",
         " "," "," "," "," "," "," "," ",
         " "," "," "," "," "," "," "," ",]
moves2 = moves3 = moves4 = moves5 = moves6 = moves1

poss = ((34,340),(340,340),(340,34),(340,646),(646,340),(952,340))

screen = pygame.display.set_mode((600,500))
under_tile = pygame.Surface((272,272))
under_tile.fill((156,138,112))
tile = pygame.Surface((34,34))
tile.fill((69,60,50))

def set_boards():
    screen.blit(under_tile,(34,340))
    screen.blit(under_tile,(340,340))
    screen.blit(under_tile,(340,34))
    screen.blit(under_tile,(340,646))
    screen.blit(under_tile,(646,340))
    screen.blit(under_tile,(952,340))
    for board_ind,board in enumerate(boards):
        for line_ind,line in enumerate(board):
            for sym_ind,sym in enumerate(line):
                if sym == "X":
                    screen.blit(tile,(sym_ind*34+poss[board_ind-1][0],line_ind*34+poss[board_ind-1][1]))
        