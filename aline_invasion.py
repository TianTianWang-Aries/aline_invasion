# -*- coding: utf-8 -*-
import sys
import pygame


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # screen_width = 600
    # screen_height = 800
    # screen = pygame.display.set_mode((screen_width, screen_height))
    screen = pygame.display.set_mode((1200, 800))

    pygame.display.set_caption("Aline Invasion")

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
