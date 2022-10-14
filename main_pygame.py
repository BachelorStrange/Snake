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



class SnakeGame:

    def __init__(self, playground):
        self.tail_coords = list()
        self.playground = playground

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
        self.my_font = pygame.font.SysFont("arial", 36)
        self.score_font = pygame.font.SysFont("arial", 16)

    def show_score(self):
        score_display = self.score_font.render("Score: "+str(self.score), False, (255,255,255), (0,0,0))
        self.playground.screen.blit(score_display, (5, self.playground.playground_width-20))



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


    def event_handling(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.stepy = +self.step
                    self.stepx = 0

                elif event.key == K_UP:
                    self.stepy = -self.step
                    self.stepx = 0

                elif event.key == K_LEFT:
                    self.stepx = -self.step
                    self.stepy = 0

                elif event.key == K_RIGHT:
                    self.stepx = self.step
                    self.stepy = 0

            if event.type == KEYUP:
                if event.key == K_DOWN:
                    # y += step
                    self.stepy = self.step
                    self.stepx = 0

                elif event.key == K_UP:
                    self.stepy = -self.step
                    self.stepx = 0

                elif event.key == K_LEFT:
                    self.stepx = -self.step
                    self.stepy = 0

                elif event.key == K_RIGHT:
                    self.stepx = self.step
                    self.stepy = 0

if __name__ == "__main__":

    pygame.init()
    playground = Playground()
    g = SnakeGame(playground)

    while True:
        time.sleep(0.1)

        if playground.border_collision_detection(g.tail_coords):
            playground.screen.fill((0, 0, 0))
            surface = g.my_font.render("Game Over", False, (255,255,255), (0,0,0))
            final_score = g.my_font.render("Your Final Score: "+str(g.score), False, (255, 255, 255), (0, 0, 0))
            playground.screen.blit(surface, (175,200))
            playground.screen.blit(final_score, (130,250))
        else:
            playground.screen.fill((0, 0, 0))
            g.show_score()
            g.event_handling()
            g.create_apple()
            g.step_coords()
            g.queue_coords()

            g.apple_collision()
            g.redraw_tails()
            g.redraw_apples()

            g.counter += 1
        pygame.display.update()
