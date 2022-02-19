import pygame
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