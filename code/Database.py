import sys

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from datetime import datetime, date
from code.Const import C_WHITE, POSITION_SCORE_DISPLAY, MENU_OPTION, C_BLUE, C_YELLOW
from code.Proxy import Proxy


def date_format():
    now = datetime.now()
    date_now = now.strftime("%d/%m/%Y %H:%M")
    return date_now


class Database:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBG.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass


    def score_save_method (self, gamemode: str, score_player: int):
        proxy_db_commands = Proxy('PlayerScore')
        nameplayer = ''

        saving = True

        while saving:
            self.window.blit(self.surf, self.rect)
            self.score_save_display_text(60, 'GAME OVER', C_BLUE, POSITION_SCORE_DISPLAY['Title'])
            prompt = f'Enter your nickname (max 10 chars):'
            self.score_save_display_text(40, prompt, C_WHITE, POSITION_SCORE_DISPLAY['Prompt'])

            cursor = '|' if (pygame.time.get_ticks() // 500) % 2 == 0 else ''
            self.score_save_display_text(40, nameplayer + cursor, C_WHITE, POSITION_SCORE_DISPLAY['Name'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        # Valida e salva
                        if 1 <= len(nameplayer) <= 10:
                            proxy_db_commands.insert({
                                'NamePlayer': nameplayer,
                                'ScorePlayer': score_player,
                                'DateGame': date_format()
                            })
                            saving = False
                    elif event.key == K_BACKSPACE:
                        nameplayer = nameplayer[:-1]
                    else:
                        c = event.unicode
                        if c.isprintable() and len(nameplayer) < 10:
                            nameplayer += c

            pygame.display.flip()

        # Depois de sair do loop, volta ao menu
        return MENU_OPTION[0]

    def score_view_method (self):
        self.window.blit(source=self.surf, dest=self.rect)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_save_display_text(48, 'TOP 5 SCORE', C_YELLOW, POSITION_SCORE_DISPLAY['Title'])
        self.score_save_display_text(20, 'NAME     SCORE           DATE      ', C_WHITE, POSITION_SCORE_DISPLAY['Label'])
        proxy_db_commands = Proxy('PlayerScore')
        lista_score = proxy_db_commands.select()
        proxy_db_commands.close_db()

        for s in lista_score:
            id_, name, score, data = s
            self.score_save_display_text(20, f'{name}     {score:05d}     {data}', C_YELLOW,
                            POSITION_SCORE_DISPLAY[lista_score.index(s)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or K_BACKSPACE:
                        return
            pygame.display.flip()

    def score_save_display_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont(name="04b_03", size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)