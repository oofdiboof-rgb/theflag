import pygame

SCREEN_X = 1000
SCREEN_Y = 500
NORMAL_COLOR = (9, 99, 0)
XRAY_COLOR = (21, 21, 21)
MATRIX=[]
MATRICS_X = 50
MATRICS_Y = 25
X_SOLDIER= int(0)
Y_SOLDIER= int(0)
GRID_POS_X = SCREEN_X // MATRICS_X
GRID_POS_Y = SCREEN_Y // MATRICS_Y
GRASS_IMG = pygame.image.load('grass.png')
GRASS_SIZE = (SCREEN_X / MATRICS_X * 3, SCREEN_Y / MATRICS_Y * 3)
GRASS = pygame.transform.scale(GRASS_IMG, GRASS_SIZE)

MINE_IMG = pygame.image.load('mine.png')
MINE_SIZE = (SCREEN_X / MATRICS_X * 3, SCREEN_Y / MATRICS_Y)
MINE = pygame.transform.scale(MINE_IMG, MINE_SIZE)

FLAG_IMG = pygame.image.load('flag.png')
FLAG_SIZE = (SCREEN_X / MATRICS_X * 4, SCREEN_Y / MATRICS_Y * 3)
FLAG = pygame.transform.scale(FLAG_IMG, FLAG_SIZE)
FLAG_START = (SCREEN_X - FLAG_SIZE[0], SCREEN_Y - FLAG_SIZE[1])

EXPLOSION = pygame.image.load('explotion.png')
INJURY = pygame.image.load('injury.png')
INJURY_SIZE =  (SCREEN_X / MATRICS_X * 2, SCREEN_Y / MATRICS_Y * 4)

SOLDIER_IMG = pygame.image.load('soldier.png')
SOLDIER_SIZE = (SCREEN_X / MATRICS_X * 2, SCREEN_Y / MATRICS_Y * 4)
SOLDIER = pygame.transform.scale(SOLDIER_IMG, SOLDIER_SIZE)
