import pygame

GRASS_IMG=pygame.image.load('grass.png')
GRASS_SIZE=(90,90)
GRASS=pygame.transform.scale(GRASS_IMG,GRASS_SIZE)

MINE_IMG=pygame.image.load('mine.png')
MINE_SIZE=(90,30)
MINE=pygame.transform.scale(MINE_IMG,MINE_SIZE)

FLAG_IMG=pygame.image.load('flag.png')
FLAG_SIZE=(90,120)
FLAG=pygame.transform.scale(FLAG_IMG,FLAG_SIZE)
FLAG_START=(1410, 630)

EXPLOTION=pygame.image.load('explotion.png')
INJURY=pygame.image.load('injury.png')
INJURY_SIZE=(120,60)

SOLDIER=pygame.image.load('soldier.png')
SOLDIER_SIZE=(120,60)
START_SOLDIER=(0, 0)

SCREEN_X=1500
SCREEN_Y=750
SCREEN_COLOR=(9,99,0)
