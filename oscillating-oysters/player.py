import itertools

# Class that declares the


class Player:
    p_ids = itertools.count()

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.id = next(self.p_ids)
        self.items = {}
        self.hp = 100
        self.level = 1

    def __repr__(self):
        cls = self.__class__.__name__
        return f"<{cls} User={self.username!r} id={self.id!r} hp={self.hp!r} level={self.level!r}>"

    # Returns an output off all the stats formatted into two columns
    def checkStats(self):
        return f'Player={self.username!r}\t Level={self.level!r}\n Items={self.items!r}\t HP={self.hp!r}\n'
