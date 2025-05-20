#!/usr/bin/python
#-*- coding: utf-8 -*-

from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.PlayerShoot import PlayerShoot


class EntityMediator:


    @staticmethod
    def verify_coll_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.vida = 0
        if isinstance(ent, PlayerShoot):
            if ent.rect.left >= WIN_WIDTH:
                ent.vida = 0

    @staticmethod
    def verify_coll_damage(Dmg1, Dmg2):
        if ((isinstance(Dmg1, Enemy) and isinstance(Dmg2, PlayerShoot)) or
            (isinstance(Dmg1, PlayerShoot) and isinstance(Dmg2, Enemy))):

            if Dmg1.rect.colliderect(Dmg2.rect):
                Dmg1.vida -= Dmg2.general_damage
                Dmg2.vida -= Dmg1.general_damage
                Dmg1.last_damage_taken = Dmg2.name
                Dmg2.last_damage_taken = Dmg1.name
            return



# --- 2) Colisão inimiga ↔ jogador, uma só vez por contato ---
        if ((isinstance(Dmg1, Enemy) and isinstance(Dmg2, Player)) or
            (isinstance(Dmg1, Player) and isinstance(Dmg2, Enemy))):

            # identifique quem é o Enemy e quem é o Player
            enemy, player = (Dmg1, Dmg2) if isinstance(Dmg1, Enemy) else (Dmg2, Dmg1)

            # se não estão sobrepostos, reset a flag para próximo contato
            if not enemy.rect.colliderect(player.rect):
                enemy.has_damaged_player = False
                return

    # se iniciando o contato (flag ainda é False), aplica dano
            if not enemy.has_damaged_player:
                player.vida -= enemy.general_damage
                player.last_damage_taken = enemy.name
                enemy.has_damaged_player = True
            return

    @staticmethod
    def __score_count(enemy: Enemy, enti_list: list[Entity]):
        if enemy.last_damage_taken == 'Arrow':
            for ent in enti_list:
                if ent.name == 'player1-11':
                    ent.get_score += enemy.get_score
                    pass

    @staticmethod
    def verify_collision(e_list: list[Entity]):
        for x in range(len(e_list)):
            e_collision = e_list[x]
            EntityMediator.verify_coll_window(e_collision)
            for y in range( x+1, len(e_list)):
                e_collision2 = e_list[y]
                EntityMediator.verify_coll_damage(e_collision,e_collision2)

    @staticmethod
    def verify_life_entity(e_list: list[Entity]):
        for entity in e_list:
            if entity.vida <= 0:
                if isinstance(entity, Enemy):
                    EntityMediator.__score_count(entity, e_list)
                e_list.remove(entity)
