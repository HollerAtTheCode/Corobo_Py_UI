import os
import pygame


class Field:


    def __init__(self, xId, yId, type ):
        self.xId = xId
        self.yId = yId
        self.height = 50
        self.width = 50
        self.x = 10 + xId * self.height
        self.y = 10 + yId * self.width
        self.type = type
