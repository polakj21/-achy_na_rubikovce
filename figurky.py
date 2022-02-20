import pygame,sys
from mapy import *
from figurky2 import *
pygame.init()

screen = pygame.display.set_mode((600,500))

black = pygame.sprite.Group()
white = pygame.sprite.Group()
kings = pygame.sprite.Group()


class K(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = K_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = True
        self.mated = False
        self.type = "K"
    def set_movement(self):
        x,y,ind = self.board[0],self.board[1],self.ind
        self.can_move = False
        self.setting(x+1,y+1)
        self.setting(x-1,y+1)
        self.setting(x,y+1)
        self.setting(x+1,y)
        self.setting(x-1,y)
        self.setting(x-1,y-1)
        self.setting(x,y-1)
        self.setting(x+1,y-1)
        if not self.can_move:
            if not moves_white[ind][y][x] == " ":
                self.mated = True
    def setting(self,x,y):
        if x >-1 and y >-1 and x < 8 and y < 8:
            ind = self.ind
            place = positions[ind][y][x]
            place2 = moves_white[ind][y][x]
            if place == " " and place2 == " ":
                self.moves[y][x] = "X"
                self.can_move = True
            elif place.capitalize() == place:
                pass
            elif place == "k":
                self.moves[y][x] = "C"
            elif place2 == " ":
                self.moves[y][x] = "X"
                self.can_move = True
class D(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = D_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "D"
    def set_movement(self):
        x,y,ind = self.board[0],self.board[1],self.ind
        while x != 0:
            x-=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if x != 0:
                    self.moves[ind][y][x-1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
        x = self.board[0]
        while x != 7:
            x+=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if x != 7:
                    self.moves[y][x+1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
        x = self.board[0]
        while y != 7:
            y+=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if y != 7:
                    self.moves[ind][y+1][x] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
        y = self.board[1]
        while y != 0:
            y-=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if y != 0:
                    self.moves[ind][y-1][x] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
        x,y,ind = self.board[0],self.board[1],self.ind
        while x != 0 and y != 0:
            x-=1
            y-=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if x != 0 and y != 0:
                    self.moves[ind][y-1][x-1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
        x,y = self.board[0],self.board[1]
        while x != 7 and y != 7:
            x+=1
            y+=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if x != 7 and y != 7:
                    self.moves[y+1][x+1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
        x,y = self.board[0],self.board[1]
        while y != 7 and x != 0:
            y+=1
            x-=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if y != 7 and x != 0:
                    self.moves[ind][y+1][x-1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
        x,y = self.board[0],self.board[1]
        while y != 0 and x != 7:
            y-=1
            x+=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if y != 0 and x != 7:
                    self.moves[ind][y-1][x+1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
class J(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = J_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "J"
    def set_movement(self):
        x,y = self.board[0],self.board[1]
        self.setting(x-1,y+2)
        self.setting(x-2,y+1)
        self.setting(x+1,y-2)
        self.setting(x+2,y-1)
        self.setting(x+1,y+2)
        self.setting(x+2,y+1)
        self.setting(x-1,y-2)
        self.setting(x-2,y-1)
    def setting(self,x,y):
        if x >-1 and y >-1 and x < 8 and y < 8:
            ind = self.ind
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                pass
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
            else:
                self.moves[y][x] = "X"
        
class V(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = V_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "V"
    def set_movement(self):
        x,y,ind = self.board[0],self.board[1],self.ind
        while x != 0:
            x-=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if x != 0:
                    self.moves[ind][y][x-1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
        x = self.board[0]
        while x != 7:
            x+=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if x != 7:
                    self.moves[y][x+1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
        x = self.board[0]
        while y != 7:
            y+=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if y != 7:
                    self.moves[ind][y+1][x] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
        y = self.board[1]
        while y != 0:
            y-=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if y != 0:
                    self.moves[ind][y-1][x] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break

class S(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = S_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "S"
    def set_movement(self):
         x,y,ind = self.board[0],self.board[1],self.ind
         while x != 0 and y != 0:
            x-=1
            y-=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if x != 0 and y != 0:
                    self.moves[ind][y-1][x-1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
         x,y = self.board[0],self.board[1]
         while x != 7 and y != 7:
            x+=1
            y+=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if x != 7 and y != 7:
                    self.moves[y+1][x+1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
         x,y = self.board[0],self.board[1]
         while y != 7 and x != 0:
            y+=1
            x-=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if y != 7 and x != 0:
                    self.moves[ind][y+1][x-1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
         x,y = self.board[0],self.board[1]
         while y != 0 and x != 7:
            y-=1
            x+=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                break
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
                if y != 0 and x != 7:
                    self.moves[ind][y-1][x+1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break

class P(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = P_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "P__"
        self.yes = False
        self.rotation = 1
    def set_movement(self):
        x,y = self.board[0],self.board[1]
        rotation = self.rotation
        if rotation == 1:
            self.setting(x,y+1)
            self.setting2(x-1,y+1)
            self.setting2(x+1,y+1)
            if self.yes:
                self.setting(x,y+2)
        elif rotation == 2:
            self.setting(x-1,y+1)
            self.setting2(x-1,y)
            self.setting2(x-1,y-1)
            if self.yes:
                self.setting2(x-2,y)
        elif rotation == 3:
            self.setting(x,y-1)
            self.setting2(x-1,y-1)
            self.setting2(x+1,y-1)
            if self.yes:
                self.setting(x,y-2)
        elif rotation == 4:
            self.setting(x+1,y+1)
            self.setting2(x+1,y)
            self.setting2(x+1,y-1)
            if self.yes:
                self.setting(x+2,y)
    def setting(self,x,y):
        if x >-1 and y >-1 and x < 8 and y < 8:
            ind = self.ind
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
                self.yes = True
    def setting2(self,x,y):
        if x >-1 and y >-1 and x < 8 and y < 8:
            ind = self.ind
            place = positions[ind][y][x]
            if place == " ":
                pass
            elif place.capitalize() == place:
                pass
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
            else:
                self.moves[y][x] = "X"
class P__(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = P_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "P__"
        self.moved = False
        self.rotation = 1
    def set_movement(self):
        x,y = self.board[0],self.board[1]
        rotation = self.rotation
        if rotation == 1:
            self.setting(x,y+1)
            self.setting2(x-1,y+1)
            self.setting2(x+1,y+1)
        elif rotation == 2:
            self.setting(x-1,y+1)
            self.setting2(x-1,y)
            self.setting2(x-1,y-1)
        elif rotation == 3:
            self.setting(x,y-1)
            self.setting2(x-1,y-1)
            self.setting2(x+1,y-1)
        elif rotation == 4:
            self.setting(x+1,y+1)
            self.setting2(x+1,y)
            self.setting2(x+1,y-1)
    def setting(self,x,y):
        if x >-1 and y >-1 and x < 8 and y < 8:
            ind = self.ind
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.capitalize() == place:
                pass
    def setting2(self,x,y):
        if x >-1 and y >-1 and x < 8 and y < 8:
            ind = self.ind
            place = positions[ind][y][x]
            if place == " ":
                pass
            elif place.capitalize() == place:
                pass
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
            else:
                self.moves[y][x] = "X"

def set_position():
    global black,white,moves_black,moves_white
    for m in moves_black:
        m = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
    for move in moves_white:
        move = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
    for pos_ind,position in enumerate(positions):
        for line_ind,line in enumerate(position):
            for sym_ind,sym in enumerate(line):
                pos_screen = (sym_ind*32+poss[pos_ind][0],line_ind*32+poss[pos_ind][1])
                pos_board = (sym_ind,line_ind)
                if sym == "V":
                    entity = V(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    black.add(entity)
                elif sym == "J":
                    entity = J(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    black.add(entity)
                elif sym == "S":
                    entity = S(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    black.add(entity)
                elif sym == "D":
                    entity = D(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    black.add(entity)
                elif sym == "K":
                    entity = K(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    kings.add(entity)
                    black.add(entity)
                elif sym == "P":
                    entity = P(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    black.add(entity)
                elif sym == "P__":
                    entity = P__(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    black.add(entity)
                elif sym == "v":
                    entity = v(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    white.add(entity)
                elif sym == "j":
                    entity = j(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    white.add(entity)
                elif sym == "s":
                    entity = s(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    white.add(entity)
                elif sym == "d":
                    entity = d(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    white.add(entity)
                elif sym == "k":
                    entity = k(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    kings.add(entity)
                    white.add(entity)
                elif sym == "p":
                    entity = p(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    white.add(entity)
                elif sym == "p__":
                    entity = p__(pos_screen,pos_ind,pos_board)
                    entity.set_movement()
                    white.add(entity)
    for figure in black:
        moves = moves_black[figure.ind]
        for line_ind,line in enumerate(figure.moves):
            for sym_ind,sym in enumerate(line):
                if sym == "X" or sym == "C":
                    moves[line_ind][sym_ind] = sym
    for figure in white:
        moves = moves_white[figure.ind]
        for line_ind,line in enumerate(figure.moves):
            for sym_ind,sym in enumerate(line):
                if sym == "X" or sym == "C":
                    moves[line_ind][sym_ind] = sym
    king_check()
def king_check():
    global black,white,kings,positions
    x = False
    for figure in kings:
        figure.set_movement()
        if figure.mated:
            kings.remove(figure)
            black.remove(figure)
            white.remove(figure)
            positions[figure.ind][figure.board[1]][figure.board[0]] = " "
            x = True
    if x:
        set_position()
