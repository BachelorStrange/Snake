import pygame
import sys


class UserInterface:

    def __init__(self, ):
        self.score_font = pygame.font.SysFont("arial", 16)
        self.my_font = pygame.font.SysFont("arial", 36)

    def show_score(self, score, playground):
        score_display = self.score_font.render("Score: "+str(score), False, (255,255,255), (0,0,0))
        playground.screen.blit(score_display, (5, playground.playground_width-20))

    def game_over_screen(self, score, playground, handler):
        button_pressed = False
        button = None
        while not button_pressed:
            playground.screen.fill((0, 0, 0))
            surface = self.my_font.render("Game Over", False, (255, 255, 255), (0, 0, 0))
            final_score = self.my_font.render("Your Final Score: " + str(score), False, (255, 255, 255), (0, 0, 0))
            retry = self.my_font.render("Press R to restart", False, (255, 255, 255), (0, 0, 0))
            quit = self.my_font.render("Press Q to quit", False, (255, 255, 255), (0, 0, 0))
            playground.screen.blit(surface, (175, 200))
            playground.screen.blit(final_score, (130, 250))
            playground.screen.blit(retry, (130, 300))
            playground.screen.blit(quit, (130, 350))
            pygame.display.update()

            button_pressed, button = handler.game_over_handling()
            if button == "R":
                return True
            elif button == "Q":
                sys.exit()




if __name__ == "__main__":
    pass