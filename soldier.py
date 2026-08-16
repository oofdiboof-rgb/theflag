import screenfile
import pygame
import random
import consts
from consts import START_SOLDIER, FLAG_START, NORMAL_COLOR, XRAY_COLOR
def create_soldier():
    screen= screenfile.screen_create()
    screen.blit(consts.SOLDIER, START_SOLDIER)