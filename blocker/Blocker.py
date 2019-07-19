
class Blocker:

  
    #Blocker, prevents Bricks to be placend on this tile.
 
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def draw(self, win):
        '''
        Draws the tile on right pos
        :param win: surface
        :return: none
        '''
        win.blit(self.img, (self.x, self.y))