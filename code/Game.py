#!/usr/bin/python
#-*- coding: utf-8 -*-

import pygame


from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_WHITE, C_BLACK, C_RED, TIMEOUT_CHANGE_LEVEL, TIMEOUT_GAME_OVER
from code.Level import Level
from code.Menu import Menu
from code.Database import Database


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Database(self.window)
            # Exibe menu
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:  # NEW GAME
                total_score = 0
                # Fase 1
                self.change_level("FASE 1 START", total_score)
                level = Level(self.window, 'level1', menu_return, total_score)
                result = level.run()

                if result is False:
                    self.__game_over(level, final='levelGameOver1')
                    continue


                total_score += level.player.get_score
                self.change_level("FASE 2 START", level.player.get_score)
                level = Level(self.window, 'level2', menu_return, level.player.get_score)
                result = level.run()

                if result is False:
                    self.__game_over(level,final='levelGameOver2')
                    continue

                total_score += level.player.get_score
                self.change_level("FASE 3 START", level.player.get_score)
                level = Level(self.window, 'level3', menu_return, level.player.get_score)
                result = level.run()

                if result:
                    score.score_save_method(menu_return, level.player.get_score)

                if result is False:
                    self.__game_over(level,final= 'levelGameOver3')
                    continue

            elif menu_return == MENU_OPTION[2]:  # CONTROL
                self.control_menu()
                continue 
                
            elif menu_return == MENU_OPTION[3]:  # EXIT
                pygame.quit()
                quit()

            elif menu_return == MENU_OPTION[1]:  # SCORE RANK
                Database.score_view_method(score)

            else:
                pass

    def change_level(self, text, score = None):
        self.window.fill(C_BLACK)
        font = pygame.font.SysFont("04b_03", 32)
        msg = font.render(text, True, C_WHITE)
        rect = msg.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 30))
        self.window.blit(msg, rect)

        if text == 'FASE 1 START':
            pass
        else:
            if score is not None:
                score_msg = font.render(f"Score: {score}", True, C_WHITE)
                rect_s = score_msg.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 30))
                self.window.blit(score_msg, rect_s)

        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.time.delay(TIMEOUT_CHANGE_LEVEL)  # espera 2 segundos

    def __game_over(self, level, final):
        # Exibe tela de Game Over e score final
        score = Database(self.window)
        self.surf = pygame.image.load('./asset/'+ final +'.png').convert_alpha()
        font = pygame.font.SysFont("04b_03", 32)
        msg = font.render("GAME OVER", True, C_RED)
        rect = msg.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 30))
        self.window.blit(msg, rect)

        score_text = font.render(f"Score: {level.player.get_score}", True, C_WHITE)
        rect2 = score_text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 30))
        self.window.blit(score_text, rect2)

        pygame.display.flip()
        pygame.time.delay(TIMEOUT_GAME_OVER)

    def control_menu(self):
        # Limpa a tela com fundo preto
        surf_control = pygame.image.load('./asset/ControlBG.png').convert_alpha()
        rect_control = surf_control.get_rect(left=0, top=0)

        # Configura a fonte
        font = pygame.font.SysFont("04b_03", 32)
        font_small = pygame.font.SysFont("04b_03", 15)
        move_msg = font.render("Move: (arrow) Left Up Down Right or A W S D", True, C_WHITE)
        move_rect = move_msg.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 3))
        shoot_msg = font.render("Shoot: ESPACE", True, C_WHITE)
        shoot_rect = shoot_msg.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        back_msg = font_small.render("Press BACKSPACE to return", True, C_WHITE)
        back_rect = back_msg.get_rect(bottomleft=(10, WIN_HEIGHT - 10))


        running = True
        while running:
            self.window.blit(surf_control, rect_control)
            self.window.blit(move_msg, move_rect)
            self.window.blit(back_msg, back_rect)
            self.window.blit(shoot_msg, shoot_rect)
            pygame.display.flip()

            # Verifica eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        running = False
                        break
        return