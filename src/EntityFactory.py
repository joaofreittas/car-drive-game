#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from src.Background import Background
from src.Enemy import Enemy
from src.Player import Player
from src.util.Const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'street':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'street', (0, 0)))
                    list_bg.append(Background(f'street', (0, WIN_HEIGHT)))
                return list_bg
            case 'car-player':
                return Player('car-player', (WIN_WIDTH / 2, WIN_HEIGHT - 130))
            case 'car-enemy':
                print('enemy generated 2')
                return Enemy('car-enemy', (random.randint(40, WIN_WIDTH - 40), -100))

