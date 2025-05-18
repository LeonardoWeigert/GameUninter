#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_WHITE, C_BLACK, C_RED, TIMEOUT_CHANGE_LEVEL, \
    TIMEOUT_GAME_OVER
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self,):
        while True:
            # Exibe menu
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                score_player = [0]

                # Fase 1
                self.change_level("FASE 1 START", score_player[0])
                level = Level(self.window, 'level1', menu_return, score_player)
                result = level.run(score_player)

                # Se player morreu no nível 1
                if result is False:
                    self.__game_over(level,final='levelGameOver1')
                    continue  # volta ao menu

                # Transição para Fase 2
                self.change_level("FASE 2 START", score_player[0])
                level = Level(self.window, 'level2', menu_return, score_player)
                result = level.run(score_player)

                if result is False:
                    self.__game_over(level,final='levelGameOver2')
                    continue

                # Transição para Fase 3
                self.change_level("FASE 3 START", score_player[0])
                level = Level(self.window, 'level3', menu_return, score_player)
                result = level.run(score_player)

                if result is False:
                    self.__game_over(level,final= 'levelGameOver3')
                    continue

            elif menu_return == MENU_OPTION[3]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pass

    def change_level(self, text, score = None):
        self.window.fill(C_BLACK)
        font = pygame.font.SysFont("04b_03", 32)
        msg = font.render(text, True, C_WHITE)
        rect = msg.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 30))
        self.window.blit(msg, rect)

        if score is not None:
            score_msg = font.render(f"Score: {score}", True, C_WHITE)
            rect_s = score_msg.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 30))
            self.window.blit(score_msg, rect_s)

        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.time.delay(TIMEOUT_CHANGE_LEVEL)  # espera 2 segundos

    def __game_over(self, level, final):
        # Exibe tela de Game Over e score final
        self.surf = pygame.image.load('./asset/'+ final +'.png').convert_alpha()
        font = pygame.font.SysFont("04b_03", 32)
        msg = font.render("GAME OVER", True, C_RED)
        rect = msg.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 30))
        self.window.blit(msg, rect)

        score_text = font.render(f"Score: {level.player.getscore}", True, C_WHITE)
        rect2 = score_text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 30))
        self.window.blit(score_text, rect2)

        pygame.display.flip()
        pygame.time.delay(TIMEOUT_GAME_OVER)

