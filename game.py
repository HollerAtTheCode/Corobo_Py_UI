import pygame
import os
from brick.Brick import Brick
from board.board import Board
import tuio


class Listener(tuio.observer.AbstractListener):

    #Why dont we update instead of deleting and creating an element anew
    #Implements a Listener
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

        self.info_objekt = pygame.display.Info()
        # width and height of field
        self.width = self.info_objekt.current_w
        self.height = self.info_objekt.current_h
        self.win = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN | pygame.HWSURFACE) # Game window
        self.board = Board(self.width, self.height) # Instance of the class Board
        # contains every brick on the field
        self.bricks = {}
        # contains the current poses of every brick on the field -> Key is marker id and value: [X-Pos,Y-Pos,Rotation-Angle]
        self.poses = {}

    def run(self):
        '''
        gameloop
        :return: none
        '''
        # Generate a GameBoard and save it in the board instance
        self.board.generate_field_array()
        run = True
        # create a Object to help track time
        clock = pygame.time.Clock()


        while run:
            clock.tick(60)  # fps = 60
            tuio.tracking.update()  # update for the Tuiolistener
            if len(self.poses) != 0:
                for key in self.poses: # Iterate all poses
                    temp = self.poses[key] # initialize temp with the value of the current pose
                    if key not in self.bricks: # checks if the tile is already existing if not it'll be created
                        self.create_brick(key, temp[0] * self.width, temp[1] * self.height, temp[2])
                        # print('new Tile rotation: ', temp[2])
                    else:
                        self.bricks[key].update(temp[0] * self.width, temp[1] * self.height, temp[2])
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN: # check if a Key is pressed
                    if event.key == pygame.K_q: # If so and the pressed Key is "q"
                        pygame.quit() # -> quit the game
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
        for k, v in self.bricks.items():
            temp_brick = v
            temp_brick.draw(self.win)

        pygame.display.update()

    listener = Listener("Event Listener", tuio.getEventManager())

    def create_brick(self, name, pos_x, pos_y, rot):
        '''
        crates new instance of class Tile and adds ot to the tiles dict.
        :param name: ident of tile
        :param pos_x: float
        :param pos_y: float
        :param rot: int
        :return: none
        '''
        ident = Brick(name, pos_x, pos_y, rot)
        self.bricks[name] = ident


pygame.init()
g = Game()

g.run()
