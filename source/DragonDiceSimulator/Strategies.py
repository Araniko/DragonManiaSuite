from source.DragonDiceSimulator.GameState import GameState
from source.DragonDiceSimulator.Gameboard import Gameboard
from source.DragonDiceSimulator.Player import Player


class Strategies:

    def prospected_colors(self, dice_roll_pair):
        board = Gameboard()

        first_tile_color = board.gameboard[GameState.current_position + dice_roll_pair[0]].tile_color
        second_tile_color = board.gameboard[GameState.current_position + dice_roll_pair[1]].tile_color
        return [first_tile_color, second_tile_color]

    def will_chest_be_finished(self, tile_color, key_amount):
        if tile_color == "Blue":
            if GameState.blue_keys + key_amount >= 3:
                return "Blue"

        if tile_color == "Gold":
            if GameState.gold_keys + key_amount >= 3:
                return "Gold"

        if tile_color == "Red":
            if GameState.red_keys + key_amount >= 3:
                return "Red"

        if tile_color == "Prismatic":
            if GameState.red_keys + key_amount > 3:
                return "Red"

            if GameState.gold_keys + key_amount > 3:
                return "Gold"

            if GameState.blue_keys + key_amount > 3:
                return "Blue"

        return False

    def will_pass_checkpoint(self, initial_position, roll):
        if initial_position < 29 < initial_position + roll:
            return True

        if initial_position < 58 < initial_position + roll:
            return True

        if initial_position < 88 < initial_position + roll:
            return True

        return False

    # Just move the first, then the second result. No fancy stuff added.
    def strategy_just_roll_dumb(self):
        GameState.strategy = "Take rolls as they come"
        rolls = 2500

        while rolls > 0:
            result = Player().roll_dice()
            for dice_result in result:
                Player().move(dice_result, self.will_pass_checkpoint(GameState.current_position, dice_result))
            rolls -= 1

    def strategy_just_roll_smart(self):
        return

    def strategy_reroll_aggressively_red(self):
        return

    def strategy_reroll_with_one_red_key(self):
        return
