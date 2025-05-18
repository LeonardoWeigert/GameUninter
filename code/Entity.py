#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


import pygame.image

from code.Const import ENTITY_LIFE, DAMAGE_GENERAL, SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.vida = ENTITY_LIFE[self.name]
        self.general_damage = DAMAGE_GENERAL[self.name]
        self.getscore = SCORE[self.name]
        self.last_damage_taken = 'None'


    @abstractmethod
    def move(self, ):
        pass


