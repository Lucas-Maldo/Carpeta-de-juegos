#puedo mover el inicio y el final y agregar/borrar puntos entremedio
#puedo agregar/borrar murallas y si no hay caminos no imprimir
#puedo implementar distintos pathfinders
#quizas implementar para matriz de triangulos y hexagonos tambien

import pygame
import sys
import random

SIZE = 800
SQUARE = 16
LEN = int(SIZE/SQUARE)
# LEN = 10
FPS = 60

pygame.init()
WINDOW = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Pathfinder')
BACKGROUND_COLOR = (0, 140, 0)
START = (255, 255, 255)
WALL = (100, 100, 100)
END = (0, 0, 0)
PASSTHROUGH = (0, 0, 255)
PATH = (88, 57, 39)
FPS = 60

FONT = pygame.font.SysFont('bahnschrift', 25)
matrix = []
for i in range(LEN):
    sub_lista = []
    for j in range(LEN):
        sub_lista.append(BACKGROUND_COLOR)
    matrix.append(sub_lista)

def draw2(matriz):
    WINDOW.fill(BACKGROUND_COLOR)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(matriz[i][j] != BACKGROUND_COLOR):
                square = pygame.Rect(i*SQUARE, j*SQUARE, SQUARE, SQUARE)
                pygame.draw.rect(WINDOW, matriz[i][j], square)
    pygame.display.update()

def maze_generation():
    pass

def treumaux():
    pass

def dead_end_filling():
    pass

def maze_routing():
    pass

def breadth_first():
    pass#probably the best to start

def mod_depth_first():
    pass#probably the best to start


def A_star():
    pass

draw_type = WALL
x,y = -1,-1
clock = pygame.time.Clock()
click = 0
points = {START:[[0, 0]], END:[[49, 49]], PASSTHROUGH:[]}
WINDOW.fill(BACKGROUND_COLOR)
pygame.display.update()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():                    
        if event.type== pygame.QUIT:
            print('EXIT SUCCESSFUL')
            pygame.quit()
            sys.exit()
        if (event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_w):
                draw_type = WALL
            if(event.key == pygame.K_s):
                draw_type = START
            if(event.key == pygame.K_e):
                draw_type = END
            if(event.key == pygame.K_p):
                draw_type = PASSTHROUGH
            if(event.key == pygame.K_d):
                draw_type = BACKGROUND_COLOR

    if(pygame.mouse.get_pressed()[0] and draw_type == WALL):#maybe implement multiple starts and finishes as well
        x,y = pygame.mouse.get_pos()
        matrix[x//SQUARE][y//SQUARE] = WALL
        draw2(matrix)
    if(pygame.mouse.get_pressed()[0] and draw_type == START):
        matrix[points[START][0][0]][points[START][0][1]] = BACKGROUND_COLOR
        x,y = pygame.mouse.get_pos()
        points[START] = [[x//SQUARE, y//SQUARE]]
        matrix[points[START][0][0]][points[START][0][1]] = START
        draw2(matrix)
    if(pygame.mouse.get_pressed()[0] and draw_type == END):
        matrix[points[END][0][0]][points[END][0][1]] = BACKGROUND_COLOR
        x,y = pygame.mouse.get_pos()
        points[END] = [[x//SQUARE, y//SQUARE]]
        matrix[points[END][0][0]][points[END][0][1]] = END
        draw2(matrix)
    if(pygame.mouse.get_pressed()[0] and draw_type == PASSTHROUGH):
        x,y = pygame.mouse.get_pos()
        if([x//SQUARE, y//SQUARE] not in points[PASSTHROUGH]):
            points[PASSTHROUGH].append([x//SQUARE, y//SQUARE])
            matrix[points[PASSTHROUGH][-1][0]][points[PASSTHROUGH][-1][1]] = PASSTHROUGH
            draw2(matrix)
        print(points)
    if(pygame.mouse.get_pressed()[0] and draw_type == BACKGROUND_COLOR):
        print(points)
        x,y = pygame.mouse.get_pos()
        if(matrix[x//SQUARE][y//SQUARE] in points.keys()):#need to add this to all cases in case someone puts a start and end in same block example
            points[matrix[x//SQUARE][y//SQUARE]].remove([x//SQUARE, y//SQUARE]) 
        matrix[x//SQUARE][y//SQUARE] = BACKGROUND_COLOR
        draw2(matrix)

