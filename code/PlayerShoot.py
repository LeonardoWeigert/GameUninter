# code/PlayerShoot.py
#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Const import SPEED_ENTITY
from code.Entity import Entity
from code.Enemy import Enemy

class PlayerShoot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = SPEED_ENTITY[self.name]

    def move(self, enemies: list[Enemy] = None):
        if enemies is None:
            super().move()
            return
        dx = self.speed           # deslocamento total desejado
        steps = max(1, abs(dx) // 5)  # subdivide em passinhos de até 5px
        step_x = dx / steps

        for _ in range(steps):
            self.rect.x += step_x  # avança um micro-passo
            for enemy in enemies:
                if self.rect.colliderect(enemy.rect):  # colisão detectada
                    enemy.vida -= self.general_damage  # aplica dano
                    self.vida = 0                      # flecha some
                    enemy.last_damage_taken = self.name
                    self.last_damage_taken = enemy.name
                    return