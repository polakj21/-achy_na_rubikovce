import pygame,sys
from mapy import *
pygame.init()

screen = pygame.display.set_mode((600,500))
#textury
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
#bíle figurky
class k(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board,pos_ind):
        super().__init__()
        self.image = k_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = True
        self.mated = False
        self.pos = pos_ind
        self.type = "k"
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
            if not moves_black[ind][y][x] == " ":
                self.mated = True
    def setting(self,x,y):
        if x >-1 and y >-1 and x < 8 and y < 8:
            ind = self.ind
            place = positions[ind][y][x]
            place2 = moves_black[ind][y][x]
            if place == " " and place2 == " ":
                self.moves[y][x] = "X"
                self.can_move = True
            elif place.lower() == place:
                pass
            elif place == "K":
                self.moves[y][x] = "C"
            elif place2 == " ":
                self.moves[y][x] = "X"
                self.can_move = True
class d(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board,pos_ind):
        super().__init__()
        self.image = d_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.pos = pos_ind
        self.type = "d"
    def set_movement(self):
        self.checking = False
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
    def __init__(self,pos,ind,board,pos_ind):
        super().__init__()
        self.image = j_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.pos = pos_ind
        self.type = "j"
    def set_movement(self):
        self.checking = False
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
            elif place.lower() == place:
                pass
            elif place == "K":
                self.checking = True
                self.moves[y][x] = "C"
            else:
                self.moves[y][x] = "X"
class v(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board,pos_ind):
        super().__init__()
        self.image = v_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.pos = pos_ind
        self.type = "v"
    def set_movement(self):
        self.checking = False
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
    def __init__(self,pos,ind,board,pos_ind):
        super().__init__()
        self.image = s_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.pos = pos_ind
        self.type = "s"
    def set_movement(self):
        self.checking = False
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
    def __init__(self,pos,ind,board,pawn_dir,pos_ind):
        super().__init__()
        self.image = p_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "p__"
        self.moved = False
        self.pos = pos_ind
        self.yes = False
        self.rotation = pawn_dir
    def set_movement(self):
        self.checking = False
        x,y = self.board[0],self.board[1]
        rotation = self.rotation
        if rotation == 3:
            self.setting(x,y+1)
            self.setting2(x-1,y+1)
            self.setting2(x+1,y+1)
            if y == 7:
                transform("w",x,y,self.ind)
            if self.yes:
                self.setting(x,y+2)
        elif rotation == 4:
            self.setting2(x-1,y+1)
            self.setting(x-1,y)
            self.setting2(x-1,y-1)
            if x == 0:
                transform("w",x,y,self.ind)
            if self.yes:
                self.setting(x-2,y)
        elif rotation == 1:
            self.setting(x,y-1)
            self.setting2(x-1,y-1)
            self.setting2(x+1,y-1)
            if y == 0:
                transform("w",x,y,self.ind)
            if self.yes:
                self.setting(x,y-2)
        elif rotation == 2:
            self.setting2(x+1,y+1)
            self.setting(x+1,y)
            self.setting2(x+1,y-1)
            if x == 7:
                transform("w",x,y,self.ind)
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
            elif place.lower() == place:
                pass
            elif place == "k":
                self.checking = True
                self.moves[y][x] = "C"
            else:
                self.moves[y][x] = "X"
class p__(pygame.sprite.Sprite):
    def __init__(self,pos,ind,board,pawn_dir,pos_ind):
        super().__init__()
        self.image = p_
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.ind = ind
        self.board = board
        self.moves = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
        self.checking = False
        self.type = "p__"
        self.moved = False
        self.pos = pos_ind
        self.rotation = pawn_dir
    def set_movement(self):
        self.checking = False
        x,y = self.board[0],self.board[1]
        rotation = self.rotation
        if rotation == 3:
            self.setting(x,y+1)
            self.setting2(x-1,y+1)
            self.setting2(x+1,y+1)
            if y == 7:
                transform("w",x,y,self.ind)
        elif rotation == 4:
            self.setting2(x-1,y+1)
            self.setting(x-1,y)
            self.setting2(x-1,y-1)
            if x == 0:
                transform("w",x,y,self.ind)
        elif rotation == 1:
            self.setting(x,y-1)
            self.setting2(x-1,y-1)
            self.setting2(x+1,y-1)
            if y == 0:
                transform("w",x,y,self.ind)
        elif rotation == 2:
            self.setting2(x+1,y+1)
            self.setting(x+1,y)
            self.setting2(x+1,y-1)
            if x == 7:
                transform("w",x,y,self.ind)
    def setting(self,x,y):
        if x >-1 and y >-1 and x < 8 and y < 8:
            ind = self.ind
            place = positions[ind][y][x]
            if place == " ":
                self.moves[y][x] = "X"
            elif place.lower() == place:
                pass
    def setting2(self,x,y):
        if x >-1 and y >-1 and x < 8 and y < 8:
            ind = self.ind
            place = positions[ind][y][x]
            if place == " ":
                pass
            elif place.lower() == place:
                pass
            elif place == "K":
                self.checking = True
                self.moves[y][x] = "C"
            else:
                self.moves[y][x] = "X"

#proměna pěšců
def transform(color,x,y,ind):
    global positions
    pygame.time.wait(200)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((176,176))
    #kontrola zda černý, či bílý
    if color == "b":
        jezdec = pygame.transform.scale2x(J_)
        jezdec_rect = jezdec.get_rect()
        jn = "J"
        věž = pygame.transform.scale2x(V_)
        věž_rect = věž.get_rect()
        vn = "V"
        dáma = pygame.transform.scale2x(D_)
        dáma_rect = dáma.get_rect()
        dn = "D"
        střelec = pygame.transform.scale2x(S_)
        střelec_rect = střelec.get_rect()
        sn = "S"
    else:
        jezdec = pygame.transform.scale2x(j_)
        jezdec_rect = jezdec.get_rect()
        jn = "j"
        věž = pygame.transform.scale2x(v_)
        věž_rect = věž.get_rect()
        vn = "v"
        dáma = pygame.transform.scale2x(d_)
        dáma_rect = dáma.get_rect()
        dn = "d"
        střelec = pygame.transform.scale2x(s_)
        střelec_rect = střelec.get_rect()
        sn = "s"
        
    věž_rect.topleft = (16,16)
    dáma_rect.topleft = (96,16)
    jezdec_rect.topleft = (16,96)
    střelec_rect.topleft = (96,96)
    b = 0
    #main loop
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
        b +=1
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and b > 40:
            if dáma_rect.collidepoint(mouse_pos):
                positions[ind][y][x] = dn
                break
            elif věž_rect.collidepoint(mouse_pos):
                positions[ind][y][x] = vn
                break
            elif jezdec_rect.collidepoint(mouse_pos):
                positions[ind][y][x] = jn
                break
            elif střelec_rect.collidepoint(mouse_pos):
                positions[ind][y][x] = sn
                break
        screen.fill((69,60,50))
        screen.blit(věž,věž_rect)
        screen.blit(dáma,dáma_rect)
        screen.blit(jezdec,jezdec_rect)
        screen.blit(střelec,střelec_rect)
        pygame.display.update()
        clock.tick(60)
    screen = pygame.display.set_mode((1184,896))
    pygame.time.wait(100)
        