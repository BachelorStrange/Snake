import pygame
from pygame.locals import *


class EventHandler:

    def game_over_handling(self):
        button_pressed = False
        button = None
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_r:
                    button_pressed = True
                    button = "R"

            if event.type == KEYDOWN:
                if event.key == K_q:
                    button_pressed = True
                    button = "Q"

        return button_pressed, button

    def event_handling(self, g):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    g.stepy = +g.step
                    g.stepx = 0

                elif event.key == K_UP:
                    g.stepy = -g.step
                    g.stepx = 0

                elif event.key == K_LEFT:
                    g.stepx = -g.step
                    g.stepy = 0

                elif event.key == K_RIGHT:
                    g.stepx = g.step
                    g.stepy = 0

            if event.type == KEYUP:
                if event.key == K_DOWN:
                    # y += step
                    g.stepy = g.step
                    g.stepx = 0

                elif event.key == K_UP:
                    g.stepy = -g.step
                    g.stepx = 0

                elif event.key == K_LEFT:
                    g.stepx = -g.step
                    g.stepy = 0

                elif event.key == K_RIGHT:
                    g.stepx = g.step
                    g.stepy = 0