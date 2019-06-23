import os

import pygame


class Tile:
    imgs = [pygame.image.load(
        os.path.join('assets/', 'cube.png'))]  # images depents on valid or non valid pos (collision())

    def __init__(self, x, y, ident):
        self.x = x
        self.y = y
        self.width = 200 #px
        self.height = 200 #px
        self.ident = ident
        self.img = pygame.image.load(os.path.join('assets/', 'cube.png'))  # input png url in assets
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.update_count = 0

    def draw(self, win):
        '''
        Draws the tile on right pos
        :param win: surface
        :return: none
        '''

        self.update_count += 1
        win.blit(self.img, (self.x, self.y))

    def collision(self, x, y):
        '''
        if pos is invalid should glow red or something
        :param x: int
        :param y: int
        :return: Bool
        '''
        if x <= self.x + self.width and x >= self.x:
            if y <= self.y + self.height and y >= self.y:
                return True
        return False

    def update(self, new_x, new_y):
        '''
        Repos this tile by contoller input
        :param new_y: int or float ... depents on Tuio input
        :param new_x: int or floar ... depents on Tuio input
        :return: none
        .... get input X and Y and move the tile obj.
        '''
        # if event something :

        # self.draw() ? vermutlich als 'redraw ' oder so

    def remove(self):
        '''
        Remove this Tile
        :return: none
        '''
