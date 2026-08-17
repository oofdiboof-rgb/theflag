import pygame
import consts
import game_field
import screenfile
import soldier
MATRIX=[]
def main():
    running = True
    while running:
        create_matrix()
        screenfile.screen_create()
        # soldier.create_soldier()
def aaa():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("esdfg")
                    game_field.banans()
                elif event.type == pygame.K_LEFT:
                    print("hgf")
                    game_field.left()
                elif event.type == pygame.K_RIGHT:
                    print("hgfhg")
                    game_field.right()
            # if החייל נוגע במוקש - אז להתפוצץ- נפסל
            # אם החייל פוגע בדגל- אז ניצחון

def create_matrix():
        for row in range(consts.MATRICS_Y):
            MATRIX.append([])
            for col in range(consts.MATRICS_X):
                MATRIX[row].append('0')

main()
aaa()