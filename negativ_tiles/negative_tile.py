
class Blocker:

    """
    Negative Block which makes a field on the Field unavailable
    """
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