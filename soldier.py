# from screenfile import screen
import pygame
import random
import consts
from consts import  FLAG_START, NORMAL_COLOR, XRAY_COLOR, SOLDIER
def create_soldier(screen):
    screen.blit(consts.SOLDIER, (consts.X_SOLDIER, consts.Y_SOLDIER))