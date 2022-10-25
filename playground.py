import pygame
from pygame.locals import *


class Playground:

    def __init__(self, playground_width=500):
        self.screen = pygame.display.set_mode((playground_width, playground_width), 0, 32)
        self.field_width = 10
        self.nr_fields = int(playground_width/self.field_width)
        self.coords = self.calculate_field_center_points()
        self.playground_width = playground_width
        self.apple_radius = 4
        self.snake_part_width = 9

    def calculate_field_center_points(self):
        coords = list()
        start = int(self.field_width/2)
        for i in range(self.nr_fields):
            start = start+self.field_width
            coords.append(start)

        return coords

    def redraw_tails(self, tail_coords):
        for coords in tail_coords:
            pygame.draw.rect(self.screen, (150, 150, 150),
                             Rect((coords[0] - int(self.snake_part_width / 2),
                                   coords[1] - int(self.snake_part_width / 2)),
                                  (self.snake_part_width, self.snake_part_width)))

    def redraw_apples(self, apples):
        for apple in apples:
            pygame.draw.circle(self.screen, (255, 0, 0), (apple[0], apple[1]), self.apple_radius)


if __name__ == "__main__":
    pass
