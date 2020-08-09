class TicTacToe:
    def __init__(s, turn=1):
        s.score = dict()
        s.turn = turn
        if s.turn == 1:
            s.score["O"] = 10
            s.score["X"] = -10
            s.human = 'X'
            s.ai = 'O'
        else:
            s.score["X"] = 10
            s.score["O"] = -10
            s.human = 'O'
            s.ai = 'X'
        s.score["tie"] = 0

        s.t = [['', '', ''],
               ['', '', ''],
               ['', '', '']]
        if s.turn == 2:
            s.best_move()

    def play(s):
        while s.check_winner() is False:
            if s.turn == 2:
                s.best_move()
                s.preview()
                if s.check_winner() is not False:
                    print(s.check_winner())
                    return
                i = int(input())
                j = int(input())
                s.t[i][j] = s.human
                s.preview()
            else:
                i = int(input())
                j = int(input())
                s.t[i][j] = s.human
                s.preview()
                if s.check_winner() is not False:
                    print(s.check_winner())
                    return
                s.best_move()
                s.preview()
        print(s.check_winner())

    def make_move(self, x, y):
        if self.t[x][y] != '':
            return
        self.t[x][y] = self.human
        if self.check_winner():
            return self.check_winner()
        self.best_move()
        if self.check_winner():
            return self.check_winner()

    def preview(s):
        return s.t

    def best_move(s):
        best_score = -float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if s.t[i][j] == '':
                    s.t[i][j] = s.ai
                    score = s.minmax(0, False)
                    s.t[i][j] = ''
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        s.t[move[0]][move[1]] = s.ai

    def minmax(s, d, is_max):
        result = s.check_winner()
        if result is not False:
            return s.score[result]

        if is_max:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if s.t[i][j] == '':
                        s.t[i][j] = s.ai
                        score = s.minmax(d + 1, False)
                        s.t[i][j] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if s.t[i][j] == '':
                        s.t[i][j] = s.human
                        score = s.minmax(d + 1, True)
                        s.t[i][j] = ''
                        best_score = min(score, best_score)
        return best_score

    def not_empty_eq(s, a, b, c):
        return a == b == c and a != ''

    def check_winner(s):
        for i in range(len(s.t)):
            if s.not_empty_eq(s.t[i][0], s.t[i][1], s.t[i][2]):
                return s.t[i][0]

        for i in range(len(s.t)):
            if s.not_empty_eq(s.t[0][i], s.t[1][i], s.t[2][0]):
                return s.t[0][i]

        if s.not_empty_eq(s.t[0][0], s.t[1][1], s.t[2][2]):
            return s.t[1][1]
        if s.not_empty_eq(s.t[2][0], s.t[1][1], s.t[0][2]):
            return s.t[1][1]

        return False


def main():
    t = TicTacToe(1)
    t.play()


if __name__ == '__main__':
    main()
