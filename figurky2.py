import pygame,sys
from mapy import *
pygame.init()

screen = pygame.display.set_mode((600,500))
K_ = pygame.image.load("šachy_textury/black/král.png").convert_alpha()
D_ = pygame.image.load("šachy_textury/black/dáma.png").convert_alpha()
J_ = pygame.image.load("šachy_textury/black/jezdec.png").convert_alpha()
V_ = pygame.image.load("šachy_textury/black/věž.png").convert_alpha()
S_ = pygame.image.load("šachy_textury/black/střelec.png").convert_alpha()
P_ = pygame.image.load("šachy_textury/black/pěšec.png").convert_alpha()
k_ = pygame.image.load("šachy_textury/white/král.png").convert_alpha()
d_ = pygame.image.load("šachy_textury/white/dáma.png").convert_alpha()
j_ = pygame.image.load("šachy_textury/white/jezdec.png").convert_alpha()
v_ = pygame.image.load("šachy_textury/white/věž.png").convert_alpha()
s_ = pygame.image.load("šachy_textury/white/střelec.png").convert_alpha()
p_ = pygame.image.load("šachy_textury/white/pěšec.png").convert_alpha()

class k(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = k_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "k"
    def set_movement(self):
        pass
class d(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = d_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "d"
    def set_movement(self):
        x,y,ind = self.board[0],self.board[1],self.ind
        while x != 0:
            x-=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
                self.checking = True
                self.moves[y][x] = "C"
                if y != 0 and x != 7:
                    self.moves[ind][y-1][x+1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
class j(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = j_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "j"
    def set_movement(self):
        x,y = self.board[0],self.board[1]
        x-=1
        y+=2
        self.setting(x,y)
        x,y = self.board[0],self.board[1]
        x-=2
        y+=1
        self.setting(x,y)
        x,y = self.board[0],self.board[1]
        x+=1
        y-=2
        self.setting(x,y)
        x,y = self.board[0],self.board[1]
        x+=2
        y-=1
        self.setting(x,y)
        x,y = self.board[0],self.board[1]
        x+=1
        y+=2
        self.setting(x,y)
        x,y = self.board[0],self.board[1]
        x+=2
        y+=1
        self.setting(x,y)
        x,y = self.board[0],self.board[1]
        x-=1
        y-=2
        self.setting(x,y)
        x,y = self.board[0],self.board[1]
        x-=2
        y-=1
        self.setting(x,y)
    def setting(self,x,y):
        if x >-1 and y >-1 and x < 8 and y < 8:
            ind = self.ind
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.lower() == place:
                pass
            elif place == "K":
                self.checking = True
                self.moves[y][x] = "C"
            else:
                self.moves[y][x] = "X"
class v(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = v_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "v"
    def set_movement(self):
        x,y,ind = self.board[0],self.board[1],self.ind
        while x != 0:
            x-=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
                self.checking = True
                self.moves[y][x] = "C"
                if y != 0:
                    self.moves[ind][y-1][x] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
class s(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = s_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "s"
    def set_movement(self):
        x,y,ind = self.board[0],self.board[1],self.ind
        while x != 0 and y != 0:
            x-=1
            y-=1
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
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
            elif place.lower() == place:
                break
            elif place == "K":
                self.checking = True
                self.moves[y][x] = "C"
                if y != 0 and x != 7:
                    self.moves[ind][y-1][x+1] = "C"
                break
            else:
                self.moves[y][x] = "X"
                break
class p(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board):
        super().__init__()
        self.image = p_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "p"
    def set_movement(self):
        pass     