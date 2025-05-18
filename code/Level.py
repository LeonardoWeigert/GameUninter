#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Const import SPAWN_ENEMY, SPAWN_ENEMY_TIME, C_WHITE
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.PlayerShoot import PlayerShoot  # identifica quando é flecha
from code.Enemy import Enemy              # identifica inimigos

class Level:
    def __init__(self, window, name, game_mode):
        self.window    = window
        self.name      = name
        self.game_mode = game_mode
        self.timeout_level = 30000
        self.timeout_timer = pygame.time.get_ticks()

        # setup inicial: background + player + enemy's spawn
        self.e_list = []
        self.e_list.extend(EntityFactory.get_entity('level1BG'))
        self.player = EntityFactory.get_entity('player1-11')
        self.e_list.append(self.player)
        pygame.time.set_timer(SPAWN_ENEMY, SPAWN_ENEMY_TIME)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            count_time = pygame.time.get_ticks() - self.timeout_timer
            timer_duration = max(0, self.timeout_level - count_time)
            font = pygame.font.SysFont("04b_03", 14)

            # 1) Eventos (spawn de inimigos e tiro)
            projectiles: list[PlayerShoot] = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); quit()
                if event.type == SPAWN_ENEMY:
                    self.e_list.append(EntityFactory.get_entity('Enemy1-2'))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    tiro = self.player.shoot()
                    if tiro:
                        projectiles.append(tiro)
            # 2) Desenho e movimento
            # CHANGED: só as flechas usam move(enemies), os demais continuam sem alteração
            enemies = [e for e in self.e_list if isinstance(e, Enemy)]
            for ent in self.e_list:
                self.window.blit(ent.surf, ent.rect)
                if isinstance(ent, PlayerShoot):
                    ent.move(enemies)  # flecha com micro-passos
                else:
                    ent.move()         # demais entidades usam move() padrão
#                if ent.name == 'player1-11':
#                    txt2 = f'FPS: {clock.get_fps():.0f}'
                if ent.name == 'player1-11':
                    health = font.render(f'Vida: {self.player.vida}', True, C_WHITE).convert_alpha()
                    score = font.render(f'Score: {self.player.getscore}', True, C_WHITE).convert_alpha()
                    self.window.blit(health, (10, 25))
                    self.window.blit(score, (10, 35))
            # 3) Acrescenta as flechas no fim da lista
            self.e_list.extend(projectiles)


            fps  = font.render(f'FPS: {clock.get_fps():.0f}', True, C_WHITE).convert_alpha()
            timer = font.render(f'Tempo: {timer_duration/1000:.1f}s', True, C_WHITE).convert_alpha()
            self.window.blit(fps,  (10, 5))
            self.window.blit(timer,  (10, 45))
            pygame.display.flip()

            # 4) Colisões gerais e remoção de entidades sem vida
            EntityMediator.verify_collision(e_list=self.e_list)
            EntityMediator.verify_life_entity(e_list=self.e_list)


