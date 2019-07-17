import os
import pygame


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
        self.NumberOfRows = 13
        self.NumberOfColumns = 20

    def generateField(self):
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
                        self.generateNewField(x, y, 2)
                        # newField = Field(x,y, 2)
                        # self.fields.append( newField )
                    else: #red
                        self.generateNewField(x, y, 3)
                        # newField = Field(x,y, 3)
                        # self.fields.append( newField )
                # third row of playarea
                elif 3<x<16 and y == 8: #green
                    if random.randrange(1,100)>10:
                        self.generateNewField(x, y, 2)
                        # newField = Field(x,y, 2)
                        # self.fields.append( newField )
                    else: #red
                        self.generateNewField(x, y, 3)
                        # newField = Field(x,y, 3)
                        # self.fields.append( newField )
                # fourth row of playarea
                elif 4<x<15 and y == 9: #green
                    if random.randrange(1,100)>10:
                        self.generateNewField(x, y, 2)
                        # newField = Field(x,y, 2)
                        # self.fields.append( newField )
                    else: #red
                        self.generateNewField(x, y, 3)
                        # newField = Field(x,y, 3)
                        # self.fields.append( newField )
                # fifth row of playarea
                elif 6<x<13 and y == 10: #green
                    if random.randrange(1,100)>10:
                        self.generateNewField(x, y, 2)
                        # newField = Field(x,y, 2)
                        # self.fields.append( newField )
                    else: #red
                        self.generateNewField(x, y, 3)
                        # newField = Field(x,y, 3)
                        # self.fields.append( newField )
                # area around the playable area
                else: #white
                    self.generateNewField(x, y, 0)
                    # newField = Field(x,y, 0)
                    # self.fields.append( newField )

    def generateNewField(self, x, y, type):
        newField = Field(x, y, type)
        self.fields.append( newField )

    def drawField(self):

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
