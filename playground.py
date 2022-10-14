import pygame
from pygame.locals import *
from sys import exit
import time
import random


class Playground:

    def __init__(self, playground_width=500):
        self.screen = pygame.display.set_mode((playground_width, playground_width), 0, 32)
        self.field_width = 10
        self.nr_fields = int(playground_width/self.field_width)
        self.coords = self.valid_centers()
        self.playground_width = playground_width

    def valid_centers(self):
        coords = list()
        start = int(self.field_width/2)
        for i in range(self.nr_fields):
            start = start+self.field_width
            coords.append(start)

        return coords

    def border_collision_detection(self, tail_coords):
        x = tail_coords[0][0]
        y = tail_coords[0][1]
        if x >= self.screen.get_width():
            return True
        elif x <= 0:
            return True
        elif y >= self.screen.get_height():
            return True
        elif y <= 0:
            return True

    def snake_collision_detection(self, tail_coords):
        x = tail_coords[0][0]
        y = tail_coords[0][1]
        for i in range(1, len(tail_coords)):
            if x == tail_coords[i][0] and y == tail_coords[i][1]:
                return True
        return False




if __name__ == "__main__":
    pass