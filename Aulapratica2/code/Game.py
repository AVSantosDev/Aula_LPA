#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame as pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGTH


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH , WIN_HEIGTH))

        while True:
            menu = Menu(self.window)
            menu.run()


    def manu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lacida Sans Typewriter")
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)






