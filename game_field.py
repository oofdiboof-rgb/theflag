import pygame
import screen
import consts


def ENTER():
    # פה זה צריך ללכת למסך השנילמשך כמה שניות
    screen.screen.fill(consts.XRAY_COLOR)
    for row in range(25):
        for column in range(50):
            pygame.draw.rect(screen, consts.NORMAL_COLOR,
                             [20 * column + 1,
                              20 * row + 1,
                              20,
                              20], 1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
def DOWN():
    pass

def UP():
    pass

def LEFT():
    pass

def RIGHT():
    pass

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
# screen.create_screen()
ENTER()