#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.util.Const import ENTITY_SPEED, WIN_HEIGHT
from src.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]

        if self.rect.top >= WIN_HEIGHT:
            self.rect.bottom = 0
