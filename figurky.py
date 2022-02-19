import pygame,sys
from mapy import *
pygame.init()

screen = pygame.display.set_mode((600,500))

black = pygame.sprite.Group()
white = pygame.sprite.Group()

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

class K(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = K_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
class D(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = D_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
class J(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = J_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class V(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = V_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class S(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = S_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class P(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = P_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class k(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = k_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class d(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = d_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class j(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = j_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


class v(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = v_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class s(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = s_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class p(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = p_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        

def set_position():
    global black,white
    for pos_ind,position in enumerate(positions):
        for line_ind,line in enumerate(position):
            for sym_ind,sym in enumerate(line):
                pos = (sym_ind*34+poss[pos_ind-1][0],line_ind*34+poss[pos_ind-1][1])
                if sym == "V":
                    entity = V(pos)
                    black.add(entity)
                elif sym == "J":
                    entity = J(pos)
                    black.add(entity)
                elif sym == "S":
                    entity = S(pos)
                    black.add(entity)
                elif sym == "D":
                    entity = D(pos)
                    black.add(entity)
                elif sym == "K":
                    entity = K(pos)
                    black.add(entity)
                elif sym == "P":
                    entity = P(pos)
                    black.add(entity)
                elif sym == "v":
                    entity = v(pos)
                    white.add(entity)
                elif sym == "j":
                    entity = j(pos)
                    white.add(entity)
                elif sym == "s":
                    entity = s(pos)
                    white.add(entity)
                elif sym == "d":
                    entity = d(pos)
                    white.add(entity)
                elif sym == "k":
                    entity = k(pos)
                    white.add(entity)
                elif sym == "p":
                    entity = p(pos)
                    white.add(entity)
