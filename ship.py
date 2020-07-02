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

        # 移动标识
        self.move_right = False

    def update(self):
        """根据移动标识调整飞船的位置"""
        if self.move_right:
            self.rect.centerx += 1

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)