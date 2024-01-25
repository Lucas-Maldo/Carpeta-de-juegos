# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:22:30 2019

@author: lucas
"""
import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="HELLO WORLD", backgroun="green", width=20, height=10)
greeting.pack()
window.mainloop()
print("Hello")
# def imprimir_tablero(matriz):
#     for i in range(len(matriz)):
#         for j in range(len(matriz)):
#             print('|' + matriz[i][j], end = "")
#         print("|")

# def crear_tablero():
#     matriz=[]
#     x=" "
#     for i in range(3):
#         fila=[]
#         for j in range(3):
#             fila.append(x)
#         matriz.append(fila)
#     return matriz

# def valid_spot(matriz, posicion):
#     if(matriz[posicion[0]][posicion[1]] != " "):
#         return False
#     return True

# def condicion_de_termino(matriz):
#     #filas:
#     for i in matriz:
#         if(i.count("X") == 3):
#             return "Jugador 1"
#         if(i.count("O") == 3):
#             return "Jugador 2"
#     #columnas        
#     for i in range(len(matriz)):
#         if(matriz[0][i] + matriz[1][i] + matriz[2][i] == "XXX"):
#             return "Jugador 1"
#         if(matriz[0][i] + matriz[1][i] + matriz[2][i] == "OOO"):
#             return "Jugador 2"
#     #diagonal
#     diagonal = matriz[0][0] + matriz[1][1] + matriz[2][2]
#     diagonal_op = matriz[0][2] + matriz[1][1] + matriz[2][0]
#     if(diagonal == "XXX" or diagonal_op == "XXX"):
#         return "Jugador 1"
#     if(diagonal == "OOO" or diagonal_op == "OOO"):
#         return "Jugador 2"

#     for i in matriz:
#         for j in i:
#             if j == " ":
#                 return False
            
# Tablero = crear_tablero()
# imprimir_tablero(Tablero)
# while True:
#     while True:
#         posicion = int(input("Jugador 1 elija una casilla del 1 al 9: "))-1
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