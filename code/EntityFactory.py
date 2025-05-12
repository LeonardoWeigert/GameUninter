#!/usr/bin/python
#-*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, RANDOM_ENEMY_SPAWN_MAX, RANDOM_ENEMY_SPAWN_MIN
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1BG':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f'level1BG{i}', (0, 0)))
                    list_bg.append(Background(f'level1BG{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'player1-11':
                return Player('player1-11',(10,330))
            case 'Enemy1-2':
                return Enemy('Enemy1-2', (WIN_WIDTH + 5, random.randint(RANDOM_ENEMY_SPAWN_MAX,RANDOM_ENEMY_SPAWN_MIN) ))