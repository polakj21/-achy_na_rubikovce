import pygame,sys
from mapy import *
from figurky import *
from figurky2 import *
pygame.init()

screen = pygame.display.set_mode((600,500))

horizontal = {"base" : pygame.image.load("šachy_textury/šipky/0.png").convert_alpha(),
              "right" : pygame.image.load("šachy_textury/šipky/1.png").convert_alpha(),
              "left" : pygame.image.load("šachy_textury/šipky/2.png").convert_alpha(),
              "deactive" : pygame.image.load("šachy_textury/šipky/3.png").convert_alpha()}
vertical = {"base" : pygame.transform.rotate(horizontal["base"],90),
            "down" : pygame.transform.rotate(horizontal["right"],90),
            "up" : pygame.transform.rotate(horizontal["left"],90),
            "deactive" : pygame.transform.rotate(horizontal["deactive"],90),}
selected_tile = pygame.Surface((32,32))
selected_tile.fill("orange")
selected_tile.set_alpha(200, pygame.RLEACCEL)
selected_board = pygame.Surface((256,256))
selected_board.fill("orange")
selected_board.set_alpha(200, pygame.RLEACCEL)

def fill(lines,top,directions):
    if top != None:
        screen.blit(selected_board,poss[top])
    for line_ind,line in enumerate(lines):
        if directions[line_ind] == "horizontal":
            for symbol_ind,symbol in enumerate(positions[line[0]][line[1]]):
                screen.blit(selected_tile,(symbol_ind*32+poss[line[0]][0],line[1]*32+poss[line[0]][1]))
        else:
            for row_ind,row in enumerate(positions[line[0]]):
                for symbol_ind,symbol in enumerate(row):
                    if symbol_ind == line[1]:
                        screen.blit(selected_tile,(symbol_ind*32+poss[line[0]][0],row_ind*32+poss[line[0]][1]))

def rotate(top,direction,top_dir):
    global positions,boards
    a = ["","","","","","","",""]
    b = ["","","","","","","",""]
    c = ["","","","","","","",""]
    d = ["","","","","","","",""]
    e = ["","","","","","","",""]
    f = ["","","","","","","",""]
    g = ["","","","","","","",""]
    h = ["","","","","","","",""]
    A = ["","","","","","","",""]
    B = ["","","","","","","",""]
    C = ["","","","","","","",""]
    D = ["","","","","","","",""]
    E = ["","","","","","","",""]
    F = ["","","","","","","",""]
    G = ["","","","","","","",""]
    H = ["","","","","","","",""]
    for sym_ind,sym in enumerate(boards[top][0]):
        A[sym_ind] = sym
    for sym_ind,sym in enumerate(boards[top][1]):
        B[sym_ind] = sym
    for sym_ind,sym in enumerate(boards[top][2]):
        C[sym_ind] = sym
    for sym_ind,sym in enumerate(boards[top][3]):
        D[sym_ind] = sym
    for sym_ind,sym in enumerate(boards[top][4]):
        E[sym_ind] = sym
    for sym_ind,sym in enumerate(boards[top][5]):
        F[sym_ind] = sym
    for sym_ind,sym in enumerate(boards[top][6]):
        G[sym_ind] = sym
    for sym_ind,sym in enumerate(boards[top][7]):
        H[sym_ind] = sym
    for sym_ind,sym in enumerate(positions[top][0]):
        a[sym_ind] = sym
    for sym_ind,sym in enumerate(positions[top][1]):
        b[sym_ind] = sym
    for sym_ind,sym in enumerate(positions[top][2]):
        c[sym_ind] = sym
    for sym_ind,sym in enumerate(positions[top][3]):
        d[sym_ind] = sym
    for sym_ind,sym in enumerate(positions[top][4]):
        e[sym_ind] = sym
    for sym_ind,sym in enumerate(positions[top][5]):
        f[sym_ind] = sym
    for sym_ind,sym in enumerate(positions[top][6]):
        g[sym_ind] = sym
    for sym_ind,sym in enumerate(positions[top][7]):
        h[sym_ind] = sym
    lines = (a,b,c,d,e,f,g,h)
    board = (A,B,C,D,E,F,G,H)
    if direction == "right" or direction == "down":
        if top_dir == 1:
            for line_ind,line in enumerate(lines):
                for sym_ind,sym in enumerate(line):
                    positions[top][-sym_ind-1][line_ind] = sym
            for line_ind,line in enumerate(board):
                for sym_ind,sym in enumerate(line):
                    boards[top][-sym_ind-1][line_ind] = sym
        else:
            for line_ind,line in enumerate(lines):
                for sym_ind,sym in enumerate(line):
                    positions[top][sym_ind][-line_ind-1] = sym
            for line_ind,line in enumerate(board):
                for sym_ind,sym in enumerate(line):
                    boards[top][sym_ind][-line_ind-1] = sym
    else:
        if top_dir == 1:
            for line_ind,line in enumerate(lines):
                for sym_ind,sym in enumerate(line):
                    positions[top][sym_ind][-line_ind-1] = sym
            for line_ind,line in enumerate(board):
                for sym_ind,sym in enumerate(line):
                    boards[top][sym_ind][-line_ind-1] = sym
        else:
            for line_ind,line in enumerate(lines):
                for sym_ind,sym in enumerate(line):
                    positions[top][-sym_ind-1][line_ind] = sym
            for line_ind,line in enumerate(board):
                for sym_ind,sym in enumerate(line):
                    boards[top][-sym_ind-1][line_ind] = sym
        
    black.empty()
    white.empty()
    kings.empty()
    set_position()
        

class horizontal_arrow(pygame.sprite.Sprite):
    def __init__(self,pos,lines,top,top_dir):
        super().__init__()
        self.image = horizontal["base"]
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.topleft = pos
        self.lines = lines
        self.top = top
        self.top_dir = top_dir
        self.can_be_used = True
        self.refresh_countdown = 0
    def update(self,mouse_pos,colour):
        if self.can_be_used:
            if self.rect.collidepoint(mouse_pos):
                fill(self.lines,self.top,("horizontal","horizontal","horizontal","horizontal"))
                if mouse_pos[0] < self.pos[0]+16:
                    self.image = horizontal["left"]
                    if pygame.mouse.get_pressed()[0]:
                        self.move(colour,"left")
                else:
                    self.image = horizontal["right"]
                    if pygame.mouse.get_pressed()[0]:
                        self.move(colour,"right")
            else:
                self.image = horizontal["base"]
    def move(self,colour,direction):
        global positions,black,white,kings,boards
        figures = 0
        check_kings = 0
        a = ["","","","","","","",""]
        b = ["","","","","","","",""]
        c = ["","","","","","","",""]
        d = ["","","","","","","",""]
        A = ["","","","","","","",""]
        B = ["","","","","","","",""]
        C = ["","","","","","","",""]
        D = ["","","","","","","",""]
        for sym_ind,sym in enumerate(positions[self.lines[0][0]][self.lines[0][1]]):
            a[sym_ind] = sym
        for sym_ind,sym in enumerate(positions[self.lines[1][0]][self.lines[1][1]]):
            b[sym_ind] = sym
        for sym_ind,sym in enumerate(positions[self.lines[2][0]][self.lines[2][1]]):
            c[sym_ind] = sym
        for sym_ind,sym in enumerate(positions[self.lines[3][0]][self.lines[3][1]]):
            d[sym_ind] = sym
        for sym_ind,sym in enumerate(boards[self.lines[0][0]][self.lines[0][1]]):
            A[sym_ind] = sym
        for sym_ind,sym in enumerate(boards[self.lines[1][0]][self.lines[1][1]]):
            B[sym_ind] = sym
        for sym_ind,sym in enumerate(boards[self.lines[2][0]][self.lines[2][1]]):
            C[sym_ind] = sym
        for sym_ind,sym in enumerate(boards[self.lines[3][0]][self.lines[3][1]]):
            D[sym_ind] = sym
        lines = (a,b,c,d)
        for letter in lines:
            if "k" in letter:
                return
            elif "K" in letter:
                return
        rects = [pygame.Rect(poss[self.lines[0][0]][0],poss[self.lines[0][0]][1]+3+(self.lines[0][1]*32),256,1),
                 pygame.Rect(poss[self.lines[1][0]][0],poss[self.lines[1][0]][1]+3+(self.lines[1][1]*32),256,1),
                 pygame.Rect(poss[self.lines[2][0]][0],poss[self.lines[2][0]][1]+3+(self.lines[2][1]*32),256,1),
                 pygame.Rect(poss[self.lines[3][0]][0],poss[self.lines[3][0]][1]+3+(self.lines[3][1]*32),256,1)]
        
        if colour == "black":
            for king in kings:
                if king in black:
                    check_kings+=1
            for figure in white:
                if not figure.checking:
                    figures+=1
                else:
                    for rectangle in rects:
                        if figure.rect.colliderect(rectangle):
                            return
        else:
            for king in kings:
                if king in white:
                    check_kings +=1
            for figure in black:
                if not figure.checking and figure not in kings:
                    figures+=1
                else:
                    for rectangle in rects:
                        if figure.rect.colliderect(rectangle):
                            return
        if direction == "left":
            positions[self.lines[0][0]][self.lines[0][1]] = b
            positions[self.lines[1][0]][self.lines[1][1]] = c
            positions[self.lines[2][0]][self.lines[2][1]] = d
            positions[self.lines[3][0]][self.lines[3][1]] = a
        else:
            positions[self.lines[0][0]][self.lines[0][1]] = d
            positions[self.lines[1][0]][self.lines[1][1]] = a
            positions[self.lines[2][0]][self.lines[2][1]] = b
            positions[self.lines[3][0]][self.lines[3][1]] = c
        
        black.empty()
        white.empty()
        kings.empty()
        set_position()
        
        check_kings_2 = 0
        figures_2 = 0
        
        if colour == "black":
            for king in kings:
                if king in black:
                    check_kings_2 +=1
            for figure in white:
                if not figure.checking and figure not in kings:
                    figures_2+=1
        else:
            for king in kings:
                if king in white:
                    check_kings_2 +=1
            for figure in black:
                if not figure.checking and figure not in kings:
                    figures_2+=1
                    
        if figures < figures_2 or check_kings_2 != check_kings:
            positions[self.lines[0][0]][self.lines[0][1]] = a
            positions[self.lines[1][0]][self.lines[1][1]] = b
            positions[self.lines[2][0]][self.lines[2][1]] = c
            positions[self.lines[3][0]][self.lines[3][1]] = d
            black.empty()
            white.empty()
            kings.empty()
            set_position()
            return
        
        self.image = horizontal["deactive"]
        self.can_be_used = False
        self.refresh_countdown =1
        
        if direction == "right":
            boards[self.lines[0][0]][self.lines[0][1]] = D
            boards[self.lines[1][0]][self.lines[1][1]] = A
            boards[self.lines[2][0]][self.lines[2][1]] = B
            boards[self.lines[3][0]][self.lines[3][1]] = C
        else:
            boards[self.lines[0][0]][self.lines[0][1]] = B
            boards[self.lines[1][0]][self.lines[1][1]] = C
            boards[self.lines[2][0]][self.lines[2][1]] = D
            boards[self.lines[3][0]][self.lines[3][1]] = A
        if self.top != None:
            rotate(self.top,direction,self.top_dir)
        
    def refresh(self):
        if self.refresh_countdown == 0:
            self.image = horizontal["base"]
            self.can_be_used = True
        else:
            self.refresh_countdown -=1
            
            
class vertical_arrow(pygame.sprite.Sprite):
    def __init__(self,pos,lines,top,top_dir):
        super().__init__()
        self.image = vertical["base"]
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.topleft = pos
        self.lines = lines
        self.top = top
        self.top_dir = top_dir
        self.can_be_used = True
        self.refresh_countdown = 0
    def update(self,mouse_pos,colour):
        if self.can_be_used:
            if self.rect.collidepoint(mouse_pos):
                fill(self.lines,self.top,("vertical","vertical","vertical","vertical"))
                if mouse_pos[1] < self.pos[1]+16:
                    self.image = vertical["down"]
                    if pygame.mouse.get_pressed()[0]:
                        self.move(colour,"down")
                else:
                    self.image = vertical["up"]
                    if pygame.mouse.get_pressed()[0]:
                        self.move(colour,"up")
            else:
                self.image = vertical["base"]
    def move(self,colour,direction):
        global positions,black,white,kings,boards
        figures = 0
        check_kings = 0
        a = ["","","","","","","",""]
        b = ["","","","","","","",""]
        c = ["","","","","","","",""]
        d = ["","","","","","","",""]
        A = ["","","","","","","",""]
        B = ["","","","","","","",""]
        C = ["","","","","","","",""]
        D = ["","","","","","","",""]
        for line_ind,line in enumerate(positions[self.lines[0][0]]):
            for sym_ind,sym in enumerate(line):
                if sym_ind == self.lines[0][1]:
                    a[line_ind] = sym
        for line_ind,line in enumerate(positions[self.lines[1][0]]):
            for sym_ind,sym in enumerate(line):
                if sym_ind == self.lines[1][1]:
                    b[line_ind] = sym
        for line_ind,line in enumerate(positions[self.lines[2][0]]):
            for sym_ind,sym in enumerate(line):
                if sym_ind == self.lines[2][1]:
                    c[line_ind] = sym
        for line_ind,line in enumerate(positions[self.lines[3][0]]):
            for sym_ind,sym in enumerate(line):
                if sym_ind == self.lines[3][1]:
                    d[line_ind] = sym
        for line_ind,line in enumerate(boards[self.lines[0][0]]):
            for sym_ind,sym in enumerate(line):
                if sym_ind == self.lines[0][1]:
                    A[line_ind] = sym
        for line_ind,line in enumerate(boards[self.lines[1][0]]):
            for sym_ind,sym in enumerate(line):
                if sym_ind == self.lines[1][1]:
                    B[line_ind] = sym
        for line_ind,line in enumerate(boards[self.lines[2][0]]):
            for sym_ind,sym in enumerate(line):
                if sym_ind == self.lines[2][1]:
                    C[line_ind] = sym
        for line_ind,line in enumerate(boards[self.lines[3][0]]):
            for sym_ind,sym in enumerate(line):
                if sym_ind == self.lines[3][1]:
                    D[line_ind] = sym
        lines = (a,b,c,d)
        for letter in lines:
            if "k" in letter:
                return
            elif "K" in letter:
                return
        rects = [pygame.Rect(poss[self.lines[0][0]][0]+3+(self.lines[0][1]*32),poss[self.lines[0][0]][1],1,256),
                 pygame.Rect(poss[self.lines[1][0]][0]+3+(self.lines[1][1]*32),poss[self.lines[1][0]][1],1,256),
                 pygame.Rect(poss[self.lines[2][0]][0]+3+(self.lines[2][1]*32),poss[self.lines[2][0]][1],1,256),
                 pygame.Rect(poss[self.lines[3][0]][0]+3+(self.lines[3][1]*32),poss[self.lines[3][0]][1],1,256)]
        
        if colour == "black":
            for king in kings:
                if king in black:
                    check_kings+=1
            for figure in white:
                if not figure.checking:
                    figures+=1
                else:
                    for rectangle in rects:
                        if figure.rect.colliderect(rectangle):
                            return
        else:
            for king in kings:
                if king in white:
                    check_kings +=1
            for figure in black:
                if not figure.checking and figure not in kings:
                    figures+=1
                else:
                    for rectangle in rects:
                        if figure.rect.colliderect(rectangle):
                            return
        if direction == "down":
            for line_ind,line in enumerate(positions[self.lines[0][0]]):
                line[self.lines[0][1]] = b[line_ind]
            for line_ind,line in enumerate(positions[self.lines[1][0]]):
                line[self.lines[1][1]] = c[line_ind]
            for line_ind,line in enumerate(positions[self.lines[2][0]]):
                line[self.lines[2][1]] = d[-line_ind-1]
            for line_ind,line in enumerate(positions[self.lines[3][0]]):
                line[self.lines[3][1]] = a[-line_ind-1]
        else:
            for line_ind,line in enumerate(positions[self.lines[0][0]]):
                line[self.lines[0][1]] = d[-line_ind-1]
            for line_ind,line in enumerate(positions[self.lines[1][0]]):
                line[self.lines[1][1]] = a[line_ind]
            for line_ind,line in enumerate(positions[self.lines[2][0]]):
                line[self.lines[2][1]] = b[line_ind]
            for line_ind,line in enumerate(positions[self.lines[3][0]]):
                line[self.lines[3][1]] = c[-line_ind-1]
        
        black.empty()
        white.empty()
        kings.empty()
        set_position()
        
        check_kings_2 = 0
        figures_2 = 0
        
        if colour == "black":
            for king in kings:
                if king in black:
                    check_kings_2 +=1
            for figure in white:
                if not figure.checking and figure not in kings:
                    figures_2+=1
        else:
            for king in kings:
                if king in white:
                    check_kings_2 +=1
            for figure in black:
                if not figure.checking and figure not in kings:
                    figures_2+=1
                    
        if figures < figures_2 or check_kings_2 != check_kings:
            for line_ind,line in enumerate(positions[self.lines[0][0]]):
                line[self.lines[0][1]] = a[line_ind]
            for line_ind,line in enumerate(positions[self.lines[1][0]]):
                line[self.lines[1][1]] = b[line_ind]
            for line_ind,line in enumerate(positions[self.lines[2][0]]):
                line[self.lines[2][1]] = c[line_ind]
            for line_ind,line in enumerate(positions[self.lines[3][0]]):
                line[self.lines[3][1]] = d[line_ind]
            black.empty()
            white.empty()
            kings.empty()
            set_position()
            return
        
        self.image = vertical["deactive"]
        self.can_be_used = False
        self.refresh_countdown =1
        
        if direction == "up":
            for line_ind,line in enumerate(boards[self.lines[0][0]]):
                line[self.lines[0][1]] = D[-line_ind-1]
            for line_ind,line in enumerate(boards[self.lines[1][0]]):
                line[self.lines[1][1]] = A[line_ind]
            for line_ind,line in enumerate(boards[self.lines[2][0]]):
                line[self.lines[2][1]] = B[line_ind]
            for line_ind,line in enumerate(boards[self.lines[3][0]]):
                line[self.lines[3][1]] = C[-line_ind-1]
        else:
            for line_ind,line in enumerate(boards[self.lines[0][0]]):
                line[self.lines[0][1]] = B[line_ind]
            for line_ind,line in enumerate(boards[self.lines[1][0]]):
                line[self.lines[1][1]] = C[line_ind]
            for line_ind,line in enumerate(boards[self.lines[2][0]]):
                line[self.lines[2][1]] = D[-line_ind-1]
            for line_ind,line in enumerate(boards[self.lines[3][0]]):
                line[self.lines[3][1]] = A[-line_ind-1]
        if self.top != None:
            rotate(self.top,direction,self.top_dir)
        
    def refresh(self):
        if self.refresh_countdown == 0:
            self.image = vertical["base"]
            self.can_be_used = True
        else:
            self.refresh_countdown -=1

class nevim_arrow(pygame.sprite.Sprite):
    def __init__(self,pos,lines,top,top_dir):
        super().__init__()
        self.image = horizontal["base"]
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.topleft = pos
        self.lines = lines
        self.top = top
        self.top_dir = top_dir
        self.can_be_used = True
        self.refresh_countdown = 0
    def update(self,mouse_pos,colour):
        if self.can_be_used:
            if self.rect.collidepoint(mouse_pos):
                fill(self.lines,self.top,("horizontal","vertical","horizontal","vertical"))
                if mouse_pos[0] < self.pos[0]+16:
                    self.image = horizontal["left"]
                    if pygame.mouse.get_pressed()[0]:
                        self.move(colour,"left")
                else:
                    self.image = horizontal["right"]
                    if pygame.mouse.get_pressed()[0]:
                        self.move(colour,"right")
            else:
                self.image = horizontal["base"]
    def move(self,colour,direction):
        global positions,black,white,kings,boards
        figures = 0
        check_kings = 0
        a = ["","","","","","","",""]
        b = ["","","","","","","",""]
        c = ["","","","","","","",""]
        d = ["","","","","","","",""]
        A = ["","","","","","","",""]
        B = ["","","","","","","",""]
        C = ["","","","","","","",""]
        D = ["","","","","","","",""]
        for sym_ind,sym in enumerate(positions[self.lines[0][0]][self.lines[0][1]]):
            a[sym_ind] = sym
        for line_ind,line in enumerate(positions[self.lines[1][0]]):
            for sym_ind,sym in enumerate(line):
                if sym_ind == self.lines[1][1]:
                    b[line_ind] = sym
        for sym_ind,sym in enumerate(positions[self.lines[2][0]][self.lines[2][1]]):
            c[sym_ind] = sym
        for line_ind,line in enumerate(positions[self.lines[3][0]]):
            for sym_ind,sym in enumerate(line):
                if sym_ind == self.lines[3][1]:
                    d[line_ind] = sym
        for sym_ind,sym in enumerate(boards[self.lines[0][0]][self.lines[0][1]]):
            A[sym_ind] = sym
        for line_ind,line in enumerate(boards[self.lines[1][0]]):
            for sym_ind,sym in enumerate(line):
                if sym_ind == self.lines[1][1]:
                    B[line_ind] = sym
        for sym_ind,sym in enumerate(boards[self.lines[2][0]][self.lines[2][1]]):
            C[sym_ind] = sym
        for line_ind,line in enumerate(boards[self.lines[3][0]]):
            for sym_ind,sym in enumerate(line):
                if sym_ind == self.lines[3][1]:
                    D[line_ind] = sym
        lines = (a,b,c,d)
        for letter in lines:
            if "k" in letter:
                return
            elif "K" in letter:
                return
        rects = [pygame.Rect(poss[self.lines[0][0]][0],poss[self.lines[0][0]][1]+3+(self.lines[0][1]*32),256,1),
                 pygame.Rect(poss[self.lines[1][0]][0]+3+(self.lines[1][1]*32),poss[self.lines[1][0]][1],1,256),
                 pygame.Rect(poss[self.lines[2][0]][0],poss[self.lines[2][0]][1]+3+(self.lines[2][1]*32),256,1),
                 pygame.Rect(poss[self.lines[3][0]][0]+3+(self.lines[3][1]*32),poss[self.lines[3][0]][1],1,256)]
        
        if colour == "black":
            for king in kings:
                if king in black:
                    check_kings+=1
            for figure in white:
                if not figure.checking:
                    figures+=1
                else:
                    for rectangle in rects:
                        if figure.rect.colliderect(rectangle):
                            return
        else:
            for king in kings:
                if king in white:
                    check_kings +=1
            for figure in black:
                if not figure.checking and figure not in kings:
                    figures+=1
                else:
                    for rectangle in rects:
                        if figure.rect.colliderect(rectangle):
                            return
        if direction == "left":
            positions[self.lines[0][0]][self.lines[0][1]] = b
            for line_ind,line in enumerate(positions[self.lines[1][0]]):
                line[self.lines[1][1]] = c[-line_ind-1]
            for sym_ind,sym in enumerate(positions[self.lines[2][0]][self.lines[2][1]]):
                positions[self.lines[2][0]][self.lines[2][1]][sym_ind] = d[-1-sym_ind]
            for line_ind,line in enumerate(positions[self.lines[3][0]]):
                line[self.lines[3][1]] = a[-line_ind-1]
        else:
            for sym_ind,sym in enumerate(positions[self.lines[0][0]][self.lines[0][1]]):
                positions[self.lines[0][0]][self.lines[0][1]][sym_ind] = d[-sym_ind-1]
                print(positions[self.lines[0][0]][self.lines[0][1]])
            for line_ind,line in enumerate(positions[self.lines[1][0]]):
                line[self.lines[1][1]] = a[line_ind]
            for sym_ind,sym in enumerate(positions[self.lines[2][0]][self.lines[2][1]]):
                positions[self.lines[2][0]][self.lines[2][1]][sym_ind] = b[-1-sym_ind]
            for line_ind,line in enumerate(positions[self.lines[3][0]]):
                line[self.lines[3][1]] = c[line_ind]
        
        black.empty()
        white.empty()
        kings.empty()
        set_position()
        
        check_kings_2 = 0
        figures_2 = 0
        
        if colour == "black":
            for king in kings:
                if king in black:
                    check_kings_2 +=1
            for figure in white:
                if not figure.checking and figure not in kings:
                    figures_2+=1
        else:
            for king in kings:
                if king in white:
                    check_kings_2 +=1
            for figure in black:
                if not figure.checking and figure not in kings:
                    figures_2+=1
                    
        if figures < figures_2 or check_kings_2 != check_kings:
            positions[self.lines[0][0]][self.lines[0][1]] = a
            for line_ind,line in enumerate(positions[self.lines[1][0]]):
                line[self.lines[1][1]] = b[line_ind]
            positions[self.lines[2][0]][self.lines[2][1]] = c
            for line_ind,line in enumerate(positions[self.lines[3][0]]):
                line[self.lines[3][1]] = d[line_ind]
            black.empty()
            white.empty()
            kings.empty()
            set_position()
            return
        
        self.image = horizontal["deactive"]
        self.can_be_used = False
        self.refresh_countdown =1
        
        if direction == "right":
            for sym_ind,sym in enumerate(boards[self.lines[0][0]][self.lines[0][1]]):
                boards[self.lines[0][0]][self.lines[0][1]][sym_ind] = D[-sym_ind-1]
            for line_ind,line in enumerate(boards[self.lines[1][0]]):
                line[self.lines[1][1]] = A[line_ind]
            for sym_ind,sym in enumerate(boards[self.lines[2][0]][self.lines[2][1]]):
                boards[self.lines[2][0]][self.lines[2][1]][sym_ind] = B[-1-sym_ind]
            for line_ind,line in enumerate(boards[self.lines[3][0]]):
                line[self.lines[3][1]] = C[line_ind]
        else:
            boards[self.lines[0][0]][self.lines[0][1]] = B
            for line_ind,line in enumerate(boards[self.lines[1][0]]):
                line[self.lines[1][1]] = C[-line_ind-1]
            for sym_ind,sym in enumerate(boards[self.lines[2][0]][self.lines[2][1]]):
                boards[self.lines[2][0]][self.lines[2][1]][sym_ind] = D[-1-sym_ind]
            for line_ind,line in enumerate(boards[self.lines[3][0]]):
                line[self.lines[3][1]] = A[-line_ind-1]
        if self.top != None:
            rotate(self.top,direction,self.top_dir)
        
    def refresh(self):
        if self.refresh_countdown == 0:
            self.image = horizontal["base"]
            self.can_be_used = True
        else:
            self.refresh_countdown -=1