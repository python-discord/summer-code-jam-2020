from typing import List

PLAYER_X = 'X'
PLAYER_O = 'O'


class TicTacToeBoard:
    # Game is small enough that this is fast
    WINNING_MOVES = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    def __init__(self, board=None):
        self.board = list(board) if board is not None else [None] * 9

    def _get_board_subset(self, a: int, b: int, c: int):
        return [self.board[a], self.board[b], self.board[c]]

    @property
    def is_end(self):
        if self.board.count(None) == 0:
            return True
        for moveset in self.WINNING_MOVES:
            set_of_vals = set(self._get_board_subset(*moveset))
            if (set_of_vals == {PLAYER_X} or set_of_vals == {PLAYER_O}):
                return True
        return False

    def child(self):
        return TicTacToeBoard(board=self.board)

    def calculate_score(self):
        for moveset in self.WINNING_MOVES:
            sect = self._get_board_subset(*moveset)
            if set(sect) == {PLAYER_X}:
                return 1
            if set(sect) == {PLAYER_O}:
                return -1

        return 0

    def make_move(self, pos: int, player: str):
        if self.board[pos] is not None:
            raise KeyError
        if player not in [PLAYER_X, PLAYER_O]:
            raise KeyError
        self.board[pos] = player

    def get_possible_moves(self):
        return [i for i, x in enumerate(self.board) if x is None]

    def __repr__(self):
        return (
            '{}|{}|{}\n'
            '{}|{}|{}\n'
            '{}|{}|{}\n'
        ).format(*self.board)


def play_game(board: List[int], player: str, move: int) -> List[int]:
    game = TicTacToeBoard(board=board)
    game.make_move(move, player)
    if game.is_end:
        return game.board, game.is_end, game.calculate_score()
    if player == PLAYER_X:
        computer_move, _ = minibon(game)
        computer_player = PLAYER_O
    else:
        computer_move, _ = maxibon(game)
        computer_player = PLAYER_X

    game.make_move(computer_move, computer_player)
    return game.board, game.is_end, game.calculate_score()


# minimax algorithm for computer player
def maxibon(parent_board: TicTacToeBoard, depth=0):
    if parent_board.is_end:
        return None, parent_board.calculate_score()
    moves = parent_board.get_possible_moves()
    king = moves[0]
    king_score = 0
    for move in moves:
        child_board = parent_board.child()
        child_board.make_move(move, PLAYER_X)
        _, score = minibon(child_board, depth=depth + 1)
        if score > king_score:
            king_score = score
            king = move
    return king, king_score


def minibon(parent_board: TicTacToeBoard, depth=0):
    if parent_board.is_end:
        return None, parent_board.calculate_score()
    moves = parent_board.get_possible_moves()
    king = moves[0]
    king_score = 0
    for move in moves:
        child_board = parent_board.child()
        child_board.make_move(move, PLAYER_O)
        _, score = maxibon(child_board, depth=depth + 1)
        if score <= king_score:
            king_score = score
            king = move
    return king, king_score
