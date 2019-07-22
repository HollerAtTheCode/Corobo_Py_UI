import os
import pygame
from math import *

class Brick:

    def __init__(self, ident, x, y, rotation):

        self.imgs = [pygame.image.load(os.path.join('assets/', 'border_straight.png')), pygame.image.load(
        os.path.join('assets/', 'border_curve.png')), pygame.image.load(os.path.join('assets/', 'border_straight_yellow.png')),
        pygame.image.load(os.path.join('assets/', 'border_curve_yellow.png')),
        pygame.image.load(os.path.join('assets/', 'border_straight_red.png')),
        pygame.image.load(os.path.join('assets/', 'border_curve_red.png'))]  # images depents on valid or non valid pos (collision())
        self.x = x
        self.y = y
        self.rotation = rotation
        self.width = 132  # px
        self.height = 132  # px
        self.ident = ident
		#Changed need to be tested
        self.field_id = ""
		#Type 1 is curve- type 0 is straightelement
        self.type = ident % 2
        #self.tile_id = pygame.
        self.img = self.imgs[self.type]  # input png url in assets


    def draw(self, win):
        '''
        Draws the tile on right pos
        :param win: surface
        :return: none
        '''
        rotated_img = pygame.transform.rotate(self.img, self.rotation)
        win.blit(rotated_img, (self.x - (self.width - 90)/2, self.y - (self.height-90)/2))

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

    def update(self, new_x, new_y,angle):
        '''
        Repos this tile by contoller input
        :param new_y: int or float ... depents on Tuio input
        :param new_x: int or floar ... depents on Tuio input
        :return: none
        .... get input X and Y and move the tile obj.
        '''
        self.rotation = angle
        self.x = new_x
        print(new_x ,'= X    ', new_y ,'= Y', angle, '= Rotate Angle')
        self.y = new_y
        self.field_id = self.assign_field_id_to_brick(new_x, new_y)
        # self.rotation = new_rotation -> rotation still missing

    def remove(self):
        self.x = 0
        self.y = 0

    def setImage(self,color):
        if(color == "yellow"):
            if(self.type == 1):
                self.img = self.imgs[3]
            else:
                self.img = self.imgs[2]
        if(color == "red"):
            if(self.type == 1):
                self.img = self.imgs[5]
            else:
                self.img = self.imgs[4]

    def assign_field_id_to_brick(self, pos_x, pos_y):
        #Array that hols column index
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
        #calculate column char
        print("Aktueller Index: "+str(int((pos_x - 60) / 90)))
        char_column = alphabet[int((pos_x - 60) / 90)]
        #calculate row number
        digit_row = int((pos_y - 15) / 90)
        #generate field id
        return (char_column + str(digit_row))
        #changed
    def get_type(self):
        return self.type
#changed
    def get_assigned_field_id(self):
        return self.field_id
