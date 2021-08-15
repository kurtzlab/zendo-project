"""
Zendo game play
"""
import random
from zendo_moderator import ZendoModerator
from zendo_observer import ZendoObserver
from structure import Structure
from rule import Rule
from constants import (
    RED, BLUE, YELLOW, EXACTLY, AT_LEAST, PYRAMIDS, WEDGES, BLOCKS
)


class ZendoGame:
    """
    Play the role of observer in Zendo.
    """

    def __init__(self, difficulty="easy") -> None:
        self._moderator = ZendoModerator(difficulty=difficulty)
        self._observer = ZendoObserver()


    def play_zendo(self):
        """
        Plays zendo
        """
        pass
