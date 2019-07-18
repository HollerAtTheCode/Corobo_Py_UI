import os
import pygame


class Tile:

    def __init__(self, ident, x, y, rotation):
        self.imgs = [pygame.image.load(os.path.join('assets/', 'border_curve.png')), pygame.image.load(
            os.path.join('assets/', 'border_straight.png'))]  # images depents on valid or non valid pos (collision())
        self.x = x
        self.y = y
        self.rotation = rotation
        self.width = 132  # px
        self.height = 132  # px
        self.ident = ident
        self.img = self.imgs[1]  # input png url in assets

    def draw(self, win):
        '''
        Draws the tile on right pos
        :param win: surface
        :return: none
        '''
        win.blit(self.img, (self.x - (self.width - 90)/2, self.y - (self.height-90)/2))

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
        self.x = new_x
        print(new_x ,'= X    ', new_y ,'= Y' )
        self.y = new_y
        # self.rotation = new_rotation -> rotation still missing

    def remove(self):
        '''
        Remove this Tile
        :return: none
        '''
        self.x = 0
        self.y = 0
