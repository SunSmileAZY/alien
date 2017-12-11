import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    #初始化游戏并创建一个游戏对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_hight))
    pygame.display.set_caption("Alien invasion")
    #创建飞船
    ship = Ship(ai_settings,screen)

    #开始游戏主循环
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings,screen,ship)
        ship.update()

run_game();