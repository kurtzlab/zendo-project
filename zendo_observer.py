"""
Zendo observer
"""
import random
from zendo_moderator import ZendoModerator
from structure import Structure
from rule import Rule
from constants import (
    RED, BLUE, YELLOW, EXACTLY, AT_LEAST, PYRAMIDS, WEDGES, BLOCKS
)


class ZendoObserver:
    """
    Play the role of observer in Zendo.
    """

    def __init__(self) -> None:
        pass


    def gen_test_structure(self):
        """
        Generates and returns a test structure
        """
        pass

    def does_test_structure_fit_moderator_rule(self, structure: Structure, moderator: ZendoModerator) -> bool:
        """
        Returns a boolean whether a structure matches the rule
        """
        return moderator.does_test_structure_fit_moderator_rule(structure)
