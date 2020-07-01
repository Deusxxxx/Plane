import sys
import pygame
import random

# 全局定义
SCREEN_X = 800
SCREEN_Y = 800

# 创建飞机类，需要包含以下几个属性
# 飞机实体本身
# 控制飞机方向
# 发射子弹
class Plane(object):
    """docstring for plane"""
# 初始化各种属性
    def __init__(self):
        # 不知道需要定义啥，稍后再添加
        self.body = [] # 创建飞机本体
        self.createplane()


    # 只能左右移动
    # def move(self, curkey):
    #     if curkey == pygame.K_LEFT:
    #         # 往左边移动
    #     if curkey == pygame.K_RIGHT:
            # 往右边移动
    

    # 在画面的底部中间生成一个50*50的方块，作为飞机本体
    def addplane(self):
        left, top = (475,50)
        node = pygame.Rect(left, top, 50, 50)
        if self.
        self.body.insert(0, node)



    # 控制飞机块的移动，只能左右移动，不能上下移动
    def movenode(self, curkey):
        left, top = (self.body[0].left, self.body[0].top)
        if curkey == pygame.K_LEFT:
            left -= 25
            print(left)
            node = pygame.Rect(left, top, 50, 50)
        elif curkey == pygame.K_RIGHT:
            print(left)
            left += 25
            node = pygame.Rect(left, top, 50, 50)



def main():
    pygame.init()
    screen_size = (SCREEN_X, SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Plane')
    clock = pygame.time.Clock()

    # 飞机 ，敌人
    plane = Plane()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                plane.movenode(event.key)



        screen.fill((255,255,255))


        # 画飞机
        # node = plane.node
        for node in plane.body:

            pygame.draw.rect(screen,(255,220,39),node,0)

        pygame.display.update()
        clock.tick(10)



if __name__ == '__main__':
    main()





