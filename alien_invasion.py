
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化 pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 设置背景颜色
    bg_color = (230, 230, 230)

    # 创建飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏主循环
    while True:
        
        # 监视键盘与鼠标事件
        gf.check_events(aisettings,screen, ship, bullets)
        ship.update()
        bullets.update()
        # 每次循环时，都填充一次屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()