import blue
import red
import copy


def main():
    blue_ai_state = {}
    red_ai_state = {}
    board_state = initial_state()

    while True:
        blue_move, blue_ai_state = blue.make_move(copy.deepcopy(board_state), blue_ai_state)
        if determine_legality(blue_move):
            board_state = apply_move(board_state, blue_move)

        red_move, red_ai_state = red.make_move(copy.deepcopy(board_state), red_ai_state)
        board_state = apply_move(board_state, red_move)

        if game_winner(board_state) is not None:
            break


def initial_state():
    # returns the initial state of the game board
    state = {}
    state['shape'] = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    return state


def game_winner(game_state):
    # determines if there is a winner
    return None


def determine_legality(board_state, move):
    return True


def apply_move(old_board_state, new_move):
    # morphs the old state by the move and returns the new state
    new_board_state = old_board_state
    # mutate here

    return new_board_state



if __name__ == '__main__':
    main()
