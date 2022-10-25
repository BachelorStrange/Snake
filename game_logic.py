import pygame
from pygame.locals import *
from sys import exit
import time
import random


class GameLogic:

    def __init__(self, playground):
        self.playground = playground
        self.score = 0
        self.apples = list()

        self.stepx = self.playground.snake_part_width
        self.stepy = 0
        self.stepsx = list()
        self.stepsy = list()
        self.stepsx.append(self.stepx)
        self.stepsy.append(self.stepy)
        self.counter = 0
        x = 100
        y = 100
        self.tail_coords = list()
        self.tail_coords.append((x, y))

    def border_collision_detection(self):
        x = self.tail_coords[0][0]
        y = self.tail_coords[0][1]
        if x >= self.playground.screen.get_width():
            return True
        elif x <= 0:
            return True
        elif y >= self.playground.screen.get_height():
            return True
        elif y <= 0:
            return True

    def snake_collision_detection(self):
        x = self.tail_coords[0][0]
        y = self.tail_coords[0][1]
        for i in range(1, len(self.tail_coords)):
            if x == self.tail_coords[i][0] and y == self.tail_coords[i][1]:
                return True
        return False

    def apple_collision(self):
        snake_center_x = self.tail_coords[0][0]
        snake_center_y = self.tail_coords[0][1]
        for apple in self.apples:
            apple_left = apple[0]-int(self.playground.field_width/2)
            apple_right = apple[0]+int(self.playground.field_width/2)
            apple_up = apple[1] - int(self.playground.field_width/2)
            apple_down = apple[1] + int(self.playground.field_width/2)

            if snake_center_x >apple_left and snake_center_x < apple_right:
                if snake_center_y > apple_up and snake_center_y < apple_down:
                    self.collision_happened(apple)

    def collision_happened(self, apple):
        self.score += 1
        self.apples.remove(apple)
        self.tail_coords.append((self.tail_coords[-1][0] - self.stepsx[-1], self.tail_coords[-1][1] - self.stepsy[-1]))
        self.stepsx.append(self.stepx)
        self.stepsy.append(self.stepy)

    def create_apple(self):
        if self.counter % 5 == 0:
            x_position = self.playground.coords[random.randrange(0, self.playground.nr_fields)]
            y_position = self.playground.coords[random.randrange(0, self.playground.nr_fields)]
            pygame.draw.circle(self.playground.screen, (255, 0, 0), (x_position, y_position),
                               self.playground.apple_radius)
            self.apples.append((x_position, y_position))

    def calculate_tail_coords_for_next_move(self):
        for i in range(len(self.tail_coords)):
            newx = self.tail_coords[i][0] + self.stepsx[i]
            newy = self.tail_coords[i][1] + self.stepsy[i]
            self.tail_coords[i] = (newx, newy)

    def update_list_of_last_moves(self):
        for i in range(len(self.tail_coords) - 1, 0, -1):
            self.stepsx[i] = self.stepsx[i - 1]
            self.stepsy[i] = self.stepsy[i - 1]
        self.stepsx[0] = self.stepx
        self.stepsy[0] = self.stepy


if __name__ == "__main__":
    pass
