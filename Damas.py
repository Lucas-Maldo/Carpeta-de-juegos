# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:05:12 2019

@author: lucas
"""

#Keep testing for player 2
#Error with  single move for player 2
Tablero = [["X","_","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","_","_","_","_","_","_","_"],
           ["_","O","_","O","_","O","_","O"]]
# Tablero = [["X","_","_","_","_","_","_","_"],
#            ["_","_","_","_","_","_","_","_"],
#            ["_","_","_","_","_","_","_","_"],
#            ["_","_","_","_","_","_","_","_"],
#            ["_","_","_","_","_","_","_","_"],
#            ["_","_","_","X","_","X","_","_"],
#            ["X","_","X","_","X","_","X","_"],
#            ["_","O","_","O","_","O","_","O"]]
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
    pass

#CHECK FOR KINGS, maybe just add an or case for if piece == QQ or another letter
def movida_valida(player_sym, enemy_sym, pos, matriz):
    saltos = len(pos) - 1

    # print("Checking if inside board") #perfect
    if(any((a[0]<0 or a[0]>7 or a[1]<0 or a[1]>7) for a in pos)):
           return "coordinate outside of map"
    
    # print("Checking if squares empty")
    moves = []
    print(pos)
    for i in pos[1:]:
        moves.append(Tablero[i[0]][i[1]])
    if(any(coordinate != "_" for coordinate in moves)):
        return "requires empty square"

    if(player_sym == "O"):
        pos = pos[::-1]

    # print("Checking if forward")#Should be ok but check for player 2
    for i in range(saltos):
        if(pos[i][0] >= pos[i+1][0]):
            return "should be forward"
        
    # print("Checking if diagonal")#Should be ok but check for player 2
    for i in range(saltos):
        if(pos[i+1][0] - pos[i][0] != abs(pos[i+1][1] - pos[i][1])):
            return "should be diagonal"

    # print("Checking for capture") #Have to check for multiple cases 
    if(any(pos[i+1][0] - pos[i][0] != 2 for i in range(saltos)) 
            and any(pos[i+1][0] - pos[i][0] != 1 for i in range(saltos))):
        return "invalid distance"
    
    if(pos[i+1][0] - pos[i][0] == 2):
        for i in range(saltos):
            if(matriz[pos[i][0] + 1]
                    [pos[i][1]+ abs(pos[i+1][1] - pos[i][1])//2 * (-1 if(pos[i+1][1] - pos[i][1] < 0) else 1)]
            == "_"):
                return "no piece to jump"
    # capture = False
    # for i in range(saltos):
    #     if(matriz[pos[i][0] + 1]
    #        [pos[i][1]+ abs(pos[i+1][1] - pos[i][1])//2 * (-1 if(pos[i+1][1] - pos[i][1] < 0) else 1)]
    #         != "_"):
    #         capture = True
    #maybe a if(any(pos[i+1][0] - pos[i][0] != 2 for i in range(saltos)) 
    #           and any(pos[i+1][0] - pos[i][0] != 1 for i in range(saltos)))
    #then the movement is invalid, independent of capture or not
    # if(capture):
    if(pos[1][0] - pos[0][0] == 2):
        #maybe an if(pos[i+1][0] - pos[i][0] != 2) because results are already
        #filtered as only all 2 space jump or all 1 space jump
        #and so we only vall the applying capture and applying movement plus imprimir_tablero
        #All this will need to be thoroughly checked
        # for i in range(saltos):
        #     if(pos[i+1][0] - pos[i][0] != 2):
        #         if(player_sym == "O"):
        #             return "invalid jump to "+ str(pos[i])
        #         return "invalid jump to "+ str(pos[i+1])
        #Applying capture
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
    if(pos[1][0] - pos[0][0] == 1):
        # if(pos[1][0] - pos[0][0] > 1):
        #     return "should be no more than one space" 
        #Applying movment
        if(player_sym == "O"):
            matriz[pos[-1][0]][pos[-1][1]] = "_"
        else:
            matriz[pos[0][0]][pos[0][1]] = "_"  
        if(player_sym == "O"):
            matriz[pos[0][0]][pos[0][1]] = player_sym
        else:
            matriz[pos[-1][0]][pos[-1][1]] = player_sym
    imprimir_tablero(matriz)   

def finish_condition(matriz, player_sym, enemy_sym):
    num_pieces = [i.count(enemy_sym) for i in matriz] 
    if(sum(num_pieces) == 0):
        return player_sym
    #Check for left right single or jump moves for X and O player for every piece
    #if all pieces throw error then cant move
    #If this is true for both players then tie
    #ESTO NO VA A FUNCIONAR PORQUE EL MOVIMIENTO ESTA EN EL CHECQUEO, ASIQUE CADA VEZ QUE REVISE LO VA A MOVER
    #CHECKEAR EL PASO A PASO HAY COSAS RARAS
    #Cuando salta a una ficha de su propio tipo y cae en una del oponente se la come
    #Algo raro ocurre cuando intenta moverse hacia un lugar que ya tiene su propia ficha
    #Agregar una funciona movimiento o captura que se encaruge del movimiento, asi poder de dejar la funcion mover condicion libre
    possible_mov1 = []
    possible_mov2 = []
    extra = 0
    for row in range(len(matriz)):
        for column in range(len(matriz)):
            pos = [row, column]
            # print("Revisando jugador", matriz[row][column])
            if(matriz[row][column] == "X"):   
                extra+=1
                possible_mov1.append(bool(movida_valida("X", "O", [pos, [pos[0]+1, pos[1]+1]], matriz)))
                possible_mov1.append(bool(movida_valida("X", "O", [pos, [pos[0]+1, pos[1]-1]], matriz)))
                possible_mov1.append(bool(movida_valida("X", "O", [pos, [pos[0]+2, pos[1]+2]], matriz)))
                possible_mov1.append(bool(movida_valida("X", "O", [pos, [pos[0]+2, pos[1]-2]], matriz)))
            # if(matriz[row][column] == "O"): 
            #     extra+=1
            #     possible_mov2.append(bool(movida_valida("O", "X", [pos, [pos[0]-1, pos[1]+1]], matriz)))
            #     possible_mov2.append(bool(movida_valida("O", "X", [pos, [pos[0]-1, pos[1]-1]], matriz)))
            #     possible_mov2.append(bool(movida_valida("O", "X", [pos, [pos[0]-2, pos[1]+2]], matriz)))
            #     possible_mov2.append(bool(movida_valida("O", "X", [pos, [pos[0]-2, pos[1]-2]], matriz)))
    imprimir_tablero(matriz)
    print(extra)
    print(len(possible_mov1))
    print(len(possible_mov2))
            #Check for every piece if it can move
    return False
     
# Tablero = crear_tablero()
# Tablero = armar_tablero(Tablero)

while True:
    #Player 1 turn
    while True:
        imprimir_tablero(Tablero)
        posicion1 = input("Player " + player1 + " select a piece by its coordinates: ").split(",")
        posicion1 = list(int(item) for item in posicion1)
        print(posicion1)
        if(Tablero[posicion1[0]][posicion1[1]] != player1):
            print("Not a valid piece")
            continue
        posicion2 = input("Select a place to move to: ").split(" ")
        posicion2 = list(list(int(item) for item in coord.split(",")) for coord in posicion2)
        #Check if valid space
        # pos = []
        # for i in posicion2:
        #     pos.append(Tablero[i[0]][i[1]])
        # if(any(coordinate != "_" for coordinate in pos)):
        #     print("Requires empty square")
        #     continue
        error = movida_valida(player1, player2, [posicion1] + posicion2, Tablero)
        if(error):
            print("Not a valid movement,", error)
            continue
        else:
            print("Valid move")
            break
    winner = finish_condition(Tablero, player1, player2)
    if(winner):
        print("Ganador", winner)
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
        # pos = []
        # for i in posicion2:
        #     pos.append(Tablero[i[0]][i[1]])
        # if(any(coordinate != "_" for coordinate in pos)):
        #     print("Requires empty square")
        #     continue
        error = movida_valida(player2, player1, [posicion1] + posicion2, Tablero)
        if(error):
            #Contador con todas las movidas posibles? y si eso igual a cantidad de errores entonces gano el otro?
            print("Not a valid movement,", error)
            continue
        else:
            print("Valid move")
            break
    winner = finish_condition(Tablero, player2, player1)
    if(winner):
        print("Ganador", winner)
        break