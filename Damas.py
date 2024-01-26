# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:05:12 2019

@author: lucas
"""

#Keep testing for player 2
Tablero = [["X","_","_","_","_","_","_","_"],
           ["_","X","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","X","_","O","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","X","_","O","_","X","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"]]
Tablero = [["_","_","_","_","_","_","_","_"],
           ["_","O","_","_","_","_","_","_"],
           ["_","_","O","_","X","_","O","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","_","_","_","X","_","O","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","O","_"],
           ["_","_","_","_","_","_","_","O"]]

player1 = "X"
player2 = "O"

#Damas
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

#CHECK FOR KINGS, maybe just add an or case for if piece == QQ or another letter
def movida_valida_v2(player_sym, enemy_sym, pos, matriz):
    if(player_sym == "O"):
        pos = pos[::-1]
    saltos = len(pos) - 1

    print("Checking if inside board") #perfect
    if(any((a[0]<0 or a[0]>7 or a[1]<0 or a[1]>7) for a in pos)):
           return "coordinate outside of map"

    print("Checking if forward")#Should be ok but check for player 2
    for i in range(saltos):
        if(pos[i][0] >= pos[i+1][0]):
            return "should be forward"
        
    print("Checking if diagonal")#Should be ok but check for player 2
    for i in range(saltos):
        if(pos[i+1][0] - pos[i][0] != abs(pos[i+1][1] - pos[i][1])):
            return "should be diagonal"

    print("Checking for jump") #Have to check for multiple cases       
    jump = False
    for i in range(saltos):
        if(matriz[pos[i][0] + 1][pos[i][1] + (pos[i+1][1] - pos[i][1])//2] != "_"):
            print("valid jump")
            jump = True

    if(jump):
        for i in range(saltos):
            if(pos[i+1][0] - pos[i][0] != 2):
                if(player_sym == "O"):
                    return "invalid jump to "+ str(pos[i])
                return "invalid jump to "+ str(pos[i+1])
        #Applying jump
        if(player_sym == "O"):
            matriz[pos[-1][0]][pos[-1][1]] = "_"
        else:
            matriz[pos[0][0]][pos[0][1]] = "_"
        for i in range(saltos):
            if(matriz[pos[i][0] + 1][pos[i][1] + (pos[i+1][1] - pos[i][1])//2] == enemy_sym):
                matriz[pos[i][0] + 1][pos[i][1] + (pos[i+1][1] - pos[i][1])//2] = "_"
        if(player_sym == "O"):
            matriz[pos[0][0]][pos[0][1]] = player_sym
        else:
            matriz[pos[-1][0]][pos[-1][1]] = player_sym

    else:
        if(pos[1][0] - pos[0][0] > 1):
            return "should be no more than one space"        

Tablero = crear_tablero()
Tablero = armar_tablero(Tablero)
imprimir_tablero(Tablero)

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
        #Check if valid space
        pos = []
        for i in posicion2:
            pos.append(Tablero[i[0]][i[1]])
        if(any(coordinate != "_" for coordinate in pos)):
            print("Requires empty square")
            continue
        error = movida_valida_v2(player1, player2, [posicion1] + posicion2, Tablero)
        if(error):
            #Contador con todas las movidas posibles? y si eso igual a cantidad de errores entonces gano el otro?
            print("Not a valid movement,", error)
            continue
        else:
            print("Valid move")
            imprimir_tablero(Tablero)
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
        #Check if valid space
        pos = []
        for i in posicion2:
            pos.append(Tablero[i[0]][i[1]])
        if(any(coordinate != "_" for coordinate in pos)):
            print("Requires empty square")
            continue
        error = movida_valida_v2(player2, player1, [posicion1] + posicion2, Tablero)
        if(error):
            #Contador con todas las movidas posibles? y si eso igual a cantidad de errores entonces gano el otro?
            print("Not a valid movement,", error)
            continue
        else:
            print("Valid move")
            imprimir_tablero(Tablero)
            break
    break
#         fila = posicion//3
#         columna = posicion%3
#         if(valid_spot(Tablero, (fila, columna))):
#             Tablero[fila][columna] = "X"
#             break
#         print("Posicion no valida intente denuevo")    
#     imprimir_tablero(Tablero)
#     ganador = condicion_de_termino(Tablero)
#     if(ganador):
#         break
#     while True:
#         posicion = int(input("Jugador 2 elija una casilla del 1 al 9: "))-1
#         fila = posicion//3
#         columna = posicion%3
#         if(valid_spot(Tablero, (fila, columna))):
#             Tablero[fila][columna] = "O"
#             break
#         print("Posicion no valida intente denuevo")
#     imprimir_tablero(Tablero)
#     ganador = condicion_de_termino(Tablero)
#     if(ganador):
#         break
# print("Gano " + ganador)
