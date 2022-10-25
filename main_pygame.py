from event_handling import EventHandler
import pygame
from game_logic import GameLogic
import time
from playground import Playground
from user_interface import UserInterface


def main():

    pygame.init()
    playground = Playground()
    ui = UserInterface()
    event_handler = EventHandler(playground.snake_part_width)
    logic = GameLogic(playground)

    while True:
        time.sleep(0.1)

        if logic.border_collision_detection():
            retry = ui.game_over_screen(logic.score, playground, event_handler)
            if retry:
                main()
        elif logic.snake_collision_detection():
            retry = ui.game_over_screen(logic.score, playground, event_handler)
            if retry:
                main()
        else:
            playground.screen.fill((0, 0, 0))
            ui.show_score(logic.score, playground)
            event_handler.keyboard_event_handling(logic)
            logic.create_apple()
            logic.update_list_of_last_moves()
            logic.calculate_tail_coords_for_next_move()

            logic.apple_collision()
            playground.redraw_tails(logic.tail_coords)
            playground.redraw_apples(logic.apples)

            logic.counter += 1
        pygame.display.update()


if __name__ == "__main__":
    main()
