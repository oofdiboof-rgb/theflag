import pygame
import consts
import game_field
import screenfile
import soldier
from consts import XRAY_COLOR, MATRICS_Y, MATRICS_X, MINE
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
            # if החייל נוגע במוקש - אז להתפוצץ- נפסל
            # אם החייל פוגע בדגל- אז ניצחון

main()
