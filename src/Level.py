#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from src.Enemy import Enemy
from src.GameOver import GameOver
from src.Player import Player
from src.util.Const import WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, C_BLACK, COLLISIONS_LIMIT, WIN_WIDTH, \
    DIFFICULT_SPAWN_TIME
from src.Entity import Entity
from src.EntityFactory import EntityFactory


class Level:
    def __init__(self, window: Surface, difficult):
        self.window = window
        self.difficult = difficult
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('street'))
        self.entity_list.append(EntityFactory.get_entity('car-player'))
        pygame.time.set_timer(EVENT_ENEMY, DIFFICULT_SPAWN_TIME[difficult])
        self.collisions_count = 0

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            player = next(ent for ent in self.entity_list if isinstance(ent, Player))
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for ent in self.entity_list:
                if isinstance(ent, Enemy) and player.rect.colliderect(ent.rect):
                    self.collisions_count = self.collisions_count + 1
                    self.entity_list.remove(ent)

                    if self.collisions_count == COLLISIONS_LIMIT:
                        game_over = GameOver(self.window)
                        game_over_return = game_over.run()

                        if game_over_return == "QUIT":
                            pygame.quit()
                            sys.exit()
                        elif game_over_return == "RESTART":
                            self.reset_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    print('enemy generated')
                    self.entity_list.append(EntityFactory.get_entity('car-enemy'))

            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_BLACK, (10, WIN_HEIGHT - 35))

            remaining_collisions = COLLISIONS_LIMIT - self.collisions_count
            self.level_text(30, f"Vidas: {remaining_collisions}", C_BLACK, (WIN_WIDTH - 100, 10))
            pygame.display.flip()

        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def reset_game(self):
        self.collisions_count = 0
        self.entity_list.clear()
        self.entity_list.extend(EntityFactory.get_entity('street'))
        self.entity_list.append(EntityFactory.get_entity('car-player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

