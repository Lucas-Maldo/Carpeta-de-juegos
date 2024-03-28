import pygame
import sys
import random

SIZE = 800
FPS = 60

pygame.init()
WINDOW = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Snake')
WHITE = (0, 0, 0)
FRUIT_COLOR = (255, 255, 255)
SNAKE_COLOR = (0, 0, 255)
SNAKE_SIZE = 20
DIFFICULTY = 20 #Higher is harder
FPS = 10

FONT = pygame.font.SysFont('arial', 25)
FONT = pygame.font.SysFont('bahnschrift', 25)
BOARD = pygame.image.load('C:\Lucas things\Projects\Games\Carpeta-de-juegos\snake\snake_board.png')

def animation(snake_coords, fruit_coords):
    WINDOW.blit(BOARD, (0, 0))
    for i in snake_coords:
        segment = pygame.Rect(i[0], i[1], SNAKE_SIZE, SNAKE_SIZE)
        pygame.draw.rect(WINDOW, SNAKE_COLOR, segment)

    fruit = pygame.Rect(fruit_coords[0], fruit_coords[1], SNAKE_SIZE, SNAKE_SIZE)
    pygame.draw.rect(WINDOW, FRUIT_COLOR, fruit)

    points = FONT.render("Points: " + str(len(snake_coords)-1), 1, WHITE)
    WINDOW.blit(points, (10, 10))
    pygame.display.update()

def movement(snake_coords, coords):
    snake_coords.append([snake_coords[-1][0] + coords[0], snake_coords[-1][1] + coords[1]])
    del snake_coords[0]
    return snake_coords

def generate_fruit():
    while True:
        fruit_x = random.randint(0, 39) * 20
        fruit_y = random.randint(0, 39) * 20
        if([fruit_y, fruit_x] in snake_coords):
            continue
        return (fruit_y, fruit_x)
    
def check_collision(snake_coords):
    if(snake_coords[-1] in snake_coords[0:-1]):
        return True
    if(snake_coords[-1][0] > 780 or snake_coords[-1][0] < 0):
        return True
    if(snake_coords[-1][1] > 780 or snake_coords[-1][1] < 0):
        return True

clock = pygame.time.Clock()
snake_size = 1
snake_coords = [[400, 700]]
x_coord, y_coord = 0,0
fruit = generate_fruit()
print(fruit)
while True:
    clock.tick(FPS)
    animation(snake_coords, (fruit[0], fruit[1]))
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            print('EXIT SUCCESSFUL')
            pygame.quit()
            sys.exit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT and x_coord != DIFFICULTY):
                x_coord = -DIFFICULTY
                y_coord = 0
            if(event.key == pygame.K_RIGHT and x_coord != -DIFFICULTY):
                x_coord = DIFFICULTY
                y_coord = 0
            if(event.key == pygame.K_UP and y_coord != DIFFICULTY):
                x_coord = 0
                y_coord = -DIFFICULTY
            if(event.key == pygame.K_DOWN and y_coord != -DIFFICULTY):
                x_coord = 0
                y_coord = DIFFICULTY
    if(tuple(snake_coords[-1]) == fruit):
        snake_coords.append([snake_coords[-1][0] + x_coord, snake_coords[-1][1] + y_coord])
        fruit = generate_fruit()
    collision = check_collision(snake_coords)
    if(collision):
        print("collision")
        mesg = FONT.render("You Lost! Press Q to Quit", True, (255, 0, 0))
        WINDOW.blit(mesg, [SIZE / 3, SIZE / 3])
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    print('EXIT SUCCESSFUL')
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print('EXIT SUCCESSFUL')
                        pygame.quit()
                        sys.exit()
            
    snake_coords = movement(snake_coords, (x_coord, y_coord))