class GameState:
    strategy = ""
    emberstones_spent = 0
    current_position = 0

    blue_step_count = 0
    gold_step_count = 0
    red_step_count = 0
    checkpoint_step_count = 0
    total_movement_distance = 0
    full_laps = 0
    double_count = 0

    blue_keys = 0
    gold_keys = 0
    red_keys = 0

    blue_chests_opened = 0
    gold_chests_opened = 0
    red_chests_opened = 0

    blue_dragon_pieces = 0
    gold_dragon_pieces = 0
    red_dragon_pieces = 0

    def print_gamestate(self):
        print("Results of the simulation (strategy: {}) \n\n"
              "Emberstones spent: {} \n"
              "Current board position: {} \n"
              "\n"
              "Blue tiles stepped on: {} \n"
              "Gold tiles stepped on: {} \n"
              "Red tiles stepped on: {} \n"
              "Checkpoints stepped on: {} \n"
              "Total spaces moved: {} \n"
              "Full laps: {} \n"
              "Doubles rolled: {} \n"
              "\n"
              "Blue chests opened: {} \n"
              "Gold chests opened: {} \n"
              "Red chests opened: {} \n"
              "\n"
              "Blue dragon pieces: {} \n"
              "Gold dragon pieces: {} \n"
              "Red dragon pieces: {} \n".format(self.strategy, self.emberstones_spent, self.current_position,
                                                self.blue_step_count,
                                                self.gold_step_count, self.red_step_count, self.checkpoint_step_count,
                                                self.total_movement_distance, self.full_laps, self.double_count,
                                                self.blue_chests_opened,
                                                self.gold_chests_opened, self.red_chests_opened,
                                                self.blue_dragon_pieces, self.gold_dragon_pieces,
                                                self.red_dragon_pieces
                                                ))
