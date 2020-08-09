# I really, really wanted to do from enum import Enum
# Alas, transcrypt won't import from the standard library


class AwfulEnum:    # I'm so sorry
    def __init__(self):
        self._dict = {getattr(self, func): func for func in dir(self) if not func.startswith("__")}

    def __getitem__(self, item):
        return self._dict[item]


class _MessageTypes(AwfulEnum):
    TEXT = 1
    IMAGE = 2
    AUDIBLES = 3


MessageTypes = _MessageTypes()
