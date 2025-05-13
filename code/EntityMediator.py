#!/usr/bin/python
#-*- coding: utf-8 -*-

from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.PlayerShoot import PlayerShoot


class EntityMediator:

    @staticmethod
    def verify_col_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.vida = 0
        if isinstance(ent, PlayerShoot):
            if ent.rect.left >= WIN_WIDTH:
                ent.vida = 0

    @staticmethod
    def verify_collision(e_list: list[Entity]):
        for i in range(len(e_list)):
            e_collision = e_list[i]
            EntityMediator.verify_col_window(e_collision)

    @staticmethod
    def verify_life_entity(e_list: list[Entity]):
        for ent in e_list:
            if ent.vida <= 0:
                e_list.remove(ent)