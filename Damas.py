# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:05:12 2019

@author: lucas
"""

#Keep testing for player 2
Tablero = [["_","_","_","_","_","_","_","_"],
           ["_","_","_","_","_","X","_","_"],
           ["_","_","_","_","X","_","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","_","O","_","O","_","_","_"],
           ["_","O","_","_","_","O","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"]]

# Tablero = [["_","X","_","X","_","X","_","X"],
#            ["O","_","X","_","X","_","X","_"],
#            ["_","_","_","_","_","_","_","_"],
#            ["O","_","_","_","X","_","_","_"],
#            ["_","_","_","O","_","X","_","_"],
#            ["_","_","_","_","O","_","O","_"],
#            ["_","_","_","O","_","_","_","O"],
#            ["_","_","O","_","O","_","O","_"]]

player1 = "X"
player2 = "O"

def imprimir_tablero(matriz):
    print("  ", end = " ")
    for i in range(len(matriz)):
        print(i, end = " ")
    print()
    for i in range(len(matriz)):
        print(i, end = " ")
        for j in range(len(matriz)):
            print('|' + matriz[i][j], end = "")
        print("|", i)
    print("  ", end = " ")
    for i in range(len(matriz)):
        print(i, end = " ")
    print()

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
                matriz[i][j] = player1
                matriz[-i-1][-j-1] = player2    
                num1-=1
            place = not place
        place = not place
    return matriz

def move(player_sym, enemy_sym, pos, matriz):
    saltos = len(pos) - 1
    #Move and capture
    if(abs(pos[1][0] - pos[0][0]) == 2):
        matriz[pos[0][0]][pos[0][1]] = "_"

        if(player_sym == "O"):
            pos = pos[::-1]
        for i in range(saltos):
            if(matriz[pos[i][0] + 1][pos[i][1] + (pos[i+1][1] - pos[i][1])//2] == enemy_sym):
                matriz[pos[i][0] + 1][pos[i][1] + (pos[i+1][1] - pos[i][1])//2] = "_"
        if(player_sym == "O"):
            pos = pos[::-1]

        matriz[pos[-1][0]][pos[-1][1]] = player_sym
    #Move one space
    if(abs(pos[1][0] - pos[0][0]) == 1):
        matriz[pos[0][0]][pos[0][1]] = "_"  
        matriz[pos[-1][0]][pos[-1][1]] = player_sym


#CHECK FOR KINGS, maybe just add an or case for if piece == QQ or another letter
def movida_valida(player_sym, enemy_sym, pos, matriz):
    if(matriz[pos[0][0]][pos[0][1]] != player_sym):
        return "Not a valid piece"

    saltos = len(pos) - 1

    # print("Checking if inside board") #perfect
    if(any((a[0]<0 or a[0]>7 or a[1]<0 or a[1]>7) for a in pos)):
           return "coordinate outside of map"
    
    # print("Checking if squares empty")
    moves = []
    for i in pos[1:]:
        moves.append(Tablero[i[0]][i[1]])
    if(any(coordinate != "_" for coordinate in moves)):
        return "requires empty square"

    if(player_sym == "O"):
        pos = pos[::-1]

    # print("Checking if forward")
    for i in range(saltos):
        if(pos[i][0] >= pos[i+1][0]):
            return "should be forward"
        
    # print("Checking if diagonal")
    for i in range(saltos):
        if(pos[i+1][0] - pos[i][0] != abs(pos[i+1][1] - pos[i][1])):
            return "should be diagonal"

    # print("Checking for correct distance")
    if(any(pos[i+1][0] - pos[i][0] != 2 for i in range(saltos)) 
            and any(pos[i+1][0] - pos[i][0] != 1 for i in range(saltos))):
        return "invalid distance"
    
    #Check if there is a piece to jump
    if(pos[i+1][0] - pos[i][0] == 2):
        for i in range(saltos):
            if(matriz[pos[i][0] + 1]
                    [pos[i][1]+ abs(pos[i+1][1] - pos[i][1])//2 * (-1 if(pos[i+1][1] - pos[i][1] < 0) else 1)]
            == "_"):
                return "no piece to jump"
            
    # move(player_sym, enemy_sym, pos, matriz)
    # imprimir_tablero(matriz)   

def finish_condition(matriz, player_sym, enemy_sym, second_turn):
    num_pieces = [i.count(enemy_sym) for i in matriz] 
    if(sum(num_pieces) == 0):
        return player_sym + " wins by eliminating " + enemy_sym + "`s pieces", False
    #CHECKEAR EL PASO A PASO HAY COSAS RARAS
    possible_mov_player = []
    possible_mov_enemy = []
    extra = 0
    for row in range(len(matriz)):
        for column in range(len(matriz)):
            pos = [row, column]
            if(matriz[row][column] == "X"):   
                extra+=1
                possible_mov_player.append(bool(movida_valida("X", "O", [pos, [pos[0]+1, pos[1]+1]], matriz)))
                possible_mov_player.append(bool(movida_valida("X", "O", [pos, [pos[0]+1, pos[1]-1]], matriz)))
                possible_mov_player.append(bool(movida_valida("X", "O", [pos, [pos[0]+2, pos[1]+2]], matriz)))
                possible_mov_player.append(bool(movida_valida("X", "O", [pos, [pos[0]+2, pos[1]-2]], matriz)))
            if(matriz[row][column] == "O"): 
                extra+=1
                possible_mov_enemy.append(bool(movida_valida("O", "X", [pos, [pos[0]-1, pos[1]+1]], matriz)))
                possible_mov_enemy.append(bool(movida_valida("O", "X", [pos, [pos[0]-1, pos[1]-1]], matriz)))
                possible_mov_enemy.append(bool(movida_valida("O", "X", [pos, [pos[0]-2, pos[1]+2]], matriz)))
                possible_mov_enemy.append(bool(movida_valida("O", "X", [pos, [pos[0]-2, pos[1]-2]], matriz)))
    # print(possible_mov_player)
    # print(possible_mov_enemy)
    if(all(possible_mov_player) and all(possible_mov_enemy)):
       return "Tie by inability to move", False
    if(all(possible_mov_player)):
        if(second_turn):
            return enemy_sym + " wins by blocking " + player_sym
        return False, True
    if(all(possible_mov_enemy)):
       if(second_turn):
           return player_sym + " wins by blocking " + enemy_sym, False
       return False, True

    return False, False
     
# Tablero = crear_tablero()
# Tablero = armar_tablero(Tablero)
imprimir_tablero(Tablero)
second_turn_1 = False
second_turn_2 = False

while True:
    #Player 1 turn
    while True:
        posicion1 = input("Player " + player1 + " select a piece by its coordinates: ").split(",")
        posicion1 = list(int(item) for item in posicion1)
        print(posicion1)
        if(Tablero[posicion1[0]][posicion1[1]] != player1):
            print("Not a valid piece")
            continue
        posicion2 = input("Select a place to move to: ").split(" ")
        posicion2 = list(list(int(item) for item in coord.split(",")) for coord in posicion2)

        error = movida_valida(player1, player2, [posicion1] + posicion2, Tablero)
        if(error):
            print("Not a valid movement,", error)
            imprimir_tablero(Tablero)
            continue
        else:
            print("Valid move")
            move(player1, player2, [posicion1] + posicion2, Tablero)
            imprimir_tablero(Tablero)
            break
    winner, second_turn_1 = finish_condition(Tablero, player1, player2, second_turn_1)
    if(winner):
        print(winner)
        break

    #Player 2 turn
    while True:
        posicion1 = input("Player " + player2 + " select a piece by its coordinates: ").split(",")
        posicion1 = list(int(item) for item in posicion1)
        print(posicion1)
        if(Tablero[posicion1[0]][posicion1[1]] != player2):
            print("Not a valid piece")
            continue
        posicion2 = input("Select a place to move to: ").split(" ")
        posicion2 = list(list(int(item) for item in coord.split(",")) for coord in posicion2)

        error = movida_valida(player2, player1, [posicion1] + posicion2, Tablero)
        if(error):
            print("Not a valid movement,", error)
            imprimir_tablero(Tablero)
            continue
        else:
            print("Valid move")
            move(player2, player1, [posicion1] + posicion2, Tablero)
            imprimir_tablero(Tablero)
            break
    winner, second_turn_2 = finish_condition(Tablero, player2, player1, second_turn_2)
    if(winner):
        print(winner)
        break