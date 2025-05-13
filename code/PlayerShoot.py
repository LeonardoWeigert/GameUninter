#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.Const import SPEED_ENTITY
from code.Entity import Entity


class PlayerShoot(Entity):

    def __int__(self, name: str, position: tuple):
        super().__int__(name,position)



    def move(self, ):
        self.rect.centerx += SPEED_ENTITY[self.name]