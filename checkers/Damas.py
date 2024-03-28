# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:05:12 2019

@author: lucas
"""
import pygame
import sys

SIZE = 800
SQUARE = SIZE/8
print(SQUARE)

pygame.init()
WINDOW = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Checkers')
WHITE = pygame.image.load('C:/Lucas things/Projects/Games/Carpeta-de-juegos/checkers/white_checkers_piece.png')
BLACK = pygame.image.load('C:/Lucas things/Projects/Games/Carpeta-de-juegos/checkers/black_checkers_piece.png')
WHITE_KING = pygame.image.load('C:/Lucas things/Projects/Games/Carpeta-de-juegos/checkers/white_checkers_king.png')
BLACK_KING = pygame.image.load('C:/Lucas things/Projects/Games/Carpeta-de-juegos/checkers/black_checkers_king.png')
BOARD = pygame.image.load('C:/Lucas things/Projects/Games/Carpeta-de-juegos/checkers/checkers_board.png')
#Will need to implement a rules tab because of the different version of checkers
GREEN = (119, 153, 81)

player1 = ["X", "K"]
player2 = ["O", "Q"]
kings = ["K", "Q"]

def draw_board(matriz):
    WINDOW.blit(BOARD, (0, 0))
    for i, row in enumerate(matriz):
        for j, square in enumerate(row):
            if(square == "X"):
                WINDOW.blit(WHITE, (j * SQUARE + 2, i * SQUARE + 2))
            if(square == "O"):
                WINDOW.blit(BLACK, (j * SQUARE + 2, i * SQUARE + 2))
            if(square == "K"):
                WINDOW.blit(WHITE_KING, (j * SQUARE + 2, i * SQUARE + 2))
            if(square == "Q"):
                WINDOW.blit(BLACK_KING, (j * SQUARE + 2, i * SQUARE + 2))
    pygame.display.update()

def highlight_select(matriz, coords):
    print("Entro aqui")
    y,x = coords[0]*SQUARE, coords[1]*SQUARE
    pygame.draw.rect(WINDOW, GREEN, (x, y, SQUARE, SQUARE))
    if(matriz[coords[0]][coords[1]] == "X"):
        WINDOW.blit(WHITE, (x + 2, y + 2))
    if(matriz[coords[0]][coords[1]] == "O"):
        WINDOW.blit(BLACK, (x + 2, y + 2))
    if(matriz[coords[0]][coords[1]] == "K"):
        WINDOW.blit(WHITE_KING, (x + 2, y + 2))
    if(matriz[coords[0]][coords[1]] == "Q"):
        WINDOW.blit(BLACK_KING, (x + 2, y + 2))
    pygame.display.update()

def crear_tablero():
    size = 8
    matriz=[]
    x="_"
    for i in range(size):
        fila=[]
        for j in range(size):
            fila.append(x)
        matriz.append(fila)
    return matriz

def armar_tablero(matriz):
    num1 = 12
    place = False
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(num1 > 0 and place):
                matriz[i][j] = player1[0]
                matriz[-i-1][-j-1] = player2[0]   
                num1-=1
            place = not place
        place = not place
    return matriz

def move(player_sym, enemy_sym, pos, matriz):
    piece = matriz[pos[0][0]][pos[0][1]]
    saltos = len(pos) - 1
    #Move and capture
    if(abs(pos[1][0] - pos[0][0]) == 2):
        matriz[pos[0][0]][pos[0][1]] = "_"
        for i in range(saltos):
            print(pos[i][0] + (-1 if(pos[i+1][0] < pos[i][0]) else 1), pos[i][1] + (-1 if(pos[i+1][1] < pos[i][1]) else 1))
            if(matriz[pos[i][0] + (-1 if(pos[i+1][0] < pos[i][0]) else 1)]
               [pos[i][1] + (-1 if(pos[i+1][1] < pos[i][1]) else 1)] in enemy_sym):
                matriz[pos[i][0] + (-1 if(pos[i+1][0] < pos[i][0]) else 1)][pos[i][1] + (-1 if(pos[i+1][1] < pos[i][1]) else 1)] = "_"
        matriz[pos[-1][0]][pos[-1][1]] = piece

    #Move one space
    if(abs(pos[1][0] - pos[0][0]) == 1):
        matriz[pos[0][0]][pos[0][1]] = "_"  
        matriz[pos[-1][0]][pos[-1][1]] = piece

#CHECK FOR KINGS
def movida_valida(player_sym, enemy_sym, pos, matriz):
    piece = matriz[pos[0][0]][pos[0][1]]
    if(piece not in player_sym):
        return "Not a valid piece"

    saltos = len(pos) - 1

    # Checking if inside board
    if(any((a[0]<0 or a[0]>7 or a[1]<0 or a[1]>7) for a in pos)):
           return "coordinate outside of map"
    
    #Checking if squares empty
    moves = []
    for i in pos[1:]:
        moves.append(Tablero[i[0]][i[1]])
    if(any(coordinate != "_" for coordinate in moves)):
        return "requires empty square"

    #Checking if diagonal
    for i in range(saltos):
        if(abs(pos[i+1][0] - pos[i][0]) != abs(pos[i+1][1] - pos[i][1])):
            return "should be diagonal"
        
    #Checking if forward and correct distance unless king
    if(piece not in kings):
        for i in range(saltos):
            if(pos[i][0] >= pos[i+1][0] and piece in player1):
                return "should be forward"
            if(pos[i][0] <= pos[i+1][0] and piece in player2):
                return "should be forward"
            
    #Check number of moves
    if((pos[i+1][0] - pos[i][0]) == 1):
        if(len(pos) > 2):
            return "invalid number of moves"

    #Checking for correct distance
    if(any(abs(pos[i+1][0] - pos[i][0]) != 2 for i in range(saltos)) 
            and any(abs(pos[i+1][0] - pos[i][0]) != 1 for i in range(saltos))):
        return "invalid distance"

    #Check if there is a piece to jump
    if(abs(pos[i+1][0] - pos[i][0]) == 2):
        for i in range(saltos):
            if(matriz[pos[i][0] + (-1 if(pos[i+1][0] < pos[i][0]) else 1)]
                    [pos[i][1] + (-1 if(pos[i+1][1] < pos[i][1]) else 1)] == "_"):
                return "no piece to jump"

def finish_condition(matriz, player_sym, enemy_sym, second_turn):
    num_pieces = [i.count(enemy_sym[0]) for i in matriz] 
    num_pieces.append(sum([i.count(enemy_sym[1]) for i in matriz]))
    if(sum(num_pieces) == 0):
        return player_sym[0] + " wins by eliminating " + enemy_sym[0] + "`s pieces", True
    possible_mov_player = []
    possible_mov_enemy = []
    #Check for available moves, needs to check for kings
    for row in range(len(matriz)):
        for column in range(len(matriz)):
            pos = [row, column]
            options = [[pos[0]+1, pos[1]+1], [pos[0]+1, pos[1]-1], [pos[0]+2, pos[1]+2], [pos[0]+2, pos[1]-2],
                       [pos[0]-1, pos[1]+1], [pos[0]-1, pos[1]-1], [pos[0]-2, pos[1]+2], [pos[0]-2, pos[1]+2]]
            if(matriz[row][column] in player1):
                for i in options:
                    if(options.index(i) > 3 and matriz[row][column] not in kings):
                        break
                    possible_mov_player.append(bool(movida_valida(player1, player2, [pos, i], matriz)))
            if(matriz[row][column] in player2): 
                for i in options:
                    if(options.index(i) < 4 and matriz[row][column] not in kings):
                        continue
                    possible_mov_enemy.append(bool(movida_valida(player2, player1, [pos, i], matriz)))

    print(possible_mov_player)
    print(possible_mov_enemy)
    if(all(possible_mov_player) and all(possible_mov_enemy)):
       return "Tie by inability to move", True
    if(all(possible_mov_player)):
        if(second_turn):
            return enemy_sym[0] + " wins by blocking " + player_sym[0], False
        return False, True
    if(all(possible_mov_enemy)):
       if(second_turn):
           return player_sym[0] + " wins by blocking " + enemy_sym[0], False
       return False, True
    return False, False
     
Tablero = crear_tablero()
Tablero = armar_tablero(Tablero)
draw_board(Tablero)
second_turn_1 = False
second_turn_2 = False

while True:
    #Player 1 turn
    positions = []
    while not second_turn_1:
        turn = True
        for event in pygame.event.get():                    
            if event.type== pygame.QUIT:
                print('EXIT SUCCESSFUL')
                pygame.quit()
                sys.exit()
            if(event.type == pygame.MOUSEBUTTONDOWN):
                x,y = pygame.mouse.get_pos()
                column = int(x//SQUARE)
                row = int(y//SQUARE)
                piece = Tablero[row][column]
                if(piece in player1):
                    positions = [(row, column)]
                    draw_board(Tablero)
                    highlight_select(Tablero, positions[0])
                    continue
                if(positions):
                    positions.append((row, column))
                    highlight_select(Tablero, positions[-1])
                if(len(positions) >= 2):
                    error = movida_valida(player1, player2, positions, Tablero)
                    if(error):
                        print("Not a valid movement,", error)
                        draw_board(Tablero)
                        positions = []
                       
                #two options, if jump keep looking for moves while maintaining positions for card or get all positions instantly
            if(event.type == pygame.KEYDOWN and len(positions) >= 2):
                print("Termino") 
                if(event.key == pygame.K_SPACE):
                    turn = False
                    break
            print(positions)
        if(turn):
            continue
        print("Turn finished")
        move(player1, player2, positions, Tablero)
        if(positions[-1][0] == 7):
            Tablero[positions[-1][0]][positions[-1][1]] = "K"
        draw_board(Tablero)
        break
    winner, second_turn_1 = finish_condition(Tablero, player1, player2, second_turn_1)
    if(winner):
        print(winner)
        break

    #Player 2 turn
    positions = []
    while not second_turn_2:
        turn = True
        for event in pygame.event.get():                    
            if event.type== pygame.QUIT:
                print('EXIT SUCCESSFUL')
                pygame.quit()
                sys.exit()
            if(event.type == pygame.MOUSEBUTTONDOWN):
                x,y = pygame.mouse.get_pos()
                column = int(x//SQUARE)
                row = int(y//SQUARE)
                piece = Tablero[row][column]
                if(piece in player2):
                    positions = [(row, column)]
                    draw_board(Tablero)
                    highlight_select(Tablero, positions[0])
                    continue
                if(positions):
                    positions.append((row, column))
                    highlight_select(Tablero, positions[-1])
                if(len(positions) >= 2):
                    error = movida_valida(player2, player1, positions, Tablero)
                    if(error):
                        print("Not a valid movement,", error)
                        draw_board(Tablero)
                        positions = []
            if(event.type == pygame.KEYDOWN):
                print("Termino") 
                if(event.key == pygame.K_SPACE):
                    turn = False
                    break
            print(positions)
        if(turn):
            continue
        print("Turn finished")
        move(player2, player1, positions, Tablero)
        if(positions[-1][0] == 0):
            Tablero[positions[-1][0]][positions[-1][1]] = "Q"
        draw_board(Tablero)
        break
    winner, second_turn_2 = finish_condition(Tablero, player2, player1, second_turn_2)
    if(winner):
        print(winner)
        break