import pygame

import game_field
import screen

def main():
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
        # אם החייל פוגע בדגל- אז ניצח
        # לשנות את המסך לפי התזוזה של החייל
