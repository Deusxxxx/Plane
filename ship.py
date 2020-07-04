import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船，并初始化位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图片，并获取其外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕的中央底部(初始化的)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性 centerx 中存储小数属性
        self.center = float(self.rect.centerx)

        # 移动标识
        self.move_right = False
        self.move_left = False

    def update(self):
        """根据移动标识调整飞船的位置"""
        # 更新飞船的 center 值，而不是 rect
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.move_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据 self.center 更新 rect 对象
        self.rect.centerx = self.center

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)