import pygame
import os
from tiles.tile import Tile


class Game:

    def __init__(self):
        self.width = 1200
        self.height = 860
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load("assets/bg_default.png")
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = []
        self.tiles = []

    def run(self):
        run = True
        clock = pygame.time.Clock()
        self.draw()

        while run:
            clock.tick(60)
            draggin = False
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False


                pos = pygame.mouse.get_pos()  # later tuio input

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    self.create_tile(pos[0], pos[1])
                    print(pos)

            self.draw()
        pygame.quit()

    def draw(self):
        self.win.fill([255, 255, 255])
        self.win.blit(self.bg, (0, 0))

        for p in self.clicks:
            pygame.draw.circle(self.win, (255, 0, 0), (p[0], p[1]), 5, 0)
            count = 0
            for t in self.tiles:
                self.temp = self.tiles[count]
                count += 1
                self.temp.draw(self.win)
        pygame.display.update()

    def create_tile(self, pos_x, pos_y):
        name = 'ID' + str(len(self.tiles))
        print(name)
        self.ident = Tile(pos_x, pos_y, name)
        self.tiles.append(self.ident)


Game().run()
