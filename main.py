#A simple chess bot developed in Python with Pygame front-end to display what the computer is thinking
#Chess Engine
#Features:
depth = 0x4
#Attempts every possible move
#Live display of back end to front end

import math, pygame, time, random
from pystockfish import *

deep = Engine(depth=depth)

pygame.init()
fps = 0x18
clock = pygame.time.Clock()
width, height = 0x190, 0x190
cursor = ["empty",'']
font = pygame.font.SysFont('Arial',0x20)
display = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
cream = (255, 209, 135)
brown = (156, 112, 31)
board_colours = [cream, brown]

abc = pygame.image.load("black_pawn.png")
acd = pygame.image.load("white_pawn.png")
kml = pygame.image.load("white_rook.png")
ytp = pygame.image.load("black_rook.png")
klp = pygame.image.load("white_bishop.png")
sqr = pygame.image.load("black_bishop.png")
zxz = pygame.image.load("black_queen.png")
aap = pygame.image.load("white_queen.png")
tap = pygame.image.load("black_king.png")
jsl = pygame.image.load("white_king.png")
ukc = pygame.image.load("black_knight.png")
lle = pygame.image.load("white_knight.png")

piece_textures = {"bpawn":abc,"wpawn":acd,"wrook":kml,"brook":ytp,"wbishop":klp,"bbishop":sqr,"bqueen":zxz,"wqueen":aap,"bking":tap,"wking":jsl,"bknight":ukc,"wknight":lle}
worth = {"bpawn":1,"wpawn":1,"wrook":5,"brook":5,"wbishop":3,"bbishop":3,"bqueen":9,"wqueen":9,"bking":0,"wking":0,"bknight":3,"wknight":3}

class Main:
    def __init__(self):
        self.tilesize = 0
        self.side = 'w'
        self.turn = 'w'
        self.tick = 0
        self.moves = []
        self.bfavour = 0
        self.wfavour = 0

    def init(self):
        self.side = input("side{ ").lower()

    def draw(self):
        for c in range(0,8):
            for r in range(0,8):
                if (c%2 == 0 and r%2 == 0) or (c%2 == 1 and r%2 == 1):
                    pygame.draw.rect(display, cream, (c * 50, r * 50, 50, 50))
                else:
                    pygame.draw.rect(display, brown, (c * 50, r * 50, 50, 50))
        self.bfavour,self.wfavour = 0,0
        for c in range(0,8):
            for r in range(0,8):
                if chess.board[r][c] != 'empty':
                    display.blit(piece_textures[chess.board[r][c]], (c * 50, r * 50))
                if chess.board[r][c][0] == 'b':
                    self.bfavour += worth[chess.board[r][c]]
                elif chess.board[r][c][0] == 'w':
                    self.wfavour += worth[chess.board[r][c]]

    def main(self):
        global cursor
        while 1:
            bestmove = deep.bestmove()['move']
            a = list(bestmove[0:2])
            b = list(bestmove[2:4])
            a[0] = ord(a[0]) - 0x61
            b[0] = ord(b[0]) - 0x61
            a[1] = int(a[1]) - 0x1
            b[1] = int(b[1]) - 0x1
            display.fill(black)
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.moves = []
                        self.turn = 'w'
                        chess.reset()
                        cursor = ['empty','']
                    if event.key == pygame.K_z:
                        chess.board[0][4] = 'empty'
                        chess.board[0][0] = 'empty'
                        chess.board[0][2] = 'bking'
                        chess.board[0][3] = 'brook'
                        sett = 'O-O-O'
                        self.moves.append(sett)
                        deep.setposition(self.moves)
                    elif event.key == pygame.K_x:
                        sett = 'O-O'
                        self.moves.append(sett)
                        deep.setposition(self.moves)
                    elif event.key == pygame.K_c:
                        sett = 'O-O-O'
                        self.moves.append(sett)
                        deep.setposition(self.moves)
                    elif event.key == pygame.K_v:
                        sett = 'O-O'
                        self.moves.append(sett)
                        deep.setposition(self.moves)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_pos[0] <= 400 and mouse_pos[1] <= 400:
                        if chess.board[mouse_pos[1]//50][mouse_pos[0]//50] != "empty" and cursor[0] == "empty":
                            if chess.board[mouse_pos[1]//50][mouse_pos[0]//50][0] == self.turn:
                                cursor[0] = chess.board[mouse_pos[1]//50][mouse_pos[0]//50]
                                l = str(chr(mouse_pos[0]//50+0x61))
                                k = str(0x8 - mouse_pos[1]//50)
                                cursor[1] = ''.join([l, k])
                                chess.board[mouse_pos[1]//50][mouse_pos[0]//50] = "empty"
                        else:
                            if self.turn == 'w':
                                self.turn = 'b'
                            elif self.turn == 'b':
                                self.turn = 'w'
                            chess.board[mouse_pos[1]//50][mouse_pos[0]//50] = cursor[0]
                            cursor[0] = "empty"
                            sett = ''.join([cursor[1], str(chr(mouse_pos[0]//50+0x61)), str(8 - mouse_pos[1]//50)])
                            self.moves.append(sett)
                            deep.setposition(self.moves)
            possible_moves = {}
            self.draw()
            pygame.draw.line(display, (0, 0, 0, 100), (a[0] * 50 + 25, (0x7 - a[1]) * 50 + 25), (b[0] * 50 + 25, (7 - b[1]) * 50 + 25), 3)
            if self.side == 'b':
                text = font.render("WPV: {}".format(self.wfavour), True, white, None)
                display.blit(text, (400, 0))
                text = font.render("BPV: {}".format(self.bfavour), True, white, None)
                display.blit(text, (400, 368))
            else:
                text = font.render("WPV: {}".format(self.wfavour), True, white, None)
                display.blit(text, (400, 368))
                text = font.render("BPV: {}".format(self.bfavour), True, white, None)
                display.blit(text, (400, 0))
            p = (self.wfavour/(self.bfavour+0.00001) - 0.5) * 100
            text = font.render("WPW: {}".format(int(p)), True, white, None)
            display.blit(text, (400, 184))
            if cursor[0] != "empty":
                display.blit(piece_textures[cursor[0]], (mouse_pos[0] + 10, mouse_pos[1] + 10))
            pygame.display.update()
            clock.tick(fps)
            self.tick += 1

class Chess:
    def __init__(self):
        if main.side == 'b':
            self.board = {0:{0:"wrook",1:"wknight",2:"wbishop",3:"wking",4:"wqueen",5:"wbishop",6:"wknight",7:"wrook"},
                          1:{0:"wpawn",1:"wpawn",2:"wpawn",3:"wpawn",4:"wpawn",5:"wpawn",6:"wpawn",7:"wpawn"},
                          2:{0:"empty",1:"empty",2:"empty",3:"empty",4:"empty",5:"empty",6:"empty",7:"empty"},
                          3:{0:"empty",1:"empty",2:"empty",3:"empty",4:"empty",5:"empty",6:"empty",7:"empty"},
                          4:{0:"empty",1:"empty",2:"empty",3:"empty",4:"empty",5:"empty",6:"empty",7:"empty"},
                          5:{0:"empty",1:"empty",2:"empty",3:"empty",4:"empty",5:"empty",6:"empty",7:"empty"},
                          6:{0:"bpawn",1:"bpawn",2:"bpawn",3:"bpawn",4:"bpawn",5:"bpawn",6:"bpawn",7:"bpawn"},
                          7:{0:"brook",1:"bknight",2:"bbishop",3:"bking",4:"bqueen",5:"bbishop",6:"bknight",7:"brook"}}
        else:
            self.board = {0:{0:"brook",1:"bknight",2:"bbishop",3:"bqueen",4:"bking",5:"bbishop",6:"bknight",7:"brook"},
                          1:{0:"bpawn",1:"bpawn",2:"bpawn",3:"bpawn",4:"bpawn",5:"bpawn",6:"bpawn",7:"bpawn"},
                          2:{0:"empty",1:"empty",2:"empty",3:"empty",4:"empty",5:"empty",6:"empty",7:"empty"},
                          3:{0:"empty",1:"empty",2:"empty",3:"empty",4:"empty",5:"empty",6:"empty",7:"empty"},
                          4:{0:"empty",1:"empty",2:"empty",3:"empty",4:"empty",5:"empty",6:"empty",7:"empty"},
                          5:{0:"empty",1:"empty",2:"empty",3:"empty",4:"empty",5:"empty",6:"empty",7:"empty"},
                          6:{0:"wpawn",1:"wpawn",2:"wpawn",3:"wpawn",4:"wpawn",5:"wpawn",6:"wpawn",7:"wpawn"},
                          7:{0:"wrook",1:"wknight",2:"wbishop",3:"wqueen",4:"wking",5:"wbishop",6:"wknight",7:"wrook"}}
        self.aboard = self.board
    def reset(self):
        if 1==1:
            self.board = {0:{0:"brook",1:"bknight",2:"bbishop",3:"bqueen",4:"bking",5:"bbishop",6:"bknight",7:"brook"},
                          1:{0:"bpawn",1:"bpawn",2:"bpawn",3:"bpawn",4:"bpawn",5:"bpawn",6:"bpawn",7:"bpawn"},
                          2:{0:"empty",1:"empty",2:"empty",3:"empty",4:"empty",5:"empty",6:"empty",7:"empty"},
                          3:{0:"empty",1:"empty",2:"empty",3:"empty",4:"empty",5:"empty",6:"empty",7:"empty"},
                          4:{0:"empty",1:"empty",2:"empty",3:"empty",4:"empty",5:"empty",6:"empty",7:"empty"},
                          5:{0:"empty",1:"empty",2:"empty",3:"empty",4:"empty",5:"empty",6:"empty",7:"empty"},
                          6:{0:"wpawn",1:"wpawn",2:"wpawn",3:"wpawn",4:"wpawn",5:"wpawn",6:"wpawn",7:"wpawn"},
                          7:{0:"wrook",1:"wknight",2:"wbishop",3:"wqueen",4:"wking",5:"wbishop",6:"wknight",7:"wrook"}}

main = Main()
chess = Chess()
main.main()
