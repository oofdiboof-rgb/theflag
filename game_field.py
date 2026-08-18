import pygame
import screenfile
import consts
import random



def create_matrix():
    for row in range(consts.MATRICS_Y):
        consts.MATRIX.append([])
        for col in range(consts.MATRICS_X):
            consts.MATRIX[row].append(0)
    for i in range(3):
        for j in range(4):
            consts.MATRIX[i+22][j+46] = "DEGEL"

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
    # print(mine_places[1][1])
    # for i in consts.MATRIX:
    #     print(i)
mine_spots = mines_list(screenfile.screen)
def spawn_mines(screen):
    for i in mine_spots:
        screen.blit(consts.MINE, ((consts.GRID_POS_X * i[1], consts.GRID_POS_Y * i[0])))


# screen.blit(consts.FLAG, FLAG_START)
# def spawn_mine():
#     for i in range(20):
#         screen.blit(consts.MINE, ((random.choice(range(int(consts.SCREEN_X-consts.MINE_SIZE[0])))), random.choice(range(int(consts.SCREEN_Y-consts.MINE_SIZE[1])))))
# while xray:
#     for event in pygame.event.get():
#         spawn_mine()
#
#         screen.blit(consts.FLAG, FLAG_START)
#         if event.type == pygame.QUIT:
#             screen.fill(XRAY_COLOR)
#             pygame.time.wait(1000)
#             xray = False
#             running = True
#     pygame.display.flip()
#     clock.tick(60)
# screenfile.screen_create()
# banans()
# spawn_mines()
# for i in consts.MATRIX:
#     print(i)

#
# draw_screen-
#
# draw_grid-
#
# if visible:
#     draw_screen --
# else:
#     draw