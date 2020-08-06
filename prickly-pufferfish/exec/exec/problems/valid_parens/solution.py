class Solution:
    def __init__(self):
        self.valid_parens = []

    def valid_pairs(self, n: int):
        if n <= 0:
            return []

        self.gen_paren('', n, 0, 0)
        return self.valid_parens

    def gen_paren(self, parens: str, n: int, open: int, closed: int):
        if (open + closed) / 2 == n:
            self.valid_parens.append(parens)
            return

        if open > closed:
            self.gen_paren(
                parens + ')', n, open, closed+1
            )

        if open < n:
            self.gen_paren(
                parens + '(', n, open+1, closed
            )
