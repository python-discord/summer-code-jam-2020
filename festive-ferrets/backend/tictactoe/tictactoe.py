from typing import Union, Optional, List


class TicTacToe:
    def __init__(self, turn: int = 1):
        """
        :param turn: 1 - human first turn, 2 - AI first turn
        :type turn: int
        """
        self.score = {}
        self.turn = turn
        if self.turn == 1:
            self.score['O'] = 10
            self.score['X'] = -10
            self.human = 'X'
            self.ai = 'O'
        else:
            self.score['X'] = 10
            self.score['O'] = -10
            self.human = 'O'
            self.ai = 'X'
        self.score['tie'] = 0

        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        if self.turn == 2:
            self.best_move()

    def make_move(self, x: int, y: int) -> Optional[str]:
        """
        Make a human move followed by a move by the AI
        :param x: x - coordinate of the move
        :type x: int
        :param y: y - coordinate of the move
        :type y: int
        :return: If there is a winner, the winner, else None
        """
        if not self.board[x][y]:
            self.board[x][y] = self.human
            if self.check_winner():
                return self.check_winner()
            self.best_move()
            if self.check_winner():
                return self.check_winner()

    def preview(self) -> List[List[str]]:
        """
        Returns the current board state
        :return: Returns the current board state
        """
        return self.board

    def best_move(self) -> None:
        """
        Make the best predicted move by the AI
        :rtype: None
        """
        best_score = -float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    self.board[i][j] = self.ai
                    score = self.minmax(0, False)
                    self.board[i][j] = ''
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        self.board[move[0]][move[1]] = self.ai

    def minmax(self, d: int, is_max: bool) -> Union[int, float]:
        """
        Return a minmax score for the state tree
        :type d: int
        :type is_max: bool
        :return: Score for the state tree
        """
        result = self.check_winner()
        if result:
            return self.score[result]

        if is_max:
            best_score = -float('inf')
            player = self.ai
        else:
            best_score = float('inf')
            player = self.human
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    self.board[i][j] = player
                    score = self.minmax(d + 1, False)
                    self.board[i][j] = ''
                    best_score = max(score, best_score)
        return best_score

    @staticmethod
    def not_empty_eq(a: str, b: str, c: str) -> bool:
        """
        Returns True if all the variables are non empty strings and are equal
        :type a: str
        :type b: str
        :type c: str
        :return: Returns True if all the variables are non empty strings and are equal
        """
        return a == b == c and a != ''

    def check_winner(self) -> Union[bool, str]:
        """
        Returns the winner if there is a winner for the current state
        :return: False if no winner, 'X' or 'O' if either is winner
        """
        for i in range(len(self.board)):
            if self.not_empty_eq(self.board[i][0], self.board[i][1], self.board[i][2]):
                return self.board[i][0]

        for i in range(len(self.board)):
            if self.not_empty_eq(self.board[0][i], self.board[1][i], self.board[2][0]):
                return self.board[0][i]

        if self.not_empty_eq(self.board[0][0], self.board[1][1], self.board[2][2]):
            return self.board[1][1]
        if self.not_empty_eq(self.board[2][0], self.board[1][1], self.board[0][2]):
            return self.board[1][1]

        return False
