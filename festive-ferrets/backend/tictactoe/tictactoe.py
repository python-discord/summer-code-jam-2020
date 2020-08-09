class TicTacToe:
    def __init__(self, turn=1):
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

    def make_move(self, x, y):
        if not self.board[x][y]:
            self.board[x][y] = self.human
            if self.check_winner():
                return self.check_winner()
            self.best_move()
            if self.check_winner():
                return self.check_winner()

    def preview(self):
        return self.board

    def best_move(self):
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

    def minmax(self, d, is_max):
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
    def not_empty_eq(a, b, c):
        return a == b == c and a != ''

    def check_winner(self):
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
