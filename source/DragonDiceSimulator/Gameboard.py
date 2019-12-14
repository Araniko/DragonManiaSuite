from source.DragonDiceSimulator.GameState import GameState


class Gameboard:
    gameboard = []

    def __init__(self):
        self.init_board()

    def init_board(self):
        self.gameboard = [
            Checkpoint, BlueTile, GoldTile, BlueTile, GoldTile, BlueTile, BlueTile, BlueTile, GoldTile, GoldTile,
            BlueTile, RedTile, BlueTile, GoldTile, RedTile, BlueTile, BlueTile, GoldTile, BlueTile, BlueTile, BlueTile,
            BlueTile, GoldTile, BlueTile, BlueTile, BlueTile, BlueTile, GoldTile, BlueTile,

            Checkpoint, BlueTile, GoldTile, BlueTile, RedTile, GoldTile, BlueTile, BlueTile, RedTile, BlueTile,
            BlueTile, GoldTile, BlueTile, BlueTile, GoldTile, BlueTile, BlueTile, GoldTile, BlueTile, BlueTile,
            GoldTile, BlueTile, BlueTile, BlueTile, BlueTile, GoldTile, BlueTile, BlueTile, GoldTile,

            Checkpoint, BlueTile, BlueTile, GoldTile, BlueTile, BlueTile, GoldTile, GoldTile, BlueTile, BlueTile,
            BlueTile, GoldTile, BlueTile, BlueTile, GoldTile, BlueTile, BlueTile, BlueTile, GoldTile, BlueTile,
            BlueTile, BlueTile, GoldTile, BlueTile, BlueTile, RedTile, BlueTile, GoldTile, RedTile, BlueTile
        ]


class BlueTile:
    tile_color = "Blue"

    def on_step(self, is_six):
        GameState.blue_step_count += 1
        GameState.blue_keys += 1
        if is_six:
            GameState.blue_keys += 1
        if GameState.blue_keys >= 3:
            GameState.blue_chests_opened += 1
            GameState.blue_dragon_pieces += 2.0016
            GameState.blue_keys -= 3


class GoldTile:
    tile_color = "Gold"

    def on_step(self, is_six):
        GameState.gold_step_count += 1
        GameState.gold_keys += 1
        if is_six:
            GameState.gold_keys += 1

        if GameState.gold_keys >= 3:
            GameState.gold_chests_opened += 1
            GameState.gold_dragon_pieces += 2.341
            GameState.gold_keys -= 3


class RedTile:
    tile_color = "Red"

    def on_step(self, is_six):
        GameState.red_step_count += 1
        GameState.red_keys += 1
        if is_six:
            GameState.red_keys += 1

        if GameState.red_keys >= 3:
            GameState.red_chests_opened += 1
            GameState.red_dragon_pieces += 2.4978
            GameState.red_keys -= 3


class Checkpoint:
    tile_color = "Prismatic"

    def on_pass(self, initial_position):
        self.reset_player_keys()
        if initial_position > 58:
            GameState.full_laps += 1
            self.open_all_chests()

    def on_step(self, is_six):
        GameState.checkpoint_step_count += 1
        if GameState.current_position == 0:
            GameState.full_laps += 1
            self.open_all_chests()
        self.choose_key(is_six)
        self.check_for_completed_chests()
        self.reset_player_keys()

    def reset_player_keys(self):
        # Future music: Transform keys into Emberstones.
        GameState.blue_keys = 0
        GameState.gold_keys = 0
        GameState.red_keys = 0

    def choose_key(self, is_six):
        # TODO: Extend logic to check for gold and blue chests
        GameState.red_keys += 1
        if is_six:
            GameState.red_keys += 1

    def open_all_chests(self):
        GameState.blue_chests_opened += 1
        GameState.gold_chests_opened += 1
        GameState.red_chests_opened += 1

        GameState.blue_dragon_pieces += 2.0016
        GameState.gold_dragon_pieces += 2.341
        GameState.red_dragon_pieces += 2.4978

    def check_for_completed_chests(self):
        if GameState.blue_keys >= 3:
            GameState.blue_chests_opened += 1
            GameState.blue_dragon_pieces += 2.0016
            GameState.blue_keys -= 3

        if GameState.gold_keys >= 3:
            GameState.gold_chests_opened += 1
            GameState.gold_dragon_pieces += 2.341
            GameState.gold_keys -= 3

        if GameState.red_keys >= 3:
            GameState.red_chests_opened += 1
            GameState.red_dragon_pieces += 2.4978
            GameState.red_keys -= 3
