import pygame
import consts
import game_field
import screenfile
import soldier
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
                elif event.key == pygame.K_DOWN:
                    print("DOWN key")
                elif event.key == pygame.K_LEFT:
                    print("LEFT key")
                elif event.key == pygame.K_RIGHT:
                    print("RIGHT key")
                elif event.key == pygame.K_RETURN:
                    print("ENTER key")

            # if החייל נוגע במוקש - אז להתפוצץ- נפסל
            # אם החייל פוגע בדגל- אז ניצחון

def create_matrix():
        for row in range(consts.MATRICS_Y):
            MATRIX.append([])
            for col in range(consts.MATRICS_X):
                MATRIX[row].append('0')
main()