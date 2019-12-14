from source.DragonDiceSimulator.GameState import GameState
from source.DragonDiceSimulator.Gameboard import Gameboard
from source.DragonDiceSimulator.Strategies import Strategies

if __name__ == '__main__':
    board = Gameboard()
    Strategies().strategy_just_roll_dumb()
    GameState().print_gamestate()


# Nevermind this :U
def calculate_divine_tickets_average():
    tickets_needed = calculate_tickets(300)
    current_iteration = 0.0

    while current_iteration < tickets_needed:
        current_iteration += 50
        tickets_needed -= calculate_tickets(2)

    tickets_needed_minus_free_chests = tickets_needed - round(tickets_needed/10)
    print(tickets_needed)
    print(tickets_needed_minus_free_chests)


def calculate_tickets(current_parts):
    return current_parts / 0.1077


