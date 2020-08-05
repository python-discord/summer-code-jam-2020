from typing import Tuple, List


class Location(object):
    """A game location object."""

    def __init__(
        self,
        coordinates: Tuple[int, int, int],
        npcs: List,
        enemies: List,
        items: List,
    ):
        self.coordinates = coordinates
        self.npcs = npcs
        self.enemies = enemies
        self.items = items
