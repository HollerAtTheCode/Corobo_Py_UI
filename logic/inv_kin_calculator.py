import numpy as np
import scipy
import math
import pygame

BASE_HEIGHT = 183
LINK01_LENGHT = 210  # in mm
LINK02_LENGHT = 180

joint01_rad = 0
joint02_rad = 0
joint03_rad = 0
joint05_rad = 0


class Segment_parent:
    def __init__(self, length, curr_x, curr_y, angle):
        self.LENGTH = length
        self.angle = angle
        self.curr_vector = (curr_x, curr_y)
        self.target_vector = (self.LENGTH, self.LENGTH)

    def draw(self, wins):
        pygame.draw.line(wins, (255, 255, 0), self.curr_vector, self.target_vector, 5)

    def update_angle(self, ty, tx):
        temp_angle = self.angle

        print(self.angle)
        pass

    def follow(self, target_x, target_y):
        new_target_vector = self.target_vector

        div_vector = np.subtract(new_target_vector, self.target_vector)
        dist_vector = np.subtract(self.target_vector, self.curr_vector)

        cos = div_vector[1] / self.LENGTH
        self.angle = np.arctan2(self.curr_vector[0], self.curr_vector[1])
        m = target_y / target_x
        orts_vector = (target_x - self.curr_vector[0], target_y - self.curr_vector[1])
        print(m * -1)
        self.target_vector = (target_x, target_y)

    # self.curr_vector = np.subtract(self.target_vector,
    #                               (self.LENGTH * math.cos(self.angle), self.LENGTH * math.sin(self.angle)))

    def update(self):
        self.angle += 0.0001
        pass


segment01 = Segment_parent(LINK02_LENGHT, 0, 0, 0)

while True:
    win = pygame.display.set_mode((800, 800), 1)
    segment01.draw(win)

    tx, ty = pygame.mouse.get_pos()
    #   segment02.follow(segment01.target_vector[0],segment01.target_vector[1])
    segment01.follow(tx, ty)
    pygame.display.flip()
