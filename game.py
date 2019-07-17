import pygame
import os
from tiles.tile import Tile
from board.board import Board
import tuio
import keyboard



class Listener(tuio.observer.AbstractListener):

    # Implements a Listener
    def notify(self, event):
        ident = event.object.id
        if ident in g.poses:
            del g.poses[ident]
        x = event.object.xpos
        y = event.object.ypos
        rad = event.object.angle
        pos = [x, y, rad]
        g.poses[ident] = pos


class Game:

    def __init__(self):
        pygame.init()
        self.info_objekt = pygame.display.Info()
        self.width = self.info_objekt.current_w  # height of field from OS--- getSize oder so
        self.height = self.info_objekt.current_h
        self.win = pygame.display.set_mode((self.width, self.height),pygame.FULLSCREEN|pygame.HWSURFACE)
        self.board = Board(self.width, self.height)
        self.tiles = {}  # contains every tile on the field
        self.poses = {}  # contains the current poses of every tile on the field

    def run(self):
        '''
        gameloop
        :return: none
        '''
        self.board.generate_field_array()
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)  # fps = 60
            tuio.tracking.update()  # update for the Tuiolistener
            if len(self.poses) != 0:
                for key in self.poses:
                    temp = self.poses[key]  # the curren pose of the 'key', which is the same as in tiles
                    if key not in self.tiles:  # checks if the tile is already existing if not it'll be created
                        self.create_tile(key, temp[0] * self.width, temp[1] * self.height, temp[2])
                        print('new Tile: ', key)
                    else:
                        self.tiles[key].update(temp[0] * self.width, temp[1] * self.height)
            # print(len(self.poses), self.poses)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                        exit()


            self.draw()
        pygame.quit()

    def draw(self):
        '''
        draws the field
        :return: none
        '''
        self.win.fill([255, 255, 255])
        self.board.draw_board(self.win)
        '''
        redraw every tile every tick. Tile.draw(local window)
        '''
        for k, v in self.tiles.items():
            temp_tile = v
            temp_tile.draw(self.win)

        pygame.display.update()

    listener = Listener("Event Listener", tuio.getEventManager())

    def create_tile(self, name, pos_x, pos_y, rot):
        '''
        crates new instance of class Tile and adds ot to the tiles dict.
        :param name: ident of tile
        :param pos_x: float
        :param pos_y: float
        :param rot: int
        :return: none
        '''
        ident = Tile(name, pos_x, pos_y, rot)
        self.tiles[name] = ident


g = Game()
g.run()
