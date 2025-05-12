#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import SPEED_ENTITY, LENGTH_PLAYER_BOX_MAX_Y, WIN_HEIGHT, WIN_WIDTH, LENGTH_PLAYER_BOX_MAX_X
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple) -> None:
        super().__init__(name, position)

    def update(self, ):
        pass

    def move(self, ):
        pressed_k = pygame.key.get_pressed()
        # Move Up
        if pressed_k[pygame.K_UP] and self.rect.top > LENGTH_PLAYER_BOX_MAX_Y or pressed_k[pygame.K_w] and self.rect.top > LENGTH_PLAYER_BOX_MAX_Y :
            self.rect.centery -= SPEED_ENTITY[self.name]

        # Move Down
        if pressed_k[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT or pressed_k[pygame.K_s] and self.rect.bottom < WIN_HEIGHT :
            self.rect.centery += SPEED_ENTITY[self.name]

        # Move Left
        if pressed_k[pygame.K_LEFT] and self.rect.left > 0 or pressed_k[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= SPEED_ENTITY[self.name]

        # Move Right
        if pressed_k[pygame.K_RIGHT] and self.rect.right < LENGTH_PLAYER_BOX_MAX_X or pressed_k[pygame.K_d] and self.rect.right < LENGTH_PLAYER_BOX_MAX_X:
            self.rect.centerx += SPEED_ENTITY[self.name]
        pass