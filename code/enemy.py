#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.direction = "up"

    def move(self):

        if self.name == "Enemy3":
            self.rect.centerx -= ENTITY_SPEED[self.name]

            # Vertical movement controlled by steering
            if self.direction == "up":
                # Climbs at normal speed
                self.rect.centery -= ENTITY_SPEED[self.name]
                if self.rect.centery <= 0:
                    self.direction = "down"  # When the enemy reaches the top he goes down again
            elif self.direction == "down":
                self.rect.centery += ENTITY_SPEED[self.name] * 2
                if self.rect.centery >= WIN_HEIGHT:
                    self.direction = "up"
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
