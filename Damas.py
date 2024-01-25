# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:05:12 2019

@author: lucas
"""

#combine pos1 and pos2 into one list 
Tablero = [["X","_","_","_","_","_","_","_"],
           ["_","X","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","X","_","O","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","X","_","O","_","X","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"]]
#Damas
def imprimir_tablero(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print('|' + matriz[i][j], end = "")
        print("|")

def crear_tablero():
    matriz=[]
    x="_"
    for i in range(8):
        fila=[]
        for j in range(8):
            fila.append(x)
        matriz.append(fila)
    return matriz

def armar_tablero(matriz):
    num1 = 12
    num2 = 12
    for i in range(len(matriz)):
        for j in range(1 if i%2==0 else 0,len(matriz),2):
            if(num1 > 0):
                matriz[i][j] = "X"
                matriz[-i-1][j] = "O"
                num1-=1
    return matriz
#CHECK FOR JUMPS for second player (maybe can be changed from before to be unnecesary)
#CHECK FOR KINGS, maybe just add an or case for if piece == QQ or another letter
def movida_valida(player, pos1, pos2, matriz):
    len_pos2 = len(pos2)
    #Check if inside board
    if(any((a[0]<0 or a[0]>7 or a[1]<0 or a[1]>7) for a in pos2)):
           return "coordinate outside of map"
    if(player == 1):
        #Check if forward
        if(pos1[0] >= pos2[0][0]):
            return "should be forward1"
        for i in range(len(pos2[0:-1])):
            if(pos2[i][0] >= pos2[i+1][0]):
                return "should be forward2"
        #Check diagonal
        if(pos2[0][0] - pos1[0] != abs(pos2[0][1] - pos1[1])):
            return "should be diagonal1"
        for i in range(len(pos2[0:-1])):
            if(pos2[i+1][0] - pos2[i][0] != abs(pos2[i+1][1] - pos2[i][1])):
                return "should be diagonal2"
    if(player == 2):
        #Check if forward
        if(pos1[0] <= pos2[0][0]):
            return "should be forward1"
        for i in range(len(pos2[0:-1])):
            if(pos2[i][0] <= pos2[i+1][0]):
                return "should be forward2"
        #Check if diagonal
        if(pos1[0] - pos2[0][0] != abs(pos1[1] - pos2[0][1])):
            return "should be diagonal1"
        for i in range(len(pos2[0:-1])):
            if(pos2[i][0] - pos2[i+1][0] != abs(pos2[i][1] - pos2[i+1][1])):
                return "should be diagonal2"
    #Check jump
    jump = False
    #Esto podria estar malo para jugador 2
    if(matriz[pos1[0]+1][pos1[1]+(pos2[0][1] - pos1[1])//2] != "_"):
        if(len(pos2)>1):
            print(len(pos2))
            for i in range(len(pos2[0:-1])):
                if(matriz[pos2[i][0]+1][pos2[i][1]+(pos2[i+1][1] - pos2[i][1])//2] != "_"):
                    print("multiple jumps")
                    jump = True
        else:
            # print("single jump")
            jump = True
    if(jump):
        print("Entro")
        if(player == 1):
            if(pos2[0][0] - pos1[0] != 2):
                return "invalid jump"
            for i in range(len(pos2[0:-1])):
                if(pos2[i+1][0] - pos2[i][0] != 2):
                    return "invalid jump to"+str(pos2[i+1])
            matriz[pos1[0]][pos1[1]] = "_"
            if(matriz[pos1[0]+1][pos1[1]+(pos2[0][1] - pos1[1])//2] == "O"):
                matriz[pos1[0]+1][pos1[1]+(pos2[0][1] - pos1[1])//2] = "_"
            for i in range(len(pos2[0:-1])):
                if(matriz[pos2[i][0] + 1][pos2[i][1] + (pos2[i+1][1] - pos2[i][1])//2] == "O"):
                   matriz[pos2[i][0] + 1][pos2[i][1] + (pos2[i+1][1] - pos2[i][1])//2] = "_"
            matriz[pos2[-1][0]][pos2[-1][1]] = "X"
            # imprimir_tablero(Tablero)
        if(player == 2):
            if(pos1[0] - pos2[0][0] != 2):
                return "invalid jump"
            for i in range(len(pos2[0:-1])):
                if(pos2[i][0] - pos2[i+1][0] != 2):
                    return "invalid jump to"+str(pos2[i+1])
            matriz[pos1[0]][pos1[1]] = "_"
            if(matriz[pos1[0] - 1][pos1[1]- (pos1[1] - pos2[0][1])//2] == "X"):
                matriz[pos1[0] - 1][pos1[1]- (pos1[1] - pos2[0][1])//2] = "_"
            for i in range(len(pos2[0:-1])):
                if(matriz[pos2[i][0] - 1][pos2[i][1] - (pos2[i][1] - pos2[i+1][1])//2] == "X"):
                   matriz[pos2[i][0] - 1][pos2[i][1] - (pos2[i][1] - pos2[i+1][1])//2] = "_"
            matriz[pos2[-1][0]][pos2[-1][1]] = "O"
            imprimir_tablero(Tablero)

    else:
        if(player == 1):
            if(pos2[0][0] - pos1[0] + abs(pos2[0][1] - pos1[1]) > 2):
                return "should be no more than one space"
        


# Tablero = crear_tablero()
# Tablero = armar_tablero(Tablero)
imprimir_tablero(Tablero)

while True:
    while True:
        posicion1 = input("Select a piece by its coordinates: ").split(",")
        posicion1 = tuple(int(item) for item in posicion1)
        print(posicion1)
        pos = Tablero[posicion1[0]][posicion1[1]]
        if(pos != "X"):
            print("Not a valid piece")
            continue
    # while True:
        posicion2 = input("Select a place to move to: ").split(" ")
        posicion2 = list(tuple(int(item) for item in coord.split(",")) for coord in posicion2)
        print(posicion2)
        pos = []
        for i in posicion2:
            pos.append(Tablero[i[0]][i[1]])
        #Check if valid space
        if(any(coordinate != "_" for coordinate in pos)):
            print("Requires empty square")
            continue
        error = movida_valida(1, posicion1, posicion2, Tablero)
        if(error):
            #Contador con todas las movidas posibles? y si eso igual a cantidad de errores entonces gano el otro?
            print("Not a valid movement,", error)
            continue
        else:
            print("Valid move")
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
