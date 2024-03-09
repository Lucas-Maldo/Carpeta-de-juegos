# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:22:30 2019

@author: lucas
"""
import pygame as pg
import sys
from pygame.locals import *


WIN_SIZE = 900
CELL_SIZE = WIN_SIZE // 3
CELL_CENTER = CELL_SIZE//2
board_path = "resources\\tic_tac_toe_images\\board_tic_tac.png"
x_path = "resources\\tic_tac_toe_images\X_tic_tac.png"
o_path = "resources\\tic_tac_toe_images\O_tic_tac.png"

class Game():
    def __init__(self):
        pg.init()
        self.board = pg.transform.smoothscale(pg.image.load(board_path), [WIN_SIZE] *2)
        self.X_image = pg.transform.smoothscale(pg.image.load(x_path), [CELL_SIZE] *2)
        self.O_image = pg.transform.smoothscale(pg.image.load(o_path), [CELL_SIZE] *2)
        self.screen = pg.display.set_mode([WIN_SIZE] * 2)
        self.screen.blit(self.board, (0,0))
        self.clock = pg.time.Clock()
        pg.display.set_caption( 'TIC TAC TOE' )
        self.font = pg.font.SysFont('Verdana', CELL_SIZE // 4, True)
        self.font2 = pg.font.SysFont('Verdana', CELL_SIZE // 10, True)
        self.matriz = [[" "]*3, [" "]*3, [" "]*3]
        # self.players = ["X", "O"]
        self.current_player = "X"
        self.win_coords = []

    def display(self):
        for x, row in enumerate(self.matriz):
            for y, item in enumerate(row):
                if (item != " " and self.win_coords == []):
                    self.screen.blit(self.X_image if (item == "X") else self.O_image, (y * CELL_SIZE, x * CELL_SIZE))

    def check_events(self):
        for event in pg.event.get():
            if(event.type == MOUSEBUTTONDOWN and self.win_coords == []):
                y,x = event.pos
                if(self.matriz[x//300][y//300] == " "):
                    self.matriz[x//300][y//300] = self.current_player
                    if(self.current_player == "X"):
                        self.current_player = "O"
                    else:
                        self.current_player = "X"
            if(event.type == KEYDOWN):
                if(event.key == pg.K_SPACE):
                    self.__init__()
            if event.type == QUIT:
                pg.quit()
                sys.exit()

    def check_finish(self):
        #filas:
        for i in range(len(self.matriz)):
            if(self.matriz[i].count("X") == 3):
                self.win_coords = [[0,i],[2,i]]
                return "Player 1 wins!"
            if(self.matriz[i].count("O") == 3):
                self.win_coords = [[0,i],[2,i]]
                return "Player 2 wins!"
        #columnas        
        for i in range(len(self.matriz)):
            if(self.matriz[0][i] + self.matriz[1][i] + self.matriz[2][i] == "XXX"):
                self.win_coords = [[i, 0], [i, 2]]
                return "Player 1 wins!"
            if(self.matriz[0][i] + self.matriz[1][i] + self.matriz[2][i] == "OOO"):
                self.win_coords = [[i, 0], [i, 2]]
                return "Player 2 wins!"
        #diagonal
        diagonal = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]
        diagonal_op = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]
        if(diagonal == "XXX" or diagonal_op == "XXX"):
            self.win_coords = [[0,0],[2,2]]
            return "Player 1 wins!"
        if(diagonal == "OOO" or diagonal_op == "OOO"):
            self.win_coords = [[0,2],[2,0]]
            return "Player 2 wins!"
        #vacios
        open_squares = sum(i.count(' ') for i in self.matriz)
        if(open_squares == 0):
            return "It was a tie."
    
    def draw_win(self, message):
        if(self.win_coords != []):
            self.win_coords = [[i * CELL_SIZE + CELL_CENTER for i in item] for item in self.win_coords]
            # print(self.win_coords)
            pg.draw.line(self.screen, 'red', *self.win_coords, CELL_SIZE // 8)
            label = self.font.render(message, True, 'white', 'black')
            self.screen.blit(label, (WIN_SIZE // 2 - label.get_width() // 2, WIN_SIZE // 3))
            label = self.font2.render("(Space to restart)", True, 'white', 'black')
            self.screen.blit(label, (WIN_SIZE // 2 - label.get_width() // 2, WIN_SIZE // 2))
            pg.display.update()
    
    def play(self):
        while True:
            self.check_events()
            self.display()
            pg.display.update()
            message = self.check_finish()
            if(message):
                self.draw_win(message)
                # break

game = Game()
game.play()
 