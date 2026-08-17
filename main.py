import pygame
import consts
import screenfile
import soldier
from consts import XRAY_COLOR, MATRICS_Y, MATRICS_X
import sys
MATRIX=[]

def main():
    screenfile.screen_create()
    while True:
        # create_matrix()
        # soldier.create_soldier()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print("Keydown")
                if event.key == pygame.K_UP:
                    print("UP key")
                    up()
                elif event.key == pygame.K_DOWN:
                    print("DOWN key")
                    down()
                elif event.key == pygame.K_LEFT:
                    print("LEFT key")
                    left()
                elif event.key == pygame.K_RIGHT:
                    print("RIGHT key")
                    right()
                elif event.key == pygame.K_RETURN:
                    enter()

            # if החייל נוגע במוקש - אז להתפוצץ- נפסל
            # אם החייל פוגע בדגל- אז ניצחון
def enter():
    screen = pygame.display.set_mode((consts.SCREEN_X, consts.SCREEN_Y))
    screen.fill(XRAY_COLOR)
    for row in range(MATRICS_Y):
        for column in range(MATRICS_X):
            pygame.draw.rect(screen, (9, 99, 0),[20 * column + 1,20 * row + 1,20,20], 1)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    return


def down():
    X_SOLDIER=(SCREEN_X / MATRICS_X * 2)-1
    print(s)
    pass


def up():
    pass

def left():
    pass

def right():
    pass
def create_matrix():
        for row in range(consts.MATRICS_Y):
            MATRIX.append([])
            for col in range(consts.MATRICS_X):
                MATRIX[row].append('0')
main()

