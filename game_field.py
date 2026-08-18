import screenfile
import consts
import random


def create_matrix():
    list = []
    for row in range(consts.MATRICS_Y):
        for col in range(consts.MATRICS_X):
            list.append(0)
        consts.MATRIX.append(list)
        list = []
    for i in range(4):
        for j in range(4):
            consts.MATRIX[i + 21][j + 46] = "DEGEL"
    for i in range(4):
        for j in range(2):
            consts.MATRIX[i][j] = "SOLDIER"


def mines_list(screen):
    create_matrix()
    mine_places = []
    for mines in range(20):
        BOOL = True
        while BOOL:
            row = random.choice(range(consts.MATRICS_Y))
            spot = random.choice(range(len(consts.MATRIX[row]) - 2))
            if (consts.MATRIX[row][spot] or consts.MATRIX[row][spot + 1] or consts.MATRIX[row][spot + 2]) == 0:
                BOOL = False
        consts.MATRIX[row][spot] = "MINE"
        consts.MATRIX[row][spot + 1] = "MINE"
        consts.MATRIX[row][spot + 2] = "MINE"
        mine_places.append([row, spot])
        BOOL = True
    return mine_places


mine_spots = mines_list(screenfile.screen)


def spawn_mines(screen):
    for i in mine_spots:
        screen.blit(consts.MINE, ((consts.GRID_POS_X * i[1], consts.GRID_POS_Y * i[0])))
