import pygame

import game_field
import screenfile

MATRIX=[]
def main():
    create_matrix()
    # להוסיף את פונקציה של המסך הירוק
    while 1>0:
        for event in pygame.event.get():
            if event.type == pygame.K_KP_ENTER:
                game_field.ENTER()
            elif event.type == pygame.KEYDOWN:
                game_field.DOWN()
            elif event.type == pygame.KEYUP:
                game_field.UP()
            elif event.type == pygame.K_LEFT:
                game_field.LEFT()
            elif event.type == pygame.K_RIGHT:
                game_field.RIGHT()
        # if החייל נוגע במוקש - אז להתפוצץ- נפסל
        # אם החייל פוגע בדגל- אז ניצחון

def create_matrix():
        for row in range(25):
            MATRIX.append([])
            for col in range(50):
                MATRIX[row].append('0')
