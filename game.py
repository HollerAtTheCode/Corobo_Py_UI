import pygame
import os
import random
from tiles.tile import Tile
import fields.field import Field
import tuio

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

class Field:
    def __init__(self, xId, yId, type ):
        self.xId = xId
        self.yId = yId
        # 25 Prozent der Groesse wars in Unity
        self.height = 50
        self.width = 50
        self.x = 10 + xId * self.height
        self.y = 10 + yId * self.width
        self.type = type

class Game:

    def __init__(self):
        self.width = 1600
        self.height = 900
        self.NumberOfRows = 13
        self.NumberOfColumns = 20
        self.win = pygame.display.set_mode((self.width, self.height))
        self.fields = []
        self.drawField()

        # self.bg = pygame.image.load(
        #     os.path.join('assets', 'bg_default.png'))  # bg picture -> needs to be random in future
        #
        # self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

        self.tiles = {}  # contains every tile on the field
        self.poses = {}  # contains the current poses of every tile on the field


    def run(self):
        '''
        gameloop
        :return: none
        '''
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
            for event in pygame.event.get():  # unused so far maybe later vor mouse or touch input to select level

                if event.type == pygame.QUIT:
                    run = False

            self.draw()
        pygame.quit()

    def draw(self):
        '''
        draws the field
        :return: none
        '''
        self.win.fill([255, 255, 255])
        # self.drawField()
        # self.win.blit(self.bg, (0, 0))
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

    def drawField(self):
        '''
        crates new instance of the playarea
        :return: none
        '''

        # go through all fields. depending on its position, assign a type
        # type 0: unplayable area - white
        # type 1: roboter position - blue
        # type 2: free field - green
        # type 3: blocked field - red (generated randomly)
        for x in range(self.NumberOfColumns):
            for y in range(self.NumberOfRows):
                # blue robot square
                if 7<x<12 and y<4: #blue
                    newField = Field(x,y, 1)
                    self.fields.append( newField )
                # first and second row of playarea
                elif 2<x<17 and 5<y<8: #green
                    if random.randrange(1,100)>10:
                        newField = Field(x,y, 2)
                        self.fields.append( newField )
                    else: #red
                        newField = Field(x,y, 3)
                        self.fields.append( newField )
                # third row of playarea
                elif 3<x<16 and y == 8: #green
                    if random.randrange(1,100)>10:
                        newField = Field(x,y, 2)
                        self.fields.append( newField )
                    else: #red
                        newField = Field(x,y, 3)
                        self.fields.append( newField )
                # fourth row of playarea
                elif 4<x<15 and y == 9: #green
                    if random.randrange(1,100)>10:
                        newField = Field(x,y, 2)
                        self.fields.append( newField )
                    else: #red
                        newField = Field(x,y, 3)
                        self.fields.append( newField )
                # fifth row of playarea
                elif 6<x<13 and y == 10: #green
                    if random.randrange(1,100)>10:
                        newField = Field(x,y, 2)
                        self.fields.append( newField )
                    else: #red
                        newField = Field(x,y, 3)
                        self.fields.append( newField )
                # area around the playable area
                else: #white
                    newField = Field(x,y, 0)
                    self.fields.append( newField )

        red = (255,0,0)
        green = (0,255,0)
        blue = (0,0,255)
        white = (255, 255, 255)
        black = (0,0,0)

        for field in self.fields:
            if field.type == 1: #blue
                pygame.draw.rect(self.win, blue, [field.x, field.y, field.width, field.height]);
                pygame.draw.rect(self.win, black, [field.x, field.y, field.width, field.height], 1);
            elif field.type == 2: #green
                pygame.draw.rect(self.win, green, [field.x, field.y, field.width, field.height]);
                pygame.draw.rect(self.win, black, [field.x, field.y, field.width, field.height], 1);
            elif field.type == 3: #red
                pygame.draw.rect(self.win, red, [field.x, field.y, field.width, field.height]);
                pygame.draw.rect(self.win, black, [field.x, field.y, field.width, field.height], 1);
            else: #white
                pygame.draw.rect(self.win, white, [field.x, field.y, field.width, field.height], 1);
                pygame.draw.rect(self.win, black, [field.x, field.y, field.width, field.height], 1);


g = Game()
g.run()
