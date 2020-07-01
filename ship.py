import pygame

class Ship():
    def __init__(self, screen):
        """初始化飞船，并初始化位置"""
        self.screen = screen

        # 加载飞船图片，并获取其外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕的中央底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)