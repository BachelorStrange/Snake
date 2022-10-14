import pygame
import time
from main_pygame import snake_game

if __name__ == "__main__":

    pygame.init()
    g = snake_game()

    while True:
        time.sleep(0.01)

        if g.border_collision_detection():
            g.screen.fill((150, 150, 150))
        else:

            if g.counter == 0:
                g.stepx = +g.step
                g.stepy = 0
            if g.counter == 1:
                g.stepx = 0
                g.stepy = +g.step
            g.step_coords()
            g.queue_coords()
            g.screen.fill((0, 0, 0))
            #g.apple_collision()
            g.redraw_tails()
            g.redraw_apples()
            g.create_apple()
            if g.apples:
                g.collision_happened(g.apples[0])
            g.counter += 1
        pygame.display.update()


