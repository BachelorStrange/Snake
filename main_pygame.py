from event_handling import EventHandler
import pygame
from pygame.locals import *
from sys import exit
import time
import random
from playground import Playground
from user_interface import UserInterface


class SnakeGame:

    def __init__(self, playground, ui):
        self.tail_coords = list()
        self.playground = playground
        self.ui = ui

        x = 100
        y = 100

        self.snake_part_width = 9
        self.step = self.snake_part_width
        self.stepx = self.snake_part_width
        self.stepy = 0
        self.apples = list()
        self.counter = 0
        self.apple_radius = 4
        self.score = 0

        self.stepsx = list()
        self.stepsy = list()
        self.stepsx.append(self.stepx)
        self.stepsy.append(self.stepy)
        self.tail_coords.append((x, y))


    def create_apple(self):
        if self.counter % 5 == 0:
            x_position = self.playground.coords[random.randrange(0, self.playground.nr_fields)]
            y_position = self.playground.coords[random.randrange(0, self.playground.nr_fields)]
            pygame.draw.circle(self.playground.screen, (255, 0, 0), (x_position, y_position), self.apple_radius)
            self.apples.append((x_position, y_position))

    def redraw_apples(self):
        for apple in self.apples:
            pygame.draw.circle(self.playground.screen, (255, 0, 0), (apple[0], apple[1]), self.apple_radius)


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
        self.tail_coords.append((self.tail_coords[-1][0] - self.stepsx[-1],
                            self.tail_coords[-1][1] - self.stepsy[-1]))
        self.stepsx.append(self.stepx)
        self.stepsy.append(self.stepy)


    def queue_coords(self):
        for i in range(len(self.tail_coords)):
            newx = self.tail_coords[i][0] + self.stepsx[i]
            newy = self.tail_coords[i][1] + self.stepsy[i]
            self.tail_coords[i] = (newx,newy)

    def step_coords(self):
        for i in range(len(self.tail_coords) - 1, 0, -1):
            self.stepsx[i] = self.stepsx[i - 1]
            self.stepsy[i] = self.stepsy[i - 1]
        self.stepsx[0] = self.stepx
        self.stepsy[0] = self.stepy

    def redraw_tails(self):
        for coords in self.tail_coords:
            pygame.draw.rect(self.playground.screen, (150, 150, 150),
                             Rect((coords[0] - int(self.snake_part_width / 2),
                                   coords[1] - int(self.snake_part_width / 2)),
                                  (self.snake_part_width, self.snake_part_width)))


def main():

    pygame.init()
    playground = Playground()
    ui = UserInterface()
    g = SnakeGame(playground, ui)
    event_handler = EventHandler()

    while True:
        time.sleep(0.1)

        if playground.border_collision_detection(g.tail_coords):
            retry = ui.game_over_screen(g.score, playground, event_handler)
            if retry:
                main()
        elif playground.snake_collision_detection(g.tail_coords):
            retry = ui.game_over_screen(g.score, playground, event_handler)
            if retry:
                main()
        else:
            playground.screen.fill((0, 0, 0))
            ui.show_score(g.score, playground)
            event_handler.event_handling(g)
            g.create_apple()
            g.step_coords()
            g.queue_coords()

            g.apple_collision()
            g.redraw_tails()
            g.redraw_apples()

            g.counter += 1
        pygame.display.update()


if __name__ == "__main__":
    main()