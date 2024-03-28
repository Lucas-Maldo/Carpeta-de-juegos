'''
class enemy
type shooter or melee or player
random.randint shoot
projectle: image

add sound? pygame.mixier.init?

'''
import pygame
import random
import sys

SIZE = 800
FPS = 60

pygame.init()
WINDOW = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Space Invaders')
BACKGROUND_COLOR = (0,0,0)
WHITE = (255, 255, 255)
BULLET_COLOR_E = (255, 0, 0)
BULLET_COLOR_P = (0, 255, 0)
DIFFICULTY = 250 #Lower is harder
ENEMY_LIVES = 1

FONT = pygame.font.SysFont('arial', 20)

spaceship = pygame.image.load('C:/Lucas things/Projects/Games/Carpeta-de-juegos/space_invaders/spaceship_red.png')
spaceship = pygame.transform.scale(spaceship, (50,43))
spaceship = pygame.transform.rotate(spaceship, 180)
enemy1 = pygame.image.load('C:/Lucas things/Projects/Games/Carpeta-de-juegos/space_invaders/red.png')
enemy2 = pygame.image.load('C:/Lucas things/Projects/Games/Carpeta-de-juegos/space_invaders/green.png')

def animation(entities):
    WINDOW.fill(BACKGROUND_COLOR)
    health = FONT.render("Health: " + str(entities[0].lives), 1, WHITE)
    points = FONT.render("Points: " + str(entities[0].points), 1, WHITE)
    WINDOW.blit(health, (10, 10))
    WINDOW.blit(entities[0].image, entities[0].coords)
    WINDOW.blit(points, (SIZE - points.get_width() - 10, 10))
    for i in entities[1]:
        i.move()
        WINDOW.blit(i.image, i.coords)
    for i in entities[2]:
        i.move()
        if(i.entity == "enemy"):
            pygame.draw.rect(WINDOW, BULLET_COLOR_E, i.image)
        if(i.entity == "player"):
            pygame.draw.rect(WINDOW, BULLET_COLOR_P, i.image)
    pygame.display.update()

def collision(entity, projectile):
    if(entity.coords[1] < projectile.coords[1] and entity.coords[1] + entity.size[1] > projectile.coords[1] and
       entity.coords[0] < projectile.coords[0] and entity.coords[0] + entity.size[0] > projectile.coords[0]):
        print("collision")
        return True, entity.points
    if(entity.coords[0] < projectile.coords[0] and  entity.coords[0] + entity.size[0] > projectile.coords[0] + 17 and
       entity.coords[1] < projectile.coords[1] and entity.coords[1] + entity.size[1] > projectile.coords[1] + 17):
        print("collision")
        return True, entity.points
    return False, 0

class Projectile():
    def __init__(self, entity, coords):
        self.entity = entity
        self.speed = 5
        if(self.entity == "player"):
            self.speed = -5
        self.coords = coords
        self.image = pygame.Rect(self.coords[0], self.coords[1], 2, 17)
    
    def move(self):
        self.coords[1] += self.speed
        self.image = pygame.Rect(self.coords[0], self.coords[1], 2, 17)

class Entity:
    def __init__(self, image, type, coords, size, lives, points):
        self.image = image
        self.type = type
        self.coords = coords
        self.size = size
        self.lives = lives
        self.speed = 1
        self.lower_distance = 40
        self.points = points

    def move(self):
        if(self.type[0:-1] == "enemy"):
            self.coords[0] += self.speed
            if(self.coords[0] >= 740):
                self.speed = -self.speed
                self.coords[0] = 740
                self.coords[1] += self.lower_distance
            if(self.coords[0] <= 20):
                self.speed = -self.speed
                self.coords[0] = 20
                self.coords[1] += self.lower_distance
    
    def shoot(self):
        shoot = random.randint(0, DIFFICULTY)
        if(self.type == "enemy1" and shoot == DIFFICULTY):
            return Projectile("enemy", [self.coords[0] + 20, self.coords[1] + 20])


def start():
    entities = []
    bullets = []
    entities.append(Entity(spaceship, "player", [400, 675], (50,43), 3, 0))
    enemys = []
    for i in range(1,8):
        for j in range(1,5):
            if(j == 1):
                enemys.append(Entity(enemy1, "enemy1", [i * 80 ,j * 88 ], (40, 32), ENEMY_LIVES + 1, 30))
            else:
                enemys.append(Entity(enemy2, "enemy2", [i * 80 ,j * 88 ], (40, 32), ENEMY_LIVES, 10))
    entities.append(enemys)
    entities.append(bullets)
    return entities
    
clock = pygame.time.Clock()
entities = start()
prev_time = pygame.time.get_ticks()

while True:
    clock.tick(FPS)
    player = entities[0]
    enemys = entities[1]
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            print('EXIT SUCCESSFUL')
            pygame.quit()
            sys.exit()

    for i in enemys:
        bullet = i.shoot()
        if(bullet):
            entities[2].append(bullet)
    if(pygame.key.get_pressed()[pygame.K_a]):
            player.coords[0] -= 3
    if(pygame.key.get_pressed()[pygame.K_d]):
            player.coords[0] += 3
    curr_time = pygame.time.get_ticks()
    if(pygame.key.get_pressed()[pygame.K_SPACE] and curr_time - prev_time > 500):
        prev_time = curr_time
        entities[2].append(Projectile("player", [player.coords[0] + 25, player.coords[1] + 5]))
    if(player.coords[0] >= 730):
        player.coords[0] = 730
    if(player.coords[0] <= 20):
        player.coords[0] = 20

    for i in entities[2]:
        for j in entities[1]:
            if(i.entity == "player"):
                collide, point = collision(j,i)
                if(collide):
                    j.lives -= 1
                    points = j.points
                    entities[2].remove(i)
                    if(j.lives == 0):
                        player.points += point
                        entities[1].remove(j)

    for i in entities[2]:
        if(i.entity == "enemy"):
            collide, point = collision(entities[0], i)
            if(collide):
                lives = entities[0].lives - 1
                points = entities[0].points
                entities[0] = Entity(spaceship, "player", [400, 675], (50,43), lives, points)
                entities[2] = []
                
    if(player.lives == 0):
        print("Player has died")
        break
    if(len(entities[1]) == 0):
        print("Player has won, points: " + str(player.points))
        break

    animation(entities)
                    