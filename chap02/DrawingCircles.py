# Drawing Circles
# Python 3.2
import sys

import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Circles")
# 主循环
while True:
    # 处理所有的事件
    for event in pygame.event.get():
        # 如果事件类型是退出或按键按下，则退出程序
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    # 用蓝色填充屏幕背景
    screen.fill((0, 0, 200))

    # 画一个圆
    color = 255, 255, 0  # 圆的颜色：黄色
    position = 300, 250  # 圆的中心位置
    radius = 100  # 圆的半径
    width = 10  # 圆的线宽
    pygame.draw.circle(screen, color, position, radius, width)

    # 更新屏幕显示
    pygame.display.update()

