import pygame
import consts
import game_field
import screenfile
import soldier
from consts import XRAY_COLOR, MATRICS_Y, MATRICS_X, MINE
import sys
import time

def main():
    while True:
        screenfile.screen_create()
        bool = True
        while bool:
            # create_matrix()
            screenfile.create_soldier()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        up()
                    elif event.key == pygame.K_DOWN:
                        down()
                    elif event.key == pygame.K_LEFT:
                        left()
                    elif event.key == pygame.K_RIGHT:
                        right()
                    elif event.key == pygame.K_RETURN:
                        enter()
                        bool = False


            # if החייל נוגע במוקש - אז להתפוצץ- נפסל
            # אם החייל פוגע בדגל- אז ניצחון
def enter():
    screen = pygame.display.set_mode((consts.SCREEN_X, consts.SCREEN_Y))
    screen.fill(XRAY_COLOR)


    for row in range(MATRICS_Y):
        for column in range(MATRICS_X):
            pygame.draw.rect(screen, (9, 99, 0),[20 * column + 1,20 * row + 1,20,20], 1)
    mine_spots = game_field.mine_spots
    for i in mine_spots:
        screen.blit(consts.MINE, ((consts.GRID_POS_X * i[1], consts.GRID_POS_Y * i[0])))
    screenfile.create_night_soldier()
    pygame.display.flip()
    running = True
    while running:
        time.sleep(1)
        running = False
    return False


def down():
    if consts.XY_SOLDIER[1] + consts.GRID_POS_Y <= consts.SCREEN_Y-consts.SCREEN_Y /MATRICS_Y * 4:
        consts.XY_SOLDIER[1]+=consts.GRID_POS_Y
    screenfile.screen_create()


def up():
    if 0<=consts.XY_SOLDIER[1]-consts.GRID_POS_Y:
        consts.XY_SOLDIER[1]-=consts.GRID_POS_Y
    screenfile.screen_create()


def left():
    if 0 <= consts.XY_SOLDIER[0] - consts.GRID_POS_X :
        consts.XY_SOLDIER[0] -=consts.GRID_POS_X
    screenfile.screen_create()


def right():
    if consts.XY_SOLDIER[0] + consts.GRID_POS_X<=consts.SCREEN_X-consts.SCREEN_X /MATRICS_X * 2:
        consts.XY_SOLDIER[0] +=consts.GRID_POS_X
    screenfile.screen_create()
main()
