import os
import pygame


class Tile:
    #imgs = [pygame.image.load(os.path.join('assets/', 'cube.png'))]  # images depents on valid or non valid pos (collision())

    def __init__(self,ident, x, y, rotatiion ):
        self.x = x
        self.y = y
        self.rotation = rotatiion
        self.width = 200 #px
        self.height = 200 #px
        self.ident = ident
        self.img = pygame.image.load(os.path.join('assets/', 'cube.png'))  # input png url in assets
        self.img = pygame.transform.scale(self.img, (self.width, self.height))


    def draw(self, win):
        '''
        Draws the tile on right pos
        :param win: surface
        :return: none
        '''
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
        self.x = new_x
        self.y = new_y
        #self.rotation = new_rotation -> rotation still missing

    def remove(self):
        '''
        Remove this Tile
        :return: none
        '''
        self.x = 0
        self.y = 0

