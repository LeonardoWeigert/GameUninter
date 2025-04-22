#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT



class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


            # Check for all events
            #for event in pg.event.get():
                #if event.type == pg.QUIT:
                 #   pg.quit()  # Close Windows
                  #  quit()