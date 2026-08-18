import pygame
import consts
import game_field
import screenfile
import soldier
from consts import XRAY_COLOR, MATRICS_Y, MATRICS_X, MINE, XY_SOLDIER, GRID_POS_X
import sys

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
                        soldier.up()
                    elif event.key == pygame.K_DOWN:
                        soldier.down()
                    elif event.key == pygame.K_LEFT:
                        soldier.left()
                    elif event.key == pygame.K_RIGHT:
                        soldier.right()
                    elif event.key == pygame.K_RETURN:
                        soldier.enter()
                        bool = False
            if consts.MATRIX[(XY_SOLDIER[1] + (consts.GRID_POS_Y*3))//consts.GRID_POS_Y][((XY_SOLDIER[0])//consts.GRID_POS_X)]=="MINE" or consts.MATRIX[(XY_SOLDIER[1] + (consts.GRID_POS_Y*3))//consts.GRID_POS_Y][((XY_SOLDIER[0]+GRID_POS_X)//consts.GRID_POS_X)]=="MINE":
                screenfile.lose(((XY_SOLDIER[0])//consts.GRID_POS_X), (XY_SOLDIER[1] + (consts.GRID_POS_Y*3))//consts.GRID_POS_Y)
                print((((XY_SOLDIER[0])/consts.GRID_POS_X), (XY_SOLDIER[1] + (consts.GRID_POS_Y*3))/consts.GRID_POS_Y), (((XY_SOLDIER[0])//consts.GRID_POS_X), (XY_SOLDIER[1] + (consts.GRID_POS_Y*3))//consts.GRID_POS_Y))
            # if החייל נוגע במוקש - אז להתפוצץ- נפסל
            # אם החייל פוגע בדגל- אז ניצחון

main()
