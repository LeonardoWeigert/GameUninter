#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

from code.Const import SPEED_ENTITY
from code.Entity import Entity


class Enemy(Entity, ABC):
    def __init__(self, name: str, position: tuple) -> None:
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= SPEED_ENTITY[self.name]