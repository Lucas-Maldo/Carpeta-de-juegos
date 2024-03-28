import pygame
import sys
import random

SIZE = (500, 1011)
SQUARE = 50
FPS = 60
BOARD_SIZE = 10

pygame.init()
WINDOW = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Battleship')
BACKGROUND_COLOR = (8, 10, 116)
BLACK = (0,0,0)
HIT = (150, 0, 0)
MISS = (38, 41, 160)
SHIP = (100, 100, 100)
SUNKEN = (81,71,69)

FPS = 60
#define a first part and a second part:
#first part can put boats and change the lower graph, second part can shoot and can change upper graph
# second for ships, should probably create a class and a lists of objects of this class for the ships of each player
#for shipp coordinates should probably implement a +1,-1 for each coord
#the coordinates should be in a list o matrix and check if coordinates from the bottom and right dont go oustside the border
#and add a sunknen counter which when 00 means boat sunk
#add a sign for when the boat is sunk and hit and maybe change the coolor for sunken ship
# maybe add a side window that shows the pieces in a vertical list and people can click on them and place them
# the peices placed will be placed doawn and to the right

player1_b = []
player1_enemy_b = []

player1_b = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0],
             [1,1,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]]
player1_enemy_b = [[0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0]]

player2_b = [[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0],
             [1,1,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]]
player2_enemy_b = [[0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0]]

class Ship():
    def __init__(self, shape):
        self.size = 0
        self.shape = shape
        self.height = len(shape)
        self.width = len(shape[0])
        for i in shape:
            self.size += sum(i)

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))
        self.height = len(self.shape)
        self.width = len(self.shape[0])

def grid():
    for i in range(BOARD_SIZE):#vertical
        divider1 = pygame.Rect(i * SQUARE, 0, 1, 1010)
        pygame.draw.rect(WINDOW, BLACK, divider1)
    for i in range(BOARD_SIZE):#horizontal
        divider1 = pygame.Rect(0, i * SQUARE, 500, 1)
        pygame.draw.rect(WINDOW, BLACK, divider1)
        divider2 = pygame.Rect(0, i * SQUARE + 511, 500, 1)
        pygame.draw.rect(WINDOW, BLACK, divider2)
    divider_mid = pygame.Rect(0, 501, 500, 10)#middle
    pygame.draw.rect(WINDOW, BLACK, divider_mid)

def draw(lista1, lista2):
    WINDOW.fill(BACKGROUND_COLOR)
    grid()
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if(lista1[i][j] == "X"):
                ship = pygame.Rect(j * SQUARE + 1, i * SQUARE + 1, SQUARE, SQUARE)
                pygame.draw.rect(WINDOW, HIT, ship)
            if(lista1[i][j] == "M"):
                ship = pygame.Rect(j * SQUARE + 1, i * SQUARE + 1, SQUARE, SQUARE)
                pygame.draw.rect(WINDOW, MISS, ship)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if(lista2[i][j] > 0):
                ship = pygame.Rect(j * SQUARE + 1, i * SQUARE + 511, SQUARE, SQUARE)
                pygame.draw.rect(WINDOW, SHIP, ship)
    pygame.display.update()

clock = pygame.time.Clock()
WINDOW.fill(BACKGROUND_COLOR)
divider = pygame.Rect(0, 501 , 510, 10)
pygame.draw.rect(WINDOW, BLACK, divider)
pygame.display.update()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():                    
        if event.type == pygame.QUIT:
            print('EXIT SUCCESSFUL')
            pygame.quit()
            sys.exit()
        if(event.type == pygame.MOUSEBUTTONDOWN):
                x,y = pygame.mouse.get_pos()
                print(y)
                if(y < 501):
                    column = int(x//SQUARE)
                    row = int(y//SQUARE)
                    if(player2_b[row][column] > 0 and player1_enemy_b[row][column] == 0):
                        player1_enemy_b[row][column] = "X"
                    if(player2_b[row][column] == 0 and player1_enemy_b[row][column] == 0):
                        player1_enemy_b[row][column] = "M"
                if(y > 511):
                    column = int(x//SQUARE)
                    row = int((y-521)//SQUARE)
                    print(row, column)
                
                
    draw(player1_enemy_b, player1_b)
