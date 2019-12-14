from random import randint as random

from source.DragonDiceSimulator.GameState import GameState
from source.DragonDiceSimulator.Gameboard import BlueTile, GoldTile, RedTile, Checkpoint, Gameboard


class Player:
    def roll_dice(self):
        result = [random(1, 6), random(1, 6)]
        GameState.emberstones_spent += 200
        if result[0] == result[1]:
            GameState.double_count += 1
        return result

    def reroll_dice(self):
        GameState.emberstones_spent += 50
        return random(1, 6)

    def move(self, spaces, will_pass_checkpoint):
        board = Gameboard()
        initial_position = GameState.current_position

        GameState.total_movement_distance += spaces
        GameState.current_position += spaces
        GameState.current_position = GameState.current_position % 88
        self.evaluate_position(board.gameboard[GameState.current_position].tile_color, spaces == 6, will_pass_checkpoint, initial_position)

    def evaluate_position(self, tile_color, is_six, checkpoint_passed, initial_position):
        if checkpoint_passed:
            Checkpoint().on_pass(initial_position)

        if tile_color == 'Blue':
            BlueTile().on_step(is_six)

        if tile_color == 'Gold':
            GoldTile().on_step(is_six)

        if tile_color == 'Red':
            RedTile().on_step(is_six)

        if tile_color == 'Prismatic':
            Checkpoint().on_step(is_six)
