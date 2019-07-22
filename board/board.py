import os
import sys
import pygame
import random
from .field import Field


class Board:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.NumberOfRows = 13
        self.NumberOfColumns = 20
        self.fields = {}
        self.imgs = [pygame.image.load('./assets/road_block_1.png').convert_alpha(), pygame.image.load(os.path.join('assets/', 'road_block_2.png')), pygame.image.load(os.path.join('assets/', 'background.png'))]  # images depents on valid or non valid pos (collision())
        self.bg = pygame.image.load('./assets/background.png').convert_alpha()

    def generate_field_array(self):
        '''
        crates new instance of the playarea
        :return: none
        '''

        # go through all board. depending on its position, assign a type
        # type 0: unplayable area - white
        # type 1: roboter position - blue
        # type 2: free field - green
        # type 3: blocked field - red (generated randomly)

        for x in range(self.NumberOfColumns):
            for y in range(self.NumberOfRows):
                # fields occupied by the robot
                if 7 < x < 12 and y < 4:
                    self.generate_field(x, y, 1)
                # first and second row of playarea
                elif 3 < x < 16 and 5 < y < 8:
                    # random placement of forbidden fields in the playarea
                    self.generate_playarea_field(x, y)
                # third row of playarea
                elif 3 < x < 16 and y == 8:
                    self.generate_playarea_field(x, y)
                # fourth row of playarea
                elif 4 < x < 15 and y == 9:
                    self.generate_playarea_field(x, y)
                # fifth row of playarea
                elif 6 < x < 13 and y == 10:  # green
                    self.generate_playarea_field(x, y)
                # area around the playable area
                else:  # outside of playarea
                    self.generate_field(x, y, 0)


    def generate_playarea_field(self, x, y):
        '''
        crates new field inside of the playarea
        90% probability of a playable field
        90% probability of a playable field
        :return: none
        '''
        # 90% probability of a playable field
        if random.randrange(1, 100) > 3:
            self.generate_field(x, y, 2)
        # 10% probability of blocked field
        else:
            self.generate_field(x, y, 3)


    def generate_field(self, x, y, type):
        '''
        crates new field in the fields{} dictionary
        The ID is generated like on a chess board, letters horizontal, numbers vertical
        :return: none
        '''
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
        ident = alphabet[x] + str(y)
        # add new field to the field array
        temp_field = Field(ident, x, y, type)
        self.fields.update({ident: temp_field})



    def draw_board(self, win):
        '''
        draw method for the board
        the background and playable fields are static
        blocked fields are displayed above the playable fields
        :return: none
        '''
        # draw the background image
        win.blit(self.bg,(60,15))
        # draw the forbidden fields in the play area
        for field in self.fields.values():
            if field.type == 3:  # red
                win.blit(self.imgs[0], (field.x_px, field.y_px))
