# Drawing Arcs
# Python 3.2

import math
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Arcs")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill((0,0,200))

    #draw the arc
    color = 255,0,255
    # 画一个圆弧
    position = (200, 150, 200, 200)  # 定义圆弧所在的矩形区域 (left, top, width, height)
    start_angle = math.radians(0)  # 起始角度，以弧度表示，0 表示从 3 点钟方向开始
    end_angle = math.radians(180)  # 结束角度，以弧度表示，180 度即半圆
    width = 8  # 圆弧的线宽

    # 使用 pygame.draw.arc() 绘制圆弧
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

    # 更新屏幕显示
    pygame.display.update()

